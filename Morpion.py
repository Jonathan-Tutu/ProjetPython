
#TODO
#COMMENTAIRE + VERIFIER LES NOMS DE VARIABLES + FINIR HIGHSCORE MORPION

from pathlib import Path
import configparser
import csv
from tkinter import messagebox
##-----Importation des Modules-----##
from tkinter import *
from typing import List

parser = configparser.ConfigParser()
parser.read("./Config.ini")
CouleurCercle = parser['Morpion']['CouleurCercle'] = "0x12FF34"
CouleurCroix = parser['Morpion']['CouleurCroix'] = "0x1216FF"

##-----Création de la rootêtre-----##
root = Tk()
root.title('Morpion')
root.resizable(width=False, height=False)
username = StringVar()                                    

##-----Création du canvas-----##
dessin=Canvas(root, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

##----- Définition des Variables globales -----##
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
n = 1  


##----- Définition des Fonctions -----##
def afficher(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    global drapeau, cases, n
    l = (event.y-2)//100                    # Ligne du clic@‘ë“
    c = (event.x-2)//100                    # Colonne du clic

    if (n < 10) and (cases[l][c] == 0):
        if drapeau == True:                              # drapeau == True
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = "#12FF34") #Permettre le choix de la couleur dans le fichier de configuration
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = "#12FF34")
            cases[l][c] = 1
            drapeau = False
            verif(cases)

        else:
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = "#1216FF")
            cases[l][c] = -1
            drapeau = True
            #verification de la condidition de victoire
            verif(cases)
        n += 1


def verif(cases):

    result = [0,0,0,0,0,0,0,0]
    # Les lignes :
    result[0] = cases[0][0] + cases[0][1] + cases[0][2]
    result[1] = cases[1][0] + cases[1][1] + cases[1][2]
    result[2] = cases[2][0] + cases[2][1] + cases[2][2]
    
    # Les colonnes
    result[3] = cases[0][0]+cases[1][0]+cases[2][0]
    result[4] = cases[0][1]+cases[1][1]+cases[2][1]
    result[5] = cases[0][2]+cases[1][2]+cases[2][2]
    # Les diagonales
    result[6] = cases[0][0]+cases[1][1]+cases[2][2]
    result[7] = cases[0][2]+cases[1][1]+cases[2][0]

    for i in range(8):    
       # Parcours des sommes
        if result[i] == 3:
            dessin.unbind("<Button-1>")
            loseWindows("Le gagnant est la croix : X")
        elif result[i] == -3:
            dessin.unbind("<Button-1>")
            loseWindows("Le gagnant est le cercle : O")

    if n == 9: #A corriger
        dessin.unbind("<Button-1>")
        loseWindows("Egalité")

def doesitexist():
    if loseWin.winfo_exists():
        loseWin.destroy()

def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveMorpion") #Variable
    myfile.touch(exist_ok=True)

def saveHighScore():
    createFileIfNotExist()
    tempList = []
    List2 = []
    if(len(username.get()) == 0):
        messagebox.showerror(title="Erreur nom d'utilisateur", message="Vous ne pouvez pas enregistrer un nom d'utilisateur vide")
    else:
        with open('./saves/highscoreSaveMorpion', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')     
            for row in spamreader:    
                tempList.append(f"{row[0]};{row[1]}")
            tempList.append(f"{username.get()};1") 
            print(tempList)

        open('./saves/highscoreSaveMorpion', 'w').close() #Clear le file
        for i in tempList:
            a = i.split(";")
            if a[0] == username.get(): #Récup le highscore name
                test = int(a[1])
                test += 1
                a[1] = test 
                z = str(a[0])+";"+str(a[1])
                List2.append(z)
            else:
                List2.append(i)
        if len(tempList) == 0: #Permet de gérer si le fichier est vide
                List2.append(f"{username.get()};1")

        print(List2)
        f = open("./saves/highscoreSaveMorpion", "a") 
        for i in List2:
            f.write(i)  

        ButtonSave.config(state=DISABLED)

def loseWindows(var):
    #Afficher truc avec Tkinter
    global loseWin
    loseWin = Toplevel(root)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: [init(), doesitexist()]).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

    #Gérer le highscore
    global ButtonSave
    ButtonSave = Button(loseWin, text="Save", width= 6 ,command= lambda: saveHighScore(), )
    ButtonSave.place(x=200, y=60) #BtnSaveHighScore

    Label(loseWin, text=f"Username : ").place(x=8, y= 60)
    Label(loseWin, text=var).pack()
    y = Entry(loseWin, textvariable=username, width=12)
    y.place(x=80,y=57)
    y.delete(0, END)
    
def init():
    dessin.bind('<Button-1>', afficher)
    """Cette fonction ré-initialise les variables globales."""
    global drapeau, cases, n
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    drapeau = True          # True pour les croix, False pour les ronds
    n = 1

    dessin.delete(ALL)      # Efface toutes les figures
    #Redessine la zone de dessin
    for i in range(4):
      dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3)
      dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3)


##-----Programme principal-----##
init()
root.mainloop()                      # Boucle d'attente des événements