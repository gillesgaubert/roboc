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
        #print(chaine)
        for i in range(len(chaine)):
            car=chaine[i]
            if car=="\n" :
                numLigne+=1
                numColonne=0
            else :
                cle=(numColonne,numLigne)
                self.grille[cle]=car
                #print(str(cle[0])+", "+str(cle[1])+" : "+self.grille.get(cle))
                #print(type(self.grille.get(cle)))
                if car=='X' :
                    self.robot['x']=cle[0]
                    self.robot['y']=cle[1]
                    #print("Le robot se trouve colonne="+str(cle[0])+" ligne="+str(cle[1]))
                numColonne+=1



    """ grille={(colonne,ligne):"elementDeDecor",...}
        robot={'x':valColonne,'y':valLigne}
    """

    def __repr__(self):
        sortie=""
        ligneExiste=True
        l=0
        c=0
        
        while ligneExiste:
            if not (c,l) in self.grille :
                #print(str((c,l))+" est non defini, ligne existe pas")
                ligneExiste=False
            else :
                colonneExiste=True
                while colonneExiste:
                    if not (c,l) in self.grille :
                        #print(str((c,l))+" est non defini, colonne existe pas")
                        sortie+="\n"
                        colonneExiste=False
                    else :
                        #print(str((c,l))+" est defini")
                        sortie+=self.grille[(c,l)]
                        c+=1
                c=0
                l+=1
        
        return sortie

    def deplacementRobot(self,commandeDeplacement):
        lDepl=0
        cDepl=0
        print("Dans la fct de deplacement")
        # ici je prends le premier caractere comme direction
        dirDeplacement=commandeDeplacement
        if dirDeplacement.lower()=='n' :
            lDepl-=1
        elif dirDeplacement.lower()=='s' :
            lDepl+=1
        elif dirDeplacement.lower()=='e' :
            cDepl+=1
        elif dirDeplacement.lower()=='o' :
            cDepl-=1
        else :
            print("t'est un couillon")
        # maintenant on deplace le robot sans controle pour commancer
        self.grille[(self.robot['x'],self.robot['y'])]=' '
        self.robot['x']+=cDepl
        self.robot['y']+=lDepl
        self.grille[(self.robot['x'],self.robot['y'])]='X'

