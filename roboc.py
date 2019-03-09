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

direction='s'
cacarte=cartes[1]
print(cacarte)

print("Maintenant je veux deplacer le robot vers le sud")
cacarte.labyrinthe.deplacementRobot(direction)
print(cacarte)

print("Maintenant je veux deplacer le robot vers l'ouest ce qui est pas possible")
direction='o'
cacarte.labyrinthe.deplacementRobot(direction)
print(cacarte)

print("Maintenant encore vers le sud")
direction='s'
cacarte.labyrinthe.deplacementRobot(direction)
print(cacarte)

print("Maintenant je veux gagner donc est...")
direction='e'
victoire=cacarte.labyrinthe.deplacementRobot(direction)
print(cacarte)
if victoire :
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
