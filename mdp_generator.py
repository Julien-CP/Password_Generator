import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

import pyperclip

print("=== Générateur de mot de passe ===")

# Longueur du mot de passe
while True:
    try:
        longueur = int(input("Longueur du mot de passe (min. 8) : "))
        if longueur < 8:
            print("Le mot de passe doit contenir au minimum 8 caractères.")
        else:
            break  # OK, on sort de la boucle
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

def demande_oui_non(question):
    while True:
        reponse = input(question + " (y/n) : ").strip().lower()
        if reponse in ['y', 'n']:
            return reponse == 'y'
        print("Réponse invalide. Veuillez répondre par 'y' ou 'n'.")

utiliser_majuscules = demande_oui_non("Inclure des MAJUSCULES ?")
utiliser_minuscules = demande_oui_non("Inclure des minuscules ?")
utiliser_chiffres   = demande_oui_non("Inclure des chiffres ?")
utiliser_symboles   = demande_oui_non("Inclure des symboles ?")

# Ensemble de caractères autorisés
caracteres = ''
caracteres_obligatoires = []

if utiliser_majuscules:
    caracteres += string.ascii_uppercase
    caracteres_obligatoires.append(random.choice(string.ascii_uppercase))
if utiliser_minuscules:
    caracteres += string.ascii_lowercase
    caracteres_obligatoires.append(random.choice(string.ascii_lowercase))
if utiliser_chiffres:
    caracteres += string.digits
    caracteres_obligatoires.append(random.choice(string.digits))
if utiliser_symboles:
    caracteres += string.punctuation
    caracteres_obligatoires.append(random.choice(string.punctuation))

# Vérification
if not caracteres:
    print("Erreur : Aucun type de caractère sélectionné !")
    exit()

# Calcul du reste à générer
reste = longueur - len(caracteres_obligatoires)
if reste < 0:
    print(f"Erreur : Longueur insuffisante pour inclure tous les types demandés. Min = {len(caracteres_obligatoires)}")
    exit()


# Génération aléatoire du reste du mot de passe
mdp = caracteres_obligatoires + [random.choice(caracteres) for _ in range(reste)]
# Mélange pour éviter que les caractères obligatoires soient toujours au début
random.shuffle(mdp)  

mot_de_passe = ''.join(mdp)
print("\nMot de passe généré :", mot_de_passe)

def evaluer_mdp(mdp):
    score = 0
    remarques = []
    
    if len(mdp) >= 12:
        score += 1
    else:
        remarques.append("🔸 Utilisez au moins 12 caractères.")

    if any(c.islower() for c in mdp):
        score += 1
    else:
        remarques.append("🔸 Ajoutez des lettres minuscules.")

    if any(c.isupper() for c in mdp):
        score += 1
    else:
        remarques.append("🔸 Ajoutez des lettres MAJUSCULES.")

    if any(c.isdigit() for c in mdp):
        score += 1
    else:
        remarques.append("🔸 Ajoutez des chiffres.")

    if any(c in string.punctuation for c in mdp):
        score += 1
    else:
        remarques.append("🔸 Ajoutez des symboles (!, @, #, etc).")

    if score <= 2:
        niveau = "Mot de passe faible"
    elif score == 3:
        niveau = "Mot de passe moyen "
    elif score == 4:
        niveau = "Mot de passe fort"
    else:
        niveau = "Mot de passe très fort"

    return niveau, remarques

def analyser_depuis_interface():
    mot_de_passe = entry.get()
    niveau, remarques = evaluer_mdp(mot_de_passe)

    result_label.config(text=f"Niveau de sécurité : {niveau}")

    if remarques:
        conseils_text = "\n".join(remarques)
    else:
        conseils_text = "Aucun conseil : excellent mot de passe !"

    conseils_label.config(text=conseils_text)


def copie_mdp(question):
    while True:
        reponse = input(question + " (y/n) : ").strip().lower()
        if reponse == 'y':
            pyperclip.copy(mot_de_passe)
            print("\nMot de passe copié dans le presse-papiers !\n")
            return True
        elif reponse == 'n':
            print("\nMot de passe non copié.\n")
            return False
        else:
            print("Réponse invalide. Veuillez répondre par 'y' ou 'n'.")

copie_mdp("Voulez-vous copier le mot de passe dans le presse-papiers ? : ")

# === Interface graphique ===
root = tk.Tk()
root.title("Analyseur de mot de passe")
root.geometry("400x300")

title = tk.Label(root, text="Analyseur de mot de passe", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
entry.pack(pady=10)

btn = tk.Button(root, text="Analyser", command=analyser_depuis_interface, font=("Helvetica", 12))
btn.pack(pady=5)


result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), fg="blue")
result_label.pack(pady=5)

texte_info = tk.Label(root, text="Amélioration(s) suggérée(s)", font=("Helvetica", 11))
texte_info.pack()

conseils_label = tk.Label(root, text="", font=("Helvetica", 10), wraplength=350, justify="left")
conseils_label.pack(pady=10)

root.mainloop()