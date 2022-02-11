from tkinter import *
import random
import configparser
import datetime
from pathlib import Path

#TODO => Faire un morpion (A modif) - Faire sélection de jeu - Highscore - 

parser = configparser.ConfigParser()

parser.read("./Config.ini")
speed = parser['ReflexGame']['Speed'] = 800
size = parser['ReflexGame']['GridSize'] = 5
life = parser['ReflexGame']['Life'] = 4

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=int(size)
NB_COLS=int(size)+1
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

root=Tk()
root.resizable(width=False, height=False)
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='gray')
cnv.pack()
username= StringVar()

cover = PhotoImage(file="./images/PastilleRouge.png")
cover2 = PhotoImage(file="./images/PastilleGrise.png")
root.score = 0
root.already_add = False
root.life = int(life)
root.noclic = 0

def restart(loseWin):  
    loseWin.destroy()
    root.score = 0
    root.already_add = False
    root.life = int(life)
    root.noclic = 0
    phrase_refresh()

def clic(event):
    root.noclic = 1
    x=event.x
    y=event.y
    line=x//SIDE
    col=y//SIDE
    if line == a and col == b:#Compris dans la case alors go
        cnv.create_image(X0+a*SIDE, Y0+b*SIDE, image=cover2)
        if root.already_add == False:
            root.score += 1 
            print("Score : ", root.score)
            root.already_add = True
    elif line != a and col != b:
        root.life -= 1

def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveClic") #Variable
    myfile.touch(exist_ok=True)
    f = open(myfile)

def phrase_refresh():
    print(root.noclic)
    if root.noclic == 0: #Permet en cas de clique d'enlever une vie
        root.life -= 1
    if root.life > 0:
        global a 
        a = random.randint(0,NB_COLS-1)
        global b
        b = random.randint(0,NB_LINES-1)
        cnv.create_image(X0+a*SIDE, Y0+b*SIDE, image=cover)
        root.after(speed, phrase_derefresh)
        root.after(speed, phrase_refresh)
        root.already_add = False
    else:
        print("Vous avez perdu")
        #Afficher truc avec Tkinter
        loseWin = Toplevel(root)
        loseWin.resizable(width=False, height=False)
        loseWin.geometry("300x150")
        Button(loseWin, text="Rejouer", command= lambda: restart(loseWin)).place(x=50, y=100) #BtnRestart
        Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

        global ButtonSave
        ButtonSave = Button(loseWin, text="Highscore", command= lambda: saveHighScore())
        ButtonSave.place(x=200, y=60) #BtnSaveHighScore

        Label(loseWin, text="Vous avez perdu").pack()
        Entry(loseWin, textvariable=username).place(x=50,y=60)
        Label(loseWin, text=f"Votre score : {root.score}").pack()
    root.noclic = 0

def saveHighScore():

    createFileIfNotExist()
    userName = username.get()
    if(len(userName == 0)):
        print("Erreur")
    else:
        ButtonSave.config(state=DISABLED)
        f = open("./saves/highscoreSaveClic", "a")
        date = datetime.date.today()
        f.write(f"{date};{userName};{root.score};{speed}\n")
        f.close()

def phrase_derefresh():
    cnv.create_image(X0+a*SIDE, Y0+b*SIDE, image=cover2) #On enlève l'image

cnv.bind("<Button>", clic)
phrase_refresh()

root.mainloop()