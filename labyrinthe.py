# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self,chaine):
        """ on definit ici grille et robot les attributs de la classe """
        
        self.grille={}
        self.robot={}
        self.surPorte=False
        
        index=0
        numLigne=0
        numColonne=0
        
        for i in range(len(chaine)):
            car=chaine[i]
            if car=="\n" :
                numLigne+=1
                numColonne=0
            else :
                cle=(numColonne,numLigne)
                self.grille[cle]=car
                
                if car=='X' :
                    self.robot['x']=cle[0]
                    self.robot['y']=cle[1]
                    
                numColonne+=1



    """ grille={(colonne,ligne):"elementDeDecor",...}
        robot={'x':valColonne,'y':valLigne}
    """

    def __repr__(self):
        sortie=""
        ligneExiste=True
        l=0
        c=0
        # Parcour du dictionnaire...
        while ligneExiste:
            if not (c,l) in self.grille :
                ligneExiste=False
            else :
                colonneExiste=True
                while colonneExiste:
                    if not (c,l) in self.grille :
                        sortie+="\n"
                        colonneExiste=False
                    else :
                        sortie+=self.grille[(c,l)]
                        c+=1
                c=0
                l+=1
        return sortie

    
    def interpreteurCommande(self,commande):
        victoire=False
        if len(commande)==0:
            print("Il faut rentrer une commande !")
        elif (commande.lower()=='w') :
            # ici sauvegearde et fin du programme
            print("Sauvegarde de la partie courante")
        else :
            if (len(commande)>1) :
                # ici une mini-gestion des erreurs :
                # commande doit etre au format "o 3" pour 3* ouest
                if ((commande[1]==' ') and (commande[2] in '123456789')) :
                    direction=commande[0]
                    nombreDeplacement=int(commande[2])
                else :
                    print("Je ne comprends pas cette commande !")
            else :
                direction=commande

            # finalement on peut deplacer le robot
            victoire=self.deplacementRobot(direction)
        return victoire


    def deplacementRobot(self,dirDeplacement):
        lDepl=0
        cDepl=0
        
        if dirDeplacement.lower()=='n' :
            lDepl-=1
        elif dirDeplacement.lower()=='s' :
            lDepl+=1
        elif dirDeplacement.lower()=='e' :
            cDepl+=1
        elif dirDeplacement.lower()=='o' :
            cDepl-=1
        else :
            print("direction non reconnue !")
        
        # maintenant on deplace le robot apres avoir verifie si cela est possible
        
        if self.grille[(self.robot['x']+cDepl,self.robot['y']+lDepl)]=='O' :
            print("Deplacement impossible car le robot n'est pas un passe-muraille !")
        else :
            # teste si on se trouve dans l ecadrement d une porte
            # si c est le cas il faut remettre un . apres le depart du robot
            if not self.surPorte :
                elementDeDecor=' '
            else :
                elementDeDecor='.'

            self.grille[(self.robot['x'],self.robot['y'])]=elementDeDecor
            
            # teste si la destination est une porte pour s en souvenir
            if self.grille[(self.robot['x']+cDepl,self.robot['y']+lDepl)]=='.' :
                self.surPorte=True
            else :
                self.surPorte=False

            # et finalement teste si arrive sur sorti donc si gagne
            if self.grille[(self.robot['x']+cDepl,self.robot['y']+lDepl)]=='U' :
                return True
            
            # si non gagne on deplace le robot
            self.robot['x']+=cDepl
            self.robot['y']+=lDepl
            self.grille[(self.robot['x'],self.robot['y'])]='X'
        return False   
