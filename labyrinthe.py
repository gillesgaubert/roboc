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
        
        # on utilise la chaine passee dans le constructeur pour
        # affecter les attributs
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


    # dans les attributs on a donc:            
    # grille={(colonne,ligne):"elementDeDecor",...} represente la grille
    # robot={'x':valColonne,'y':valLigne} represente la position du robot
    

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
        #nombreDeplacement=1
        resultat="EnCours"
        if len(commande)==0:
            print("Il faut rentrer une commande !")
            resultat="Erreur"
        elif (commande.lower()=='q') :
            # ici sauvegearde et fin du programme
            resultat="Sauvegarde"
        else : 
                # ici une mini-gestion des erreurs :
                # commande doit etre au format "o3" pour 3* ouest
                if ((len(commande)==2) and (commande[1] in '123456789')) :
                    direction=commande[0]
                    nombreDeplacement=int(commande[1])
                    # finalement on peut deplacer le robot

                    resultat=self.deplacementRobot(direction,nombreDeplacement)
                    # resultat qui est renvoye peut etre
                    # Gagne, EnCours ou Sauvegarde
                elif (len(commande)==1):
                    # meme chose quand commande au format "n"
                    direction=commande[0]
                    nombreDeplacement=1
                    resultat=self.deplacementRobot(direction,nombreDeplacement)
                else :
                    print("Je ne comprends pas cette commande !")
                    resultat="Erreur"
        return resultat


    def deplacementRobot(self,dirDeplacement,nbDepl):
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
        
        for i in range(nbDepl):
            # maintenant on deplace le robot apres avoir verifie si cela est possible
        
            if self.grille[(self.robot['x']+cDepl,self.robot['y']+lDepl)]=='O' :
                print("Deplacement impossible car le robot n'est pas un passe-muraille !")
            else :
                # teste si on se trouve dans l encadrement d une porte
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

                # et finalement teste si arrive sur sortie donc si gagne
                if self.grille[(self.robot['x']+cDepl,self.robot['y']+lDepl)]=='U' :
                    return "Gagne"
            
                # si non gagne on deplace le robot
                self.robot['x']+=cDepl
                self.robot['y']+=lDepl
                self.grille[(self.robot['x'],self.robot['y'])]='X'
        return "EnCours"   
