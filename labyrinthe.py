# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self,chaine):
        """ on definit ici grille et robot les attreibut de la classe """
        self.grille={}
        self.robot={}
        
        index=0
        numLigne=0
        numColonne=0
        print(chaine)
        for i in range(len(chaine)-1):
        	car=chaine[i]
        	if car=="\n" :
        		numLigne+=1
        		numColonne=0
        	else :
        		cle=(numColonne,numLigne)
        		self.grille[cle]=car
        		print(str(cle[0])+", "+str(cle[1])+" : "+self.grille.get(cle))
        		if car=='X' :
        			self.robot['x']=cle[0]
        			self.robot['y']=cle[1]
        		numColonne+=1



    """ grille={(absisse,ordonnee):"elementDeDecor",...}
        robot=[abs,ordonnee]
    """

    def __repr__(self):
    	sortie=""
    	ligneExiste=True
    	l=0
    	c=0
    	
    	

    	"""
    	while ligneExiste:
    		if self.grille.get(l,c) is None :
    			ligneExiste=False
    		else :
    			colonneExiste=True
    			while colonneExiste:
    				if self.grille.get(l,c) is None :
    					sortie+="\n"
    					colonneExiste=False
    				else :
    					sortie+=str(self.grille.get(l,c))
    					c+=1
    		l+=1
    	"""
    	print(self.grille.get((1,1)))
    	print(self.grille.get((1,2)))
    	print(self.grille.get((1,3)))

    	#sortie=self.grille.get(1,0)+self.grille.get(1,1)+self.grille.get(1,2)+self.grille.get(1,3)

    	return sortie


