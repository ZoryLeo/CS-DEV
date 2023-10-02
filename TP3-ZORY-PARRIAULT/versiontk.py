from tkinter import Tk, Label, PhotoImage,Canvas
import tkinter as tk 
mainw = Tk()
labelPendu = Label(mainw, text = "bienvenu dans ce pendu" )
mainw.title("Choisir un mainw")

# Ajout d'un grand titre en rouge brillant à l'interface
titre_label = tk.Label(mainw, text="Choix du mainw", font=("impact", 40), fg="white", bg="black")
titre_label.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)

# Création de l'image pour le bouton
quitter = tk.PhotoImage(file=".\TP3-ZORY-PARRIAULT\quitter.png")
Canevas = Canvas(mainw,width=500,height=500)
item = Canevas.create_image(0,0,image=quitter)

# Création du bouton
button = tk.Button(mainw, image=quitter, command=mainw.destroy,highlightthickness=0)
button.place(relx=1.0, rely=1.0, anchor=tk.SE)

mainw.attributes('-fullscreen', True)
mainw.mainloop()