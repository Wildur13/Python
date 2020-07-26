import json
import os

dossier = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier, "kaufliste.json")

if os.path.exists(chemin_liste):
    with open (chemin_liste, "r") as f:
        kaufliste = json.load(f)
else:
    kaufliste = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""

print(affichage)
a = input("Veuillez choisir une action à effectuer: ")
while not (a.isdigit()) :
                print(affichage)
                a = input("Veuillez entrer une valeur correcte: ")
while(int(a)<=4):
    if int(a) == 1:
        elem = input("Entrez le nom de l'element à ajouter: ")
        kaufliste.append(elem)
    elif int(a) == 2:
        element = input("Entrez le nom de l'element à retirer: ")
        if element in kaufliste:
             kaufliste.remove(element)
        else:
             element = input("L'élément que vous voulez enlever n'existe pas dans votre liste.\nVeuillez entrer le nom d'un elelment correct: ")
    elif int(a) == 3:
        if(len(kaufliste) != 0):
            i = 0
            while (i<len(kaufliste)):
                print(kaufliste[i])
                i += 1
        else:
            print("Votre liste est vide!")
    else:
        kaufliste.clear()
    print(affichage)
    a = (input(""))

print("Au revoir.")

with open (chemin_liste, "w") as f:
    json.dump(kaufliste, f, indent=4)