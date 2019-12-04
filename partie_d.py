#PARTIE D: Annulation de coups

#dans cette partie nous allons utiliser un dictionnaire qui correspond aux coups joué en fonction du tour.
#la clé est le numéro du tour
#les valeur sont les coups joué
    
from partie_b import *

def annuler_dernier_coup(dict, num_der_tour, plateau, n):
    #on place les valeurs joué dans un variable.
    val = dict[num_der_tour]

    #on efface le disque du plateau 
    efface_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau, n)
    
    #on supprime la clé et ses valeur du dictionnaire
    del dict[num_der_tour]

    #on retroune ces valeurs afin de d'avoir les valeurs d'annulation.
    val.reverse()

    #on change le disque de position dans le plateau.
    plateau[val[1]] = plateau[val[0]]

    #on redessine le disque à sa nouvelle position.
    dessine_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau , n)

    #on decremente le compteur de tour directement dans la boucle de jeu.