#PARTIE D: Annulation de coups
    
from partie_b import *

def annuler_dernier_coup(dict, num_der_tour, plateau, n):
    #On place les valeurs joué dans un variable.
    val = dict[num_der_tour]

    #On efface le disque du plateau.
    efface_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau, n)
    
    #On supprime la clé et ses valeur du dictionnaire.
    del dict[num_der_tour]

    #On retroune ces valeurs afin de d'avoir les valeurs d'annulation.
    val.reverse()

    #On change le disque de position dans le plateau.
    plateau[val[1]].append(plateau[val[0]][len(plateau[val[0]])-1])
    plateau[val[0]].remove(plateau[val[0]][len(plateau[val[0]])-1])

    #On redessine le disque à sa nouvelle position.
    dessine_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau , n)

    #On decremente le compteur de tour directement dans `boucle_de_jeu` de la partie c.

