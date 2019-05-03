# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.
Exécutez-le avec Python pour lancer le jeu.
"""

import os
import pickle

from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichCarte:
            contenu = fichCarte.read()
            # Création d'une carte
            carte=Carte(nom_carte,contenu)
        cartes.append(carte)

# on a une sauvegarde ?
anciennePartieExiste=True
try:
    with open('sauvegarde', 'rb') as fichSav:
        mon_depickler = pickle.Unpickler(fichSav)
        carteSauv = mon_depickler.load()
        print(carteSauv)
except FileNotFoundError:
    print("Pas de fichier de sauvegarde de partie précédente.")
    anciennePartieExiste=False

# un menu pour choisir la carte
if anciennePartieExiste:
    print("0 : sauvegarde partie précédement commencée")
for i in range(len(cartes)):
    print("{} : {}".format(i+1,cartes[i].nom))

carteChoisie=False
while (not carteChoisie):
    print("Choisissez la carte :")
    choix=int(input())

    if (choix==0 and anciennePartieExiste):
        MaCarte=carteSauv
        carteChoisie=True
    elif choix<=len(cartes):
        MaCarte=cartes[choix-1]
        carteChoisie=True
    else:
        print("Carte inexistante !")

# debut de la partie
etat="EnCours";
print(MaCarte)

while (etat=="EnCours"):
    print("Donnez la direction :")
    direction=input()
    etat=MaCarte.labyrinthe.interpreteurCommande(direction)
    print(MaCarte)

    if etat=="Gagne":
        print("Tu est sorti vivant de ce labyrinthe... Bravo !")
        # si il s agissait d'une partie enregistree on
        # l efface car elle est finie
        if anciennePartieExiste:
            os.remove('sauvegarde')
    elif etat=="EnCours":
        print("T'est pas encore sorti, continue...")
    elif etat=="Erreur":
        print("Donne donc une commande valide pour changer !")
        etat="EnCours"
    else:
        # cas ou on veut quitter le jeu en sauvegardant
        print("Sauvegarde... et fin de partie !")
        with open('sauvegarde', 'wb') as fichSav:
            mon_pickler = pickle.Pickler(fichSav)
            mon_pickler.dump(MaCarte)

