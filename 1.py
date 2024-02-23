import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json

class ResultatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Affichage des Résultats")
        self.root.geometry("600x400")

        self.resultats = []
        self.setup_gui()

    def setup_gui(self):
        self.import_button = tk.Button(self.root, text="Importer les résultats", command=self.import_results)
        self.import_button.pack(pady=20)

        self.date_label = tk.Label(self.root, text="Sélectionnez la date de la partie:")
        self.date_label.pack()

        self.date_combobox = ttk.Combobox(self.root, state="readonly")
        self.date_combobox.pack()

        self.player_label = tk.Label(self.root, text="Nom du joueur:")
        self.player_label.pack()

        self.player_combobox = ttk.Combobox(self.root, state="readonly")
        self.player_combobox.pack()

        self.response_label = tk.Label(self.root, text="Réponses du joueur:")
        self.response_label.pack()

        self.response_text = tk.Text(self.root, height=10, width=40)
        self.response_text.pack()

        self.score_label = tk.Label(self.root, text="Pointage du joueur:", font=("Helvetica", 12))
        self.score_label.pack()

        self.score_value_label = tk.Label(self.root, text="", font=("Helvetica", 14), fg="blue")
        self.score_value_label.pack()

    def import_results(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if file_path:
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    data = json.load(file)
                    self.resultats = data.get("resultat", [])
                    self.display_results(data)
            except Exception as e:
                print(f"Erreur lors de l'importation du fichier : {e}")

    def display_results(self, data):
        if "resultat" in data:
            self.resultats = data["resultat"]
            self.date_combobox['values'] = [result["datePartie"] for result in self.resultats]
            self.date_combobox.bind("<<ComboboxSelected>>", self.show_players)
        else:
            print("Erreur: Clé 'resultat' non trouvée dans le fichier JSON.")

    def show_players(self, event):
        selected_date = self.date_combobox.get()
        selected_result = next((result for result in self.resultats if result["datePartie"] == selected_date), None)

        if selected_result:
            print(f"Nom du joueur (show_players): {selected_result.get('nom', 'N/A')}")
            self.player_combobox['values'] = [selected_result.get("nom", "")]
            self.player_combobox.set(selected_result.get("nom", ""))
            self.player_combobox.bind("<<ComboboxSelected>>", lambda event, data=selected_result: self.show_selected_player(event, data))

    def show_selected_player(self, event, selected_result):
        self.response_text.delete(1.0, tk.END)  # Efface le contenu précédent

        selected_player_result = selected_result

        for response in selected_player_result.get("listeReponses", []):
            question_text = f"{response.get('question', '')}\nRéponse: {response.get('reponse', '')}\n"
            is_correct = response.get("bonne", False)

            # Ajout de la réponse avec la couleur appropriée
            color_tag = "green" if is_correct else "red"
            self.response_text.insert(tk.END, question_text, color_tag)

            # Applique la couleur à la réponse
            start_index = self.response_text.index(tk.END) + "-2c"
            end_index = self.response_text.index(tk.END)
            self.response_text.tag_add(color_tag, start_index, end_index)

            # Applique la couleur au texte ajouté
            self.response_text.tag_config(color_tag, foreground=color_tag)

        self.score_value_label.config(text=f"Pointage: {selected_player_result.get('pointage', 0)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResultatApplication(root)
    root.mainloop()