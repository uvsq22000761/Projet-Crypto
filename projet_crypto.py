# TEXTE 1
# Cette fonction est celle utilisé en TD, elle permet de chiffrer et dechiffrer les lettres du message avec une clé(une lettre)
import tkinter as tk

def rang(lettre):
    return ord(lettre) - 97


def decalage(lettre1, lettre2):
    if ord(lettre1) < 97 or ord(lettre1) > 122:
        return lettre1
    return chr(((rang(lettre1) + rang(lettre2)) % 26) + 97)


def dec_texte(texte, cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        res += decalage(texte[i], cle[i % taille_cle])
    return res


def dechiffre():
    resultat.delete(0, tk.END)
    text = entree_texte.get()
    cle = entree_cle.get()
    if (len(text) > 0) and (len(cle) > 0):
        res = dec_texte(text, cle)
        resultat.insert(0, res)
    else:
        resultat.insert(0, "Il manque quelque chose")


racine = tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width=50, font=("helvetica", "20"))
entree_texte.grid(row=0, column=0)

entree_cle = tk.Entry(racine, width=50, font=("helvetica", "20"))
entree_cle.grid(row=1, column=0)

label_texte = tk.Label(racine, font=("helvetica", "20"), text="Entrer le message ici.")
label_texte.grid(row=0, column=1)

label_cle = tk.Label(racine, font=("helvetica", "20"), text="Entrer la clé ici.")
label_cle.grid(row=1, column=1)

label_dech = tk.Label(racine, font=("helvetica", "28"), text="Déchiffre ici")
label_dech.grid(row=3, column=1)

bouton_coder = tk.Button(racine, text="Déchiffrer texte", fg="black", width=15, command=dechiffre)
bouton_coder.grid(row=2, column=0)

resultat = tk.Entry(racine, width=50, font=("helvetica", "20"))
resultat.grid(row=3, column=0)

racine.mainloop()