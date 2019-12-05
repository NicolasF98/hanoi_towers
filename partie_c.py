#PARTIE C: Interactions avec le joueur

from partie_a import *
from partie_b import *
from partie_d import *
from partie_e import *


def lire_coords(plateau):
    #valide_dep et _arr vont être nos conditions de sortie de nos boucles.
    valide_dep = 0
    valide_arr = 0

    #Création de la liste de sortie de nos coordonnées.
    coords = []

    #On boucle temps que le joueur n'a pas donnée une coord de départ valide.
    while (valide_dep != 1):
        t_dep = int(input("Choisis la tour de départ: "))
        if (0 <= t_dep <= 2 and ((len(plateau[t_dep]) != 0))):
            valide_dep = 1
        elif ((len(plateau[t_dep]) == 0)):
            print("Invalide, tour vide.")
        elif (0 > t_dep > 2):
            print("Invalide, la tour n'existe pas.")
    coords.append(t_dep)

    #On boucle temps que le joueur n'a pas donnée une coord d'arrivé valide.
    while (valide_arr != 1):
        t_arriv = int(input("Choisis la tour d'arrivée: "))
        if (0 <= t_arriv <= 2):
            if (len(plateau[t_arriv]) == 0):
                valide_arr = 1
            elif (plateau[t_dep][len(plateau[t_dep])-1] < plateau[t_arriv][len(plateau[t_arriv])-1]):
                valide_arr = 1
    coords.append(t_arriv)

    return coords


def jouer_un_coup(plateau, n):
    #On récupére les coordonnées de déplacement fournis par le joueur.
    coords = lire_coords(plateau)

    #On récupère la valeur de départ demandé par le joueur.
    val = plateau[coords[0]][len(plateau[coords[0]])-1]

    #On supprime la position initiale du disque sur notre plateau.
    efface_disque(val, plateau,n)

    #On déplace notre disque sur sa nouvelle position dans notre liste représentant notre plateau.
    plateau[coords[0]].remove(val)
    plateau[coords[1]].append(val)

    #On dessine la nouvelle position de notre disque.
    dessine_disque(val, plateau, n)

    return coords

def boucle_jeu(plateau, n):
    #La variable `win` correspond à la condition de victoire, en fonction du plateau et de nbr de disque.
    win = verifier_victoire(plateau,n)

    #Création du dictionnaire qui nous permet de récupèrere la paire de mouvement du joueur, en fonction du coup.
    coups = {}     # PARTIE D #

    #Compteur de coups joué.
    cpt = 1 

    #Variable qui nous sert de booléen d'annulation.
    annuler = 0

    #On initialise le nbr de coup max à 10.
    cpt_max = 10

    #On boucle temps que le joueur n'a pas gagné ou que le nbr max de coup n'est pas atteint.
    while (win != True) and (cpt <= cpt_max):
        print("Coup numéro ",cpt)

        #On récupère les coordonées fournit par le joueur au coup cpt, cela nous permet de faire un suivi 
        # des coups qu'on pourra annuler par la suite.
        coups[cpt] = jouer_un_coup(plateau,n)        # PARTIE D #

        #On propose à l'utilisateur d'annuler son coup. 1 pour oui, 0 pour non.
        annuler = int(input("Veux-tu annuler ce coup ? (1/0) "))

        #Si il accepte, on appelle notre fonction annuler_dernier_coup et on décremente notre compteur.
        if (annuler == 1):
            annuler_dernier_coup(coups, cpt, plateau, n)
            cpt += -1
        
        #0n reinitialise notre variable annuler à 0 afin d'éviter des problèmes de booleen au prochain tour de boucle.
        annuler = 0

        #On vérifie si on à réussi notre jeu, on stock le resultat dans une variable `win`.
        win = verifier_victoire(plateau,n)
        cpt += 1
    
    #Si le joueur a joué trop de coups, il a perdu.
    if (cpt >= cpt_max):
        print("Désolé tu as perdu !")
    
    #Sinon il a gagné.
    else:
        print("Formidable ! tu as gagné en:",cpt,"coups ! \nTu es vraiment beaucoup trop fort.")
        nom_joueur = input("Quel est ton nom jeune joueur ?")

    #On ajoute le score de 'nom_joueur' dans notre txt avec l'aide de la fonction 'score_joueur'.
    score_joueur(nom_joueur, str(n), str(cpt))          # PARTIE E #


#definition d'une fonction main comme demandé.
def main():
    print("-- Bienvenue dans les Tours de Hanoi --")
    n = int(input("Avec combien de disque souhaites-tu jouer ? "))
    liste_plateau = init(n)
    dessine_plateau(n)
    dessine_config(liste_plateau, n)
    boucle_jeu(liste_plateau, n)

main()