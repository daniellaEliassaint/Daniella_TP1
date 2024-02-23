import datetime

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
        


















