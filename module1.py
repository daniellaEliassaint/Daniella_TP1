import datetime
import json 

#création de la classe/objet Joueur 
class Joueur :
    
    #constructeur
    def __init__(self, p_nomJoueur ):
       self.datePartie =  datetime.datetime.now()
       self.nomJoueur = p_nomJoueur
       self.listeReponses = {}
       self.pointage = 0
       
    #methode pour afficher les données
    def afficherPartie(self):
        print("Date: " +str(self.datePartie) + ",Nom: " + self.nomJoueur +
              ",listeReponses: " + str(self.listeReponses) +
              "Pointage: " + str(self.pointage))
        
with open('questions.json', 'r') as fic:
    questions = json.load(fic)
        
#Affichage ddes règles du jeu
print("|-------------------------------------------------------------|")
print("|   Travail pratique 1 - Quiz 4B5 - Daniella Eliassaint       |")
print("|-------------------------------------------------------------|")
print("|  Choississez la bonne réponse pour chaque question (a/b/c)  |")
print("|  q pour quitter                                             |")
print("|-------------------------------------------------------------|")

nom = input("Entrez votre nom: ")
joueur = Joueur(nom)

numeroQuestion =1

for i in questions:
    print(numeroQuestion,":",i["q"])
    print("a.",i["a"])
    print("b.",i["b"])
    print("c.",i["c"])
    
    choix = input("Réponse (a/b/c/q): ")


    numeroQuestion  += 1
















