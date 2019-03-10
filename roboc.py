# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte
            carte=Carte(nom_carte,contenu)
        
        cartes.append(carte)

print("sur la carte facile : 1")
cacarte=cartes[1]
fini=False

while (not fini):
    print("Donnez la direction :")
    read(direction)
    fini=cacarte.labyrinthe.interpreteurCommande(direction)
    print(cacarte)

    if fini :
        print("Tu est sorti vivant de ce labyrinthe... Bravo !")
    else :
        print("T'est pas encore sorti, continue...")





"""
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
"""
