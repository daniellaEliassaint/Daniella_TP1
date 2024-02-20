import datetime
import json 

#création de la classe/objet Joueur 
class Joueur :
    
    #constructeur
    def __init__(self, p_nomJoueur ):
       self.datePartie =  datetime.datetime.now()
       self.nomJoueur = p_nomJoueur
       self.listeReponses = []
       self.pointage = 0
       
    #methode pour afficher les données
    def afficherPartie(self):
        print("Date: " +str(self.datePartie) + ",Nom: " + self.nomJoueur +
              ",listeReponses: " + str(self.listeReponses) +
              "Pointage: " + str(self.pointage))
        
with open('questions.json', 'r',encoding="utf-8") as fic:
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
#afficher les questions
for i in questions:
    print(numeroQuestion,")",i["q"])
    print("<a>",i["a"])
    print("<b>",i["b"])
    print("<c>",i["c"])
    
    choix = input("Entrez l'option (a/b/c) ou q pour quitter: ").lower()
    
    if choix == i["rep"]:
        print ("Bonne réponse!")
        joueur.pointage += i["pts"]
        reponse = True

    elif choix == 'q':
        break
    else :
        print ("Mauvaise réponse. La bonne réponse est " , i["rep"])
        reponse=False
        
    joueur.listeReponses.append( {"question": i["q"],
                                  "reponse": choix,
                                  "bonne" :reponse})
    
    print()
    numeroQuestion +=1
  
joueur.afficherPartie()
    
resultat_dict = {
    "nom": joueur.nomJoueur,
    "datePartie": str(joueur.datePartie),
    "listeReponses": joueur.listeReponses,
    "pointage": joueur.pointage
}

# écriture du dictionnaire dans un fichier 
with open ("resultat.json", "w", encoding="utf-8") as fic_json:
    json.dump(resultat_dict,
              fic_json,
              ensure_ascii=False,
              indent = 4,
              sort_keys=False)

















