from tkinter import *
from PIL import ImageTk, Image  
from subprocess import run
import csv
from tkinter import ttk

#Permet de lancer le jeu de clique
def runGameClique():
    run("python ./JeuClique.py")

#Permet de lancer le jeu Reaction
def runGameReact():
    run("python ./TempsReaction.py")

#Permet de lancer le jeu du morpion
def runGameMorpion():
    run("python ./Morpion.py")

#Affichage des highscores du jeu de temps de reaction grâce à TtkTreedef 
def showHighScoreGameClic():
    tempList = []
    #On parse le fichier
    with open('./saves/highscoreSaveClic', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)
                
    tempList.sort(key=lambda e: e[2], reverse=False)
    cols = ('Position', 'Date', 'Name', 'Score','Vitesse')
    scores = Tk() 
    scores.title("Score Tape-Taupe")
    
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for i in range(6):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (date, name, score, vitesse) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, date, name, score, vitesse))
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

#Affichage des highscores du jeu de reaction grâce à TtkTree
def showHighScoreGameReact():
    tempList = []
    #On parse le fichier
    with open('./saves/highscoreSaveReact', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)

    tempList.sort(key=lambda e: e[2], reverse=False)
    cols = ('Position', 'Date', 'Name', 'Score')
    scores = Tk() 
    scores.title("Score Jeu Réaction")

    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for i in range(5):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (date, name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, date, name, score))
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

#Affichage des highscores du jeu du morpion grâce à TtkTree
def showHighScoreGameMorpion():
    tempList = []
    #On parse le fichier
    with open('./saves/highscoreSaveMorpion', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)

    tempList.sort(key=lambda e: e[1], reverse=True)
    cols = ('Position', 'Name', 'Nb Victoire')
    scores = Tk() 
    scores.title("Score Morpion")

    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for i in range(4):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (name, nbVictoire) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, nbVictoire))
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

#Création de toute la fenêtre
root = Tk() 
root.title("Launcheur") 
root.resizable(width=False, height=False)
root.geometry("620x500") 

labelTitre1 = Label(root, text="JEU DE REFLEXE", font='Helvetica 18 bold')
labelTitre1.place(x=20, y=20)

labelTitre2 = Label(root, text="JEU DE REFLEXION", font='Helvetica 18 bold')
labelTitre2.place(x=20, y=250)

imageJeuClique = Image.open("./images/LogoJeuClique.png")
imageJeuCliqueTk = ImageTk.PhotoImage(imageJeuClique)

imageJeuReact = Image.open("./images/LogoJeuTempsReaction.png")
imageJeuReactTk = ImageTk.PhotoImage(imageJeuReact)

imageLogoPlusl1 = Image.open("./images/Logo+.png")
imageLogoPlusl1Tk = ImageTk.PhotoImage(imageLogoPlusl1)

imageJeuMorpion = Image.open("./images/Logo Morpion.png")
imageJeuMorpionTk = ImageTk.PhotoImage(imageJeuMorpion)

imageLogoPlusl2 = Image.open("./images/Logo+.png")
imageLogoPlusl2Tk = ImageTk.PhotoImage(imageLogoPlusl2)

#Premier bloc de jeu (Jeu de clic)
label1 = Label(root, image=imageJeuCliqueTk, width=150, height=150, borderwidth=1, relief="solid")
label1.image = imageJeuCliqueTk
label1.place(x=40, y=60)
buttonPlay1 = Button(root, text="Jouer", command= lambda: runGameClique())
buttonPlay1.place(x=40, y=215)
buttonHighscore1 = Button(root, text="Highscore", command= lambda: showHighScoreGameClic())
buttonHighscore1.place(x=126, y=215)

#Seconde bloc de jeu (Jeu de temps de réaction)
label2 = Label(root, image=imageJeuReactTk, width=150, height=150, borderwidth=1, relief="solid")
label2.image = imageJeuReactTk
label2.place(x=240, y=60)
buttonPlay2 = Button(root, text="Jouer", command= lambda: runGameReact())
buttonPlay2.place(x=240, y=215)
buttonHighscore2 = Button(root, text="Highscore", command= lambda: showHighScoreGameReact())
buttonHighscore2.place(x=326, y=215)

#Premier bloc +
label3 = Label(root, image=imageLogoPlusl1Tk, width=150, height=150, borderwidth=1, relief="solid")
label3.image = imageLogoPlusl1Tk
label3.place(x=440, y=60)

#Quatrième bloc de jeu
label4 = Label(root, image=imageJeuMorpionTk, width=150, height=150, borderwidth=1, relief="solid")
label4.image = imageJeuMorpionTk
label4.place(x=40, y=290)
buttonPlay3 = Button(root, text="Jouer", command= lambda: runGameMorpion())
buttonPlay3.place(x=40, y=445)
buttonHighscore3 = Button(root, text="Highscore", command= lambda: showHighScoreGameMorpion())
buttonHighscore3.place(x=126, y=445)

#Deuxième bloc +
label5 = Label(root, image=imageLogoPlusl2Tk, width=150, height=150, borderwidth=1, relief="solid")
label5.image = imageLogoPlusl2Tk
label5.place(x=240, y=290)

root.mainloop()
