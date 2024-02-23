#Jeu de questionnaire en mode grphique
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import json

class fenetre(tk.Tk):
    #constructeur
    def __init__(self):
        super().__init__()
        
        #configuration de notre fenetre
        self.title("Jeu de Questionnnaire")
        self.geometry("500x300")
        
        #importer le fichier resultat
        self.frm_bouton = tk.Frame()
        self.frm_bouton.pack(side= tk.BOTTOM)
        
        self.btn_afficher = tk.Button(self.frm_bouton, text="Importer le fichier")
        self.btn_afficher["command"] = self.btn_importer_clicked
        self.btn_afficher.pack()
        
       #cadre haut
        self.frm_haut = tk.Frame()
        self.frm_haut.pack(side=tk.TOP) 
        
         #ajout comboBox : utiliser le module ttk de tkinker
        self.combo_ville = ttk.Combobox(self.frm_haut, width=30)
        self.combo_ville["values"] = ("Laval", "Trois-Riviere" , "Québec", "Montreal", "Longueil")
        self.combo_ville["state"] = "readonly"
        self.combo_ville.pack()

 #importer un fichier Json       
    def btn_importer_clicked(self):
        importer = filedialog.askopenfilename(title="Sélectionner un fichier",
                                              filetypes=[("Fichiers Json", "*.json")])
        if importer:
            try:
                with open(importer, 'r', encoding="utf-8") as fic:
                    resultat=json.load(fic)
                    self.afficher =resultat.get("resultat", [])
                    self.afficherDate(resultat)
            except:
                print("N'a pas pu ouvert le fichier")
#Selectionner la date
    def afficherDate(self, date):
        if "resultat" in date:
            self.resultats = date["resultat"]
            self.date_cb['values'] = [resulat["datePartie"] for resulat in self.resultats]          
            self.date_cb.bind("<<ComboboxSelected>>", self.joueur)
 
 #Selectionner un joueur
    def joueur(self, event):
        date_select = self.date_cb.get()
        fichier_select = next((resultat for resultat in self.resultats))
        
 
 
            
    #programme principal
if __name__ =="__main__":
    app = fenetre() # création de l'objet fenetre
    app.mainloop()        #affichage de la fenetre