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
        
        self.resultats = []
        
        #importer le fichier resultat
        self.frm_bouton = tk.Frame()
        self.frm_bouton.pack(side= tk.TOP)
        
        self.btn_afficher = tk.Button(self.frm_bouton, text="Importer le fichier")
        self.btn_afficher["command"] = self.btn_importer_clicked
        self.btn_afficher.pack()
        
        #label pour la date
        self.date_label = tk.Label(self, text="Sélectionnez la date de la partie:")
        self.date_label.pack()
        
        self.date_combobox = ttk.Combobox( width=30)
        self.date_combobox.pack()
        
        #label pour le nom du joueur
        self.joueur_label = tk.Label(self, text="Sélectionnez le nom du joueur:")
        self.joueur_label.pack()
        
         #ajout comboBox : utiliser le module ttk de tkinker
      
        self.joueur_combo = ttk.Combobox(width=30)
        self.joueur_combo.pack()
        
        #label pour les reponses du joueur
        self.reponse_label = tk.Label(self, text="Résultat du joueur:")
        self.reponse_label.pack()
        
        
        #champ texte
        self.champ_text = tk.Text(self, height=10, width=60)
        self.champ_text.pack()
        
        
        #label du nbr de points total du joueur
        self.score_label = tk.Label(self, text="",font= ("Helvetica", 12))
        self.score_label.pack()

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
            self.date_combobox['values'] = [resulat["datePartie"] for resulat in self.resultats]          
            self.date_combobox.bind("<<ComboboxSelected>>", self.joueur)
        else:
            print("Erreur")
 
 #Selectionner un joueur
    def joueur(self, event):
        date_select = self.date_combobox.get()
        fichier_select = next((resultat for resultat in self.resultats if resultat["datePartie" ] == date_select), None)
        
        if fichier_select:
            self.joueur_combo['values'] = [fichier_select.get("nom", "")]
            self.joueur_combo.set(fichier_select.get("nom",""))
            self.joueur_combo.bind("<<ComboboxSelected>>", lambda event, date= fichier_select:self.afficherReponse(event, date))
 
 # selectionner le pointage et le resultat
    def afficherReponse(self, event, fichier_select):
        self.champ_text.delete(1.0, tk.END)
        select_resultat = fichier_select
        
        for reponse in select_resultat.get("listeReponses", ()):
            question = "{} Réponse: {}".format(reponse.get('question', ''), reponse.get('reponse', '')) 
            correct = reponse.get("bonne", False)
            
            couleur = "green" if correct else "red"
            self.champ_text.insert(tk.END, question, couleur)
            
            debut = self.champ_text.index(tk.END) + "-2c"
            fin = self.champ_text.index(tk.END)
            self.champ_text.tag_add(couleur,debut, fin)
            
            self.champ_text.tag_config(couleur, foreground=couleur) 
            
        self.score_label.config(text="Pointage: {}".format(select_resultat.get('pointage', 0)))
            
    #programme principal
if __name__ =="__main__":
    app = fenetre() # création de l'objet fenetre
    app.mainloop()        #affichage de la fenetre