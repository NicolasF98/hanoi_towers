from partie_a import *
from partie_b import *

#Nous avons utiliser la récursion dans cette fonction
def IA(n , tour_deb, tour_arriv, tour_sec, coups_IA):

    #Notre conditions de "sortie" de recursion, elle va nous permettre de build notres stack.
    if n == 1:

        #On ajoute les coordonnées dans notre liste.
        coups_IA.append([tour_deb, tour_arriv])

        #on force un return pour avoir les autres élément de notre stack.
        return

    #On appelle de nouveau notre fonction avec n-1, et on donne notre tour secondaire comme tour d'arrivé de notre disque.
    IA(n-1, tour_deb, tour_sec, tour_arriv, coups_IA) 

    #On ajoute les nouvelles valeurs dans notre liste.
    coups_IA.append([tour_deb, tour_arriv])

    #On appelle de nouveau notre fonction avec n-1, et on donne notre tour secondaire comme tour de depart de notre disque.
    IA(n-1, tour_sec, tour_arriv, tour_deb, coups_IA)
    
    return coups_IA

coups_IA = []
print(IA(3,"1","3","2",coups_IA))

def dessine_IA(n, coups_IA):
    print("-- Bienvenue dans les Tours de Hanoi --")
    n = 3 #int(input("Avec combien de disque souhaites-tu jouer ? "))

    plateau = init(n)
    dessine_plateau(n)
    dessine_config(plateau, n)
    for coords in coups_IA:
        print(plateau)
        print(int(coords[0]))
        print(int(coords[1]))

        val = plateau[int(coords[0])-1][len(plateau[int(coords[0])-1])-1]
        print(val)

        efface_disque(val, plateau, n)        

        print(plateau[int(coords[0])-1])
        plateau[int(coords[0])-1].remove(val)
        plateau[int(coords[1])-1].append(val)
        
        dessine_disque(val, plateau, n)

dessine_IA(3,IA(3,"1","3","2",[]))