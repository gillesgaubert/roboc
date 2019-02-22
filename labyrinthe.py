# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self,robot,grille):
        self.robot=robot
        self.grille=grille

    """ grille={(absisse,ordonnee):"elementDeDecor",...}
        robot=[abs,ordonnee]
    """

    def __repr__(self):
    	sortie=""
    	ligneExiste=True
    	l=0
    	c=0
    	while ligneExiste:
    		if self.grille[l,c]="" :
    			ligneExiste=False
    		else :
    			colonneExiste=True
    			while colonneExiste:
    				if self.grille[(l,c)]="" :
    					sortie+="\n"
    					colonneExiste=False
    				else :
    					sortie+=self.grille[(l,c)]
    					c+=1
    		l+=1
    	return sortie


