from cgitb import text
from faulthandler import disable
from tkinter import *
import random
from subprocess import run
import datetime
import configparser
from pathlib import Path
import time
from tkinter import messagebox

parser = configparser.ConfigParser()

parser.read("./Config.ini")
timeMinReac = parser['ReactGame']['TempsMinReac'] = "1"
timeMaxReac = parser['ReactGame']['TempsMaxReac'] = "7"

root = Tk()
root.geometry("310x250")
root.resizable(width=False, height=False)
username= StringVar()
root.start = 0
root.end = 0
root.counter = 0
root.cpt = 0

#Todo -> Gérer le Highscore

def key(event):
    print("pressed", repr(event.char))

def saveHighScore():
        createFileIfNotExist()
        userName = username.get()
        if(len(userName) == 0):
                messagebox.showerror(title="Erreur nom d'utilisateur", message="Vous ne pouvez pas enregistrer un nom d'utilisateur vide")
        else:
                ButtonSave.config(state=DISABLED)
                f = open("./saves/highscoreSaveReact", "a")
                f.write(f"{datetime.date.today()};{userName};{round(root.end-root.start, 3)}")
                f.close()

                ButtonSave.config(state=DISABLED)

def restart(event):
        canvas.config(bg="blue")
        root.counter = 0
        root.cpt += 1
        root.destroy()
        run("python ./TempsReaction.py") #Permet de relancer l'application
        
def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveReact") #Variable
    myfile.touch(exist_ok=True)

def loseWindows(event):
    #Afficher truc avec Tkinter
    global loseWin
    loseWin = Toplevel(root)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: restart(event)).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

    #Gérer le highscore
    global ButtonSave
    ButtonSave = Button(loseWin, text="Save", width= 6 ,command= lambda: saveHighScore())
    ButtonSave.place(x=200, y=60) #BtnSaveHighScore

    Label(loseWin, text=f"Username : ").place(x=8, y= 60)
    Label(loseWin, text=f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} ms.").pack()
    y = Entry(loseWin, textvariable=username, width=12).place(x=80,y=57)
    y.place(x=80,y=57)
    y.delete(0, END)
    
def updateTime(event):
        if root.counter == 0:
                time.sleep(random.randint(int(timeMinReac),int(timeMaxReac))) #à rentre "aléatoire"
                canvas.configure(bg="green")
                root.start = time.perf_counter()
                print(root.counter)
                root.cpt +=1
        if root.counter == 1:
                root.end = time.perf_counter()
                print(f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} secondes")
                canvas.unbind("<Button-1>")   
                loseWindows(event)     
        root.counter = 1
        
titre = Label(root, text="Jeu de réflexe")
titre.pack()

canvas= Canvas(root, width=200, height=100, bd=15, bg="blue", highlightthickness=3, highlightbackground="black")
canvas.create_text(120,60, fill="black", text="Click on me.")
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", updateTime)
canvas.pack(pady=30)
        
root.mainloop()