from pathlib import Path
import configparser
import csv
from tkinter import messagebox
from tkinter import *

#Lecture du fichier de config
parser = configparser.ConfigParser()
parser.read("./Config.ini")
CouleurCercle = parser["Morpion"]["CouleurCercle"] = "0x12FF34"
CouleurCroix = parser["Morpion"]["CouleurCroix"] = "0x1216FF"

root = Tk()
root.title("Morpion")
root.resizable(width=False, height=False)
username = StringVar()                                    
dessin=Canvas(root, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)
cases=[ [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
drapeau = True                              # True pour les croix, False pour les ronds
tour = 1  

#Permet de dessiner la croix ou le cercle
def Dessiner(event) :
    global drapeau, cases, tour
    l = (event.y-2)//100                    # Ligne clic
    c = (event.x-2)//100                    # Colonne clic

    if tour < 10 and cases[l][c] == 0:
        if drapeau == True:                             
            dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = "#12FF34") 
            dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = "#12FF34")
            cases[l][c] = 1
            drapeau = False
            verif(cases)

        elif drapeau == False:
            dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = "#1216FF")
            cases[l][c] = -1 
            drapeau = True
            verif(cases)

        elif tour == 9:
            dessin.unbind("<Button-1>") #On unbind le bouton de la souris pour éviter que le joueur clique encore
            loseWindows("Egalité")
    tour += 1

    
    
    

#Vérification des possibilité de victoire
def verif(cases):
    result = [0,0,0,0,0,0,0,0]
    # Vérification des lignes :
    result[0] = cases[0][0] + cases[0][1] + cases[0][2]
    result[1] = cases[1][0] + cases[1][1] + cases[1][2]
    result[2] = cases[2][0] + cases[2][1] + cases[2][2]
    
    # Vérification des colonnes
    result[3] = cases[0][0]+cases[1][0]+cases[2][0]
    result[4] = cases[0][1]+cases[1][1]+cases[2][1]
    result[5] = cases[0][2]+cases[1][2]+cases[2][2]
    # Vérification des diagonales
    result[6] = cases[0][0]+cases[1][1]+cases[2][2]
    result[7] = cases[0][2]+cases[1][1]+cases[2][0]

    for i in range(8):    
       #On parcour le tableau des résultats
        if result[i] == 3:
            dessin.unbind("<Button-1>")
            loseWindows("Le gagnant est la croix : X")
        elif result[i] == -3:
            dessin.unbind("<Button-1>")
            loseWindows("Le gagnant est le cercle : O")

#Permet de fermer la fenêtre de fin de jeu si elle est toujours ouverte
def doesitexist():
    if loseWin.winfo_exists():
        loseWin.destroy()

#Permet de créer le fichier de sauvegarde s'il n'existe pas
def createFileIfNotExist():
    myfile = Path("./saves/highscoreSaveMorpion") #Variable
    myfile.touch(exist_ok=True)

#Permet de sauvegarder les informations 
def saveHighScore():
    createFileIfNotExist()
    tempList = []
    List2 = []
    #Permet d'éviter le champs vide
    if(len(username.get()) == 0):
        messagebox.showerror(title="Erreur nom d'utilisateur", message="Vous ne pouvez pas enregistrer un nom d'utilisateur vide")
    else:
        #On lit le fichier de sauvegarde
        with open('./saves/highscoreSaveMorpion', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')     
            for row in spamreader:    
                tempList.append(f"{row[0]};{row[1]}")
        open('./saves/highscoreSaveMorpion', 'w').close() #On clear le fichier pour réécrire les nouvelles informations
        for i in tempList:
            stringSplit = i.split(";")
            print(stringSplit)
            #Si le nom entré par l'utilisateur existe déjà, on incrémente son score de 1 et on l'ajoute dans une nouvelle liste
            if stringSplit[0] == username.get(): #Récup le highscore name
                #Conversion de string à int
                Entier = int(stringSplit[1])
                Entier += 1
                stringSplit[1] = Entier
                stringReformed = str(stringSplit[0])+";"+str(stringSplit[1])
                List2.append(stringReformed)
            else:
                List2.append(i)  

        List2.append(f"{username.get()};1")  
        f = open("./saves/highscoreSaveMorpion", "a") 
        for i in List2:
            f.write(f"{i}\n")  

        #Permet de disable le boutton de sauvegarde
        ButtonSave.config(state=DISABLED)

#Permet d'afficher la fenêtre de fin de jeu
def loseWindows(var):
    global loseWin
    loseWin = Toplevel(root)
    loseWin.resizable(width=False, height=False)
    loseWin.geometry("300x150")
    Button(loseWin, text="Rejouer", command= lambda: [init(), doesitexist()]).place(x=50, y=100) #BtnRestart
    Button(loseWin, text="Quitter", command= lambda: root.destroy()).place(x=200, y=100) #BtnExit

    global ButtonSave
    ButtonSave = Button(loseWin, text="Save", width= 6 ,command= lambda: saveHighScore())
    ButtonSave.place(x=200, y=60)

    Label(loseWin, text=f"Username : ").place(x=8, y= 60)
    Label(loseWin, text=var).pack()
    textBox = Entry(loseWin, textvariable=username, width=15)
    textBox.place(x=80,y=63)
    textBox.delete(0, END) #Permet de clear la textbox 
    
#Permet d'initialiser l'interface + de remettre à 0
def init():
    dessin.bind('<Button-1>', Dessiner) #Bind du clique gauche de la souris
    global drapeau, cases, tour
    cases = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    drapeau = True          # True = X , False = O
    tour = 1

    dessin.delete(ALL)      #Efface tout
    
    #Dessine la zone de dessin
    for i in range(4):
      dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3)
      dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3)


init()
root.mainloop()                      # Boucle d'attente des événements