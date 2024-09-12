import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class DataVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application de Visualisation de Données IoT")
        self.geometry("1200x700")  # Augmenter la taille pour plus d'espace

        # Ajout d'un titre en haut de l'interface
        self.header_label = tk.Label(self, text="Application de Visualisation de Données pour la Surveillance des Nœuds et Protocoles IoT", font=("Arial", 16, "bold"))
        self.header_label.pack(pady=10)

        # Chargement et redimensionnement du logo
        self.logo_image = Image.open("C:/Users/SAMAR/Desktop/Logo_IMT_Nord_Europe.png")  # Remplacez ce chemin par le chemin vers votre logo
        self.logo_image = self.logo_image.resize((150, 150))  # Redimensionner l'image
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        
        # Création des widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame pour le logo
        logo_frame = tk.Frame(self, padx=10, pady=10)
        logo_frame.pack(side=tk.LEFT, anchor='nw', fill=tk.Y)

        # Affichage du logo dans le logo_frame
        self.logo_label = tk.Label(logo_frame, image=self.logo_photo)
        self.logo_label.pack()

        # Frame pour les options
        options_frame = tk.Frame(self, padx=10, pady=10)
        options_frame.pack(side=tk.LEFT, anchor='nw', fill=tk.Y)

        # Liste des nœuds
        self.node_label = tk.Label(options_frame, text="Choisissez un ou plusieurs nœuds:")
        self.node_label.pack(pady=5)

        self.node_listbox = tk.Listbox(options_frame, height=15, width=30, selectmode=tk.MULTIPLE)  # Ajuster la taille pour plus de clarté
        nodes = ["Node 1", "Node 2", "Node 3", "Node 4", "Node 5", "Node 6", "Node 7", "Node 8", "Node 9", "Node 10"]
        for node in nodes:
            self.node_listbox.insert(tk.END, node)
        self.node_listbox.pack(pady=5)

        # Liste des protocoles
        self.protocol_label = tk.Label(options_frame, text="Choisissez un ou plusieurs protocoles:")
        self.protocol_label.pack(pady=5)

        self.protocol_listbox = tk.Listbox(options_frame, height=15, width=30, selectmode=tk.MULTIPLE)  # Ajuster la taille pour plus de clarté
        protocols = ["Protocol LoRa", "Protocol BLE", "Protocol WIFI"]
        for protocol in protocols:
            self.protocol_listbox.insert(tk.END, protocol)
        self.protocol_listbox.pack(pady=5)

        # Filtrage des données
        self.filter_button = tk.Button(options_frame, text="Filtrer", command=self.filter_data)
        self.filter_button.pack(pady=10)

        # Zone de visualisation des graphiques
        graph_frame = tk.Frame(self)
        graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.figure, self.ax = plt.subplots(2, 1, figsize=(10, 8))
        self.figure.tight_layout(pad=3.0)
        self.canvas = FigureCanvasTkAgg(self.figure, graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def filter_data(self):
        # Récupérer les sélections multiples
        selected_nodes = [self.node_listbox.get(i) for i in self.node_listbox.curselection()]
        selected_protocols = [self.protocol_listbox.get(i) for i in self.protocol_listbox.curselection()]

        # Afficher les sélections dans la console
        print(f"Nodes selected: {selected_nodes}")
        print(f"Protocols selected: {selected_protocols}")

        # Simulation de données en fonction des sélections
        time = np.linspace(0, 10, 100)
        
        # Réinitialiser les graphiques
        self.ax[0].cla()
        self.ax[1].cla()
        
        # Ajouter des graphiques pour chaque nœud sélectionné
        for node in selected_nodes:
            temperature = 20 + 5 * np.sin(time)  # Simuler des données de température
            position = np.cumsum(np.random.randn(100))  # Simuler des données de position

            self.ax[0].plot(time, temperature, label=f"{node} Temperature")
            self.ax[1].plot(time, position, label=f"{node} Position")

        # Ajouter des légendes et des titres
        self.ax[0].set_title("Temperature Over Time")
        self.ax[0].set_xlabel("Time")
        self.ax[0].set_ylabel("Temperature (°C)")
        self.ax[0].legend()

        self.ax[1].set_title("Position Over Time")
        self.ax[1].set_xlabel("Time")
        self.ax[1].set_ylabel("Position")
        self.ax[1].legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = DataVisualizer()
    app.mainloop()
