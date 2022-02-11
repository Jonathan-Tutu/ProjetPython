
#TODO
#COMMENTAIRE + VERIFIER LES NOMS DE VARIABLES + FINIR TOUT LE HIGHSCORE DU MORPION 
#CORRIGER L'EGALITER, FAIRE EN SORTE QU'UN FICHIER DE SAVE SE CREER S'IL N'EXISTE PAS 
#POUR EVITER LES BUGS

from pathlib import Path
import configparser
parser = configparser.ConfigParser()
import csv


parser.read("./Config.ini")
CouleurCercle = parser['Morpion']['CouleurCercle'] = "0x12FF34"
CouleurCroix = parser['Morpion']['CouleurCroix'] = "0x1216FF"


##-----Importation des Modules-----##
from tkinter import *


##----- Définition des Variables globales -----##
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
n = 1                                       # Numéro du tour de jeu


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
            print("x")
            #Set une variable
            loseWindows("Gagnant X")
            saveHighScore() #Remove only for test
        elif result[i] == -3:
            dessin.unbind("<Button-1>")
            print("y")
            #Set une variable
            loseWindows("Gagnant Y")
    if n == 9:
        dessin.unbind("<Button-1>")
        print("Egalité")
        loseWindows("Egalité")
        #Set une variable

def doesitexist():
    if loseWin.winfo_exists():
        loseWin.destroy()

def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveMorpion") #Variable
    myfile.touch(exist_ok=True)
    f = open(myfile)

def saveHighScore():

    createFileIfNotExist()
    if(len(userName == 0)): #A récup
        print("Erreur")
    else:
        tempList = []
        List2 = []
        with open('./saves/highscoreSaveMorpion', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')     
            for row in spamreader:    
                tempList.append(row)
        print(tempList)

        open('./saves/highscoreSaveMorpion', 'w').close() #Clear le file
        for i in tempList:
            if i[0] == "Jonathan": #Récup le highscore name

                test = int(i[1])
                test += 1
                i[1] = test 
                List2.append(i)
            else:
                List2.append("Else")
    

    f = open("./saves/highscoreSaveMorpion", "a") 
    for i in range(len(List2)):
        f.write(f"{List2[i][0]};{List2[i][1]}")  
    
def loseWindows(var):
    print("Vous avez perdu")
    #Afficher truc avec Tkinter
    global loseWin
    loseWin = Toplevel(fen)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: [init(), doesitexist()]).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: fen.destroy()).place(x=200, y=100) #BtnExit

    #Gérer le highscore
    global ButtonSave
    #ButtonSave = Button(loseWin, text="Highscore", command= lambda: saveHighScore())
    #ButtonSave.place(x=200, y=60) #BtnSaveHighScore

    #Label(loseWin, text="Vous avez perdu").pack()
    #Entry(loseWin, textvariable=username).place(x=50,y=60)
    #Label(loseWin, text=f"Votre score : {root.score}").pack()
    

def init():
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


##-----Création de la fenêtre-----##
fen = Tk()
fen.title('Morpion')
fen.resizable(width=False, height=False)

##-----Création du canvas-----##
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


##-----Evenements-----##
dessin.bind('<Button-1>', afficher)

##-----Programme principal-----##
init()
fen.mainloop()                      # Boucle d'attente des événements