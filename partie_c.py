#PARTIE C: Interactions avec le joueur

from partie_b import *
from partie_a import *
from partie_d import *
from partie_e import *


def lire_coords(plateau):
    #valide_dep et _arr vont être nos conditions de sortie de nos boucles.
    valide_dep = 0
    valide_arr = 0

    #creation de la liste de sortie de nos coordonnées.
    coords = []

    #on boucle temps que le joueur n'a pas donnée une coord de départ valide.
    while (valide_dep != 1):
        t_dep = int(input("Choisis la tour de départ: "))
        if (0 <= t_dep <= 2 and ((len(plateau[t_dep]) != 0))):
            valide_dep = 1
        elif ((len(plateau[t_dep]) == 0)):
            print("Invalide, tour vide.")
        elif (0 > t_dep > 2):
            print("Invalide, la tour n'existe pas.")
    coords.append(t_dep)

    #on boucle temps que le joueur n'a pas donnée une coord de départ valide.
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
    #on recupére les coordonnées de deplacement fournis par le joueur.
    coords = lire_coords(plateau)

    #on récupère la valeur de depart demandé par le joueur.
    val = plateau[coords[0]][len(plateau[coords[0]])-1]

    #on supprime la position initiale du disque sur notre plateau.
    efface_disque(val, plateau,n)

    #on déplace notre disque sur sa nouvelle position dans notre liste representant notre plateau.
    plateau[coords[0]].remove(val)
    plateau[coords[1]].append(val)

    #on dessine la nouvelle position de notre disque.
    dessine_disque(val, plateau, n)

    return coords

def boucle_jeu(plateau, n):
    #la variable win correspond à la condition de victoire, en fonction du plateau et de nbr de disque.
    win = verifier_victoire(plateau,n)

    #creation du dictionnaire qui nous permet de recuperere la paire de mouvement du joueur, en fonction du coup.
    coups = {}

    #compteur de coups joué.
    cpt = 1 

    #variable qui nous sert de booléen d'annulation.
    annuler = 0

    #on initialise le nbr de coup max à 10.
    cpt_max = 10

    #on boucle temps que le joueur n'a pas gagné ou que le nbr max de coup n'est pas atteind.
    while (win != True) and (cpt <= cpt_max):
        print("Coup numéro ",cpt)

        #recupère les coordonées donnée par le joueur au coup cpt, cela nous permet de faire un suivi 
        #des coups qu'on pourra annuler par la suite.
        coups[cpt] = jouer_un_coup(plateau,n)
        print(coups)
        annuler = int(input("Veux-tu annuler ce coup ? (1/0) "))
        if (annuler == 1):
            annuler_dernier_coup(coups, cpt, plateau, n)
            cpt += -1
            

        annuler = 0


        print(plateau)
        win = verifier_victoire(plateau,n)
        cpt += 1
    if (cpt >= cpt_max):
        print("Désolé tu as perdu !")
    else:
        print("Formidable ! tu as gagné en:",cpt,"coups ! \nTu es vraiment beaucoup trop fort.")
        nom_joueur = input("Quel est ton nom jeune joueur ?")
    #nous devons ajouter le score de 'nom_joueur' dans notre txt avec l'aide de la fonction
    #'score_joueur'.
    score_joueur(nom_joueur, str(n), str(cpt))

#definition d'une fonction main comme demandé.
def main():
    print("-- Bienvenue dans les Tours de Hanoi --")
    n = int(input("Avec combien de disque souhaites-tu jouer ? "))
    liste_plateau = init(n)
    dessine_plateau(n)
    dessine_config(liste_plateau, n)
    boucle_jeu(liste_plateau, n)

main()