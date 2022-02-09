from distutils import command
from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image  
from subprocess import run
import csv
from tkinter import ttk


def runGame1():
    run("python ./Nouveau.py")

def runGame2():
    run("python ./TempsReaction.py")

def runGame3():
    run("python ./Morpion.py")

def showHighScorGame1():
    tempList = []
    with open('./saves/highscoreClic', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)
                
    print(tempList)
    tempList.sort(key=lambda e: e[2], reverse=False)

    cols = ('Position', 'Date', 'Name', 'Score','Vitesse')
    scores = Tk() 
    
    listBox = ttk.Treeview(scores, columns=cols, show='headings')

    for i in range(6):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (date, name, score, vitesse) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, date, name, score, vitesse))

    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)



def showHighScorGame2():
    tempList = []
    with open('./saves/highscoreSaveReact', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)

    print(tempList)
    tempList.sort(key=lambda e: e[2], reverse=False)
    cols = ('Position', 'Date', 'Name', 'Score')
    scores = Tk() 

    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for i in range(5):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (date, name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, date, name, score))
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

def showHighScorGame3():
    tempList = []
    with open('./saves/highscoreSaveMorpion', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')     
        for row in spamreader:    
            tempList.append(row)

    print(tempList)
    tempList.sort(key=lambda e: e[2], reverse=False)
    cols = ('Position', 'Date', 'Name', 'Score','Vitesse')
    scores = Tk() 

    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    for i in range(6):
        listBox.column(f"#{i}", anchor=CENTER, stretch=NO)
    for i, (date, name, score, vitesse) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, date, name, score, vitesse))
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

root = Tk() 
root.title("New Window") 
root.resizable(width=False, height=False)
root.geometry("620x500") 

labelTitre1 = Label(root, text="JEU DE REFLEX", font='Helvetica 18 bold')
labelTitre1.place(x=20, y=20)

labelTitre2 = Label(root, text="JEU DE REFLEXION", font='Helvetica 18 bold')
labelTitre2.place(x=20, y=250)

image1 = Image.open("./images/LogoJeuClique.png")
test1 = ImageTk.PhotoImage(image1)

image2 = Image.open("./images/LogoJeuTempsReaction.png")
test2 = ImageTk.PhotoImage(image2)

image3 = Image.open("./images/Logo+.png").resize((50,50), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(image3)

image4 = Image.open("./images/Logo Morpion.png")
test4 = ImageTk.PhotoImage(image4)

image5 = Image.open("./images/Logo+.png").resize((50,50), Image.ANTIALIAS)
test5 = ImageTk.PhotoImage(image5)




label1 = Label(root, image=test1, width=150, height=150, borderwidth=1, relief="solid")
label1.image = test1
label1.place(x=40, y=60)
button1 = Button(root, text="Jouer", command= lambda: runGame1())
button1.place(x=40, y=215)
button11 = Button(root, text="Highscore", command= lambda: showHighScorGame1())
button11.place(x=126, y=215)
tip = Balloon(root)
tip.bind_widget(label1,balloonmsg="Le but du jeu ici est simple, il suffit de cliquer sur les cercles rouges qui vont apparaitres avant que ceux ci ne disparaissent")

label2 = Label(root, image=test2, width=150, height=150, borderwidth=1, relief="solid")
label2.image = test2
label2.place(x=240, y=60)
button2 = Button(root, text="Jouer", command= lambda: runGame2())
button2.place(x=240, y=215)
button22 = Button(root, text="Highscore", command= lambda: showHighScorGame2())
button22.place(x=326, y=215)
tip2 = Balloon(root)
tip2.bind_widget(label2,balloonmsg="Le but du jeu ici est de faire le temps le plus cours en appuyant le plus rapidement lorsque le rectangle change de couleur")




label3 = Label(root, image=test3, width=150, height=150, borderwidth=1, relief="solid")
label3.image = test3
label3.place(x=440, y=60)
tip3 = Balloon(root)
tip3.bind_widget(label3,balloonmsg="Plus de jeu à venir")




label4 = Label(root, image=test4, width=150, height=150, borderwidth=1, relief="solid")
label4.image = test4
label4.place(x=40, y=290)
button4 = Button(root, text="Jouer", command= lambda: runGame3())
button4.place(x=40, y=445)
button44 = Button(root, text="Highscore", command= lambda: showHighScorGame3())
button44.place(x=126, y=445)
tip4 = Balloon(root)
tip4.bind_widget(label4,balloonmsg="Le but du jeu est d'aligner avant son adversaire 3 symboles identiques horizontalement, verticalement ou en diagonale.")

label5 = Label(root, image=test5, width=150, height=150, borderwidth=1, relief="solid")
label5.image = test5
label5.place(x=240, y=290)
tip5 = Balloon(root)
tip5.bind_widget(label5,balloonmsg="Plus de jeu à venir")

root.mainloop()
