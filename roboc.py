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
            #print(nom_carte)
            #print(contenu)
            # Création d'une carte, à compléter
            carte=Carte(nom_carte,contenu)
            #print(carte)
            #print(carte.nom)
            #print(carte.labyrinthe)
        
        cartes.append(carte)

print("sur la carte facile : 1")
print("Maintenant je veux deplacer le robot vers le sud")
direction='s'
cacarte=cartes[1]
print(cacarte)
lab=cacarte.labyrinthe
lab.deplacementRobot(direction)
print(cacarte)




"""
# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
"""
