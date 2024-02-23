import json
import module1 as module

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
joueur = module(nom)
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
        module.joueur["pointage"]+= i["pts"]
        reponse = True

    elif choix == 'q':
        print()
        print("Fin de la partie")
        print("Votre pointage est: ",   module.joueur["pointage"], "points")
        break
    else :
        print ("Mauvaise réponse. La bonne réponse est " , i["rep"])
        reponse=False
        
    module.joueur.listeReponses.append( {"question": i["q"],
                                  "reponse": choix,
                                  "bonne" :reponse})
    
    print()
    numeroQuestion +=1
  

    
resultat_dict = {
    "datePartie": str(module.joueur.datePartie),
    "nom": module.joueur.nomJoueur,
    "listeReponses": module.joueur.listeReponses,
    "pointage": module.joueur.pointage
}