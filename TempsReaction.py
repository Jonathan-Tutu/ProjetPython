from cgitb import text
from faulthandler import disable
from tkinter import *
import random
from subprocess import run
import datetime
import configparser

import time

parser = configparser.ConfigParser()

parser.read("./Config.ini")
speed = parser['ReactGame']['TempsMin']
size = parser['ReactGame']['TempsMax']


root = Tk()
root.geometry("310x300")
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
        userName = username.get()
        ButtonSave.config(state=DISABLED)
        f = open("./saves/highscoreSaveReact", "a")
        f.write(f"{datetime.date.today()};{userName};{round(root.end-root.start, 3)}")
        f.close()

def replay(event):
        canvas.config(bg="blue")
        root.counter = 0
        root.cpt += 1
        root.destroy()
        run("python ./TempsReaction.py") #Permet de relancer l'application
        
def updateTime(event):
        if root.counter == 0:
                time.sleep(random.randint(1,7)) #à rentre "aléatoire"
                canvas.configure(bg="green")
                root.start = time.perf_counter()
                print(root.counter)
                root.cpt +=1
        if root.counter == 1:
                root.end = time.perf_counter()
                print(f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} secondes")
                canvas.unbind("<Button-1>")
                Entry(root, textvariable=username).place(x=100,y=243)
                global ButtonSave
                ButtonSave =  Button(root, text="Highscore", command=lambda: saveHighScore()).place(x=240,y=240)
                ButtonSave.place(x=240,y=270)
                Button(root, text="Relancer", command=lambda: replay(event))
                titre1.config(text=f"Votre temps  de réaction à été de {round(root.end-root.start, 3)} ms.")
        root.counter = 1
        
titre = Label(root, text="Jeu de réflexe")
titre.pack()

canvas= Canvas(root, width=200, height=100, bd=15, bg="blue", highlightthickness=3, highlightbackground="black")
canvas.create_text(120,60, fill="black", text="Click on me.")
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", updateTime)
canvas.pack(pady=30)

titre1 = Label(root, text="Votre temps  de réaction à été de 0 ms")
titre1.pack()
        
root.mainloop()