# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = chaineVersLabyrinthe(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)+"\n"+__repr__(self.labyrinthe)

    """ methode qui transforme une chaine issue d'un fichier en labyrinthe """
    def chaineVersLabyrinthe(chaine):
        grille={}
        index=0
        numLigne=0
        numColonne=0
        
        for car in chaine:
        	if car="\n" :
        		numLigne+=1
        		numColonne=0
        	else :
        		cle=(numColonne,numLigne)
        		grille[cle]=car
        		if car=='X' :
        			robot['x']=cle[0]
        			robot['y']=cle[1]

        lab=new Labyrinthe(robot,grille)
        return lab

