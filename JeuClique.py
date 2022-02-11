from tkinter import *
import random
import configparser
import datetime
from pathlib import Path
from tkinter import messagebox

#Lecture du fichier de config
parser = configparser.ConfigParser()
parser.read("./Config.ini")
speed = parser['ReflexGame']['Speed'] = "800"
size = parser['ReflexGame']['GridSize'] = "5"
life = parser['ReflexGame']['Life'] = "4"

nbLine=int(size)
nbCols=int(size)+1
width=130*nbCols
height=130*nbLine
x0=130//2
y0=130//2

root=Tk()
root.title("Jeu tape-taupe")
root.resizable(width=False, height=False)
cnv=Canvas(root, width=width, height=height, bg='gray')
cnv.pack()
username= StringVar()

cover = PhotoImage(file="./images/PastilleRouge.png")
cover2 = PhotoImage(file="./images/PastilleGrise.png")
root.score = 0
root.Flag = False
root.life = int(life)
root.noclic = 0

def restart(loseWin):  
    loseWin.destroy()
    root.score = 0
    root.already_add = False
    root.life = int(life)
    root.noclic = 0
    MoveIcon()

def clic(event):
    root.noclic = 1
    x=event.x
    y=event.y
    line=x//130
    col=y//130
    if line == posX and col == posY:#Compris dans la case alors go
        cnv.create_image(x0+posX*130, y0+posY*130, image=cover2)
        if root.Flag == False:
            root.score += 1 
            root.Flag = True
    elif line != posX and col != posY:
        root.life -= 1

#Permet de créer le fichier de sauvegarde s'il n'existe pas
def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveClic") #Variable
    myfile.touch(exist_ok=True)

#Permet d'afficher la fenêtre de fin de jeu
def loseWindows():
    global loseWin
    loseWin = Toplevel(root)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: restart(loseWin)).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

    global ButtonSave
    ButtonSave = Button(loseWin, text="Save", width= 6 ,command= lambda: saveHighScore())
    ButtonSave.place(x=200, y=60)

    Label(loseWin, text=f"Username : ").place(x=8, y= 60)
    Label(loseWin, text="Vous avez perdu").pack()
    textBox = Entry(loseWin, textvariable=username, width=15)
    textBox.place(x=80,y=63)
    textBox.delete(0, END)

#Permet de faire bouger le cercle dans la grille de l'interface (#Fait apparaitre la pastille dans une case de la grille choisis aléatoirement)
def MoveIcon():
    print(root.noclic)
    if root.noclic == 0: #Permet en cas de clique d'enlever une vie
        root.life -= 1
    if root.life > 0:
        global posX 
        posX = random.randint(0,nbCols-1)
        global posY 
        posY = random.randint(0,nbLine-1)
        cnv.create_image(x0+posX*130, y0+posY*130, image=cover)
        root.after(speed, removeIcon) 
        root.after(speed, MoveIcon) 
        root.Flag = False
    else:
        loseWindows()
    root.noclic = 0

#Permet de sauvegarder les informations 
def saveHighScore():
    createFileIfNotExist()
    userName = username.get()
    #Permet d'éviter le champs vide
    if(len(userName) == 0):
        messagebox.showerror(title="Erreur nom d'utilisateur", message="Vous ne pouvez pas enregistrer un nom d'utilisateur vide")
    else:
        ButtonSave.config(state=DISABLED)
        f = open("./saves/highscoreSaveClic", "a")
        date = datetime.date.today()
        f.write(f"{date};{userName};{root.score};{speed}\n")
        f.close()

        #Permet de disable le boutton de sauvegarde
        ButtonSave.config(state=DISABLED)

#Cache la pastille avec une autre image de la même couleur que le fond
def removeIcon():
    cnv.create_image(x0+posX*130, y0+posY*130, image=cover2) #On enlève l'image

cnv.bind("<Button>", clic)
MoveIcon()

root.mainloop()