from tkinter import *
import random
from subprocess import run
import datetime
import configparser
from pathlib import Path
import time
from tkinter import messagebox

#Lecture du fichier de config
parser = configparser.ConfigParser()
parser.read("./Config.ini")
timeMinReac = parser['ReactGame']['TempsMinReac'] = "1"
timeMaxReac = parser['ReactGame']['TempsMaxReac'] = "7"

#Permet de sauvegarder les informations 
def saveHighScore():
        createFileIfNotExist()
        userName = username.get()
        #Permet d'éviter le champs vide
        if(len(userName) == 0):
                messagebox.showerror(title="Erreur nom d'utilisateur", message="Vous ne pouvez pas enregistrer un nom d'utilisateur vide")
        else:
                f = open("./saves/highscoreSaveReact", "a")
                f.write(f"{datetime.date.today()};{userName};{round(root.end-root.start, 3)}\n")
                f.close()

                #Permet de disable le boutton de sauvegarde
                ButtonSave.config(state=DISABLED)

#Permet de relancer le jeu. c'est le moyen le plus simple
def restart():
        canvas.config(bg="blue")
        root.counter = 0
        root.destroy() #On détruit la fenêtre
        run("python ./TempsReaction.py") #Permet de relancer l'application
        
#Permet de créer le fichier de sauvegarde s'il n'existe pas
def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveReact") #Variable
    myfile.touch(exist_ok=True)

#Permet d'afficher la fenêtre de fin de jeu
def loseWindows():
    global loseWin
    loseWin = Toplevel(root)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: restart()).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

    global ButtonSave
    ButtonSave = Button(loseWin, text="Save", width= 6 ,command= lambda: saveHighScore())
    ButtonSave.place(x=200, y=60) #BtnSaveHighScore

    Label(loseWin, text=f"Username : ").place(x=8, y= 60)
    Label(loseWin, text=f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} ms.").pack()
    textBox = Entry(loseWin, textvariable=username, width=15)
    textBox.place(x=80,y=63)
    textBox.delete(0, END)

#Permet de gérer le clic sur le rectangle
def updateTime(self):
        if root.counter == 0:
                time.sleep(random.randint(int(timeMinReac),int(timeMaxReac))) #Valeur aléatoire
                canvas.configure(bg="green")
                root.start = time.perf_counter() #Lance un timer
                print(root.counter)
        if root.counter == 1:
                root.end = time.perf_counter() #Stop le timer
                print(f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} secondes") #Permet de calculer la différence de temps et donc de donner le temps de réaction
                canvas.unbind("<Button-1>")   
                loseWindows()     
        root.counter = 1

root = Tk()
root.title("Jeu de temps de réaction")
root.geometry("310x250")
root.resizable(width=False, height=False)
username= StringVar()
root.start = 0
root.end = 0
root.counter = 0

titre = Label(root, text="Jeu de réflexe")
titre.pack()

canvas= Canvas(root, width=200, height=100, bd=15, bg="blue", highlightthickness=3, highlightbackground="black")
canvas.create_text(120,60, fill="black", text="Click on me.")
canvas.bind("<Button-1>", updateTime)
canvas.pack(pady=30)
                
root.mainloop()