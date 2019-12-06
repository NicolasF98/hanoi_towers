- FOURNOUT Nicolas
- CHOMBART Gabriel
- IMA-9

# Projet INF101 - Les Tours de Hanoi.

Pour la répartition du travail nous avons fait chacun de notre coté les différentes parties, nous avons par la suite mis en commun nos codes.

Nicolas à commenté tous les codes, redigé le compte rendu en markdown et créée cette page GitHub qui résume l'avancement du Projet: `https://github.com/NicolasF98/hanoi_towers.py`.

Dans ce compte rendu nous allons expliquer pour chaque exercice de chaque partie les difficultées rencontrés (si il y en a eu), les solutions apportés, ainsi qu'une courte explication de la démarche qui nous a permis de résoudre cet exercice.

# Partie A - Plateau de jeu et Listes:

Dans la partie A on initialise les fonctions de base ainsi que la structure de notre plateau de jeu.

Nous n'avons pas rencontré de problème particulier, nous avons simplement suivi les indications fourni par la fiche de projet.

# Partie B - Graphisme avec Turtle:

Dans la partie B, nous avons créée la partie graphique de notre jeu, pour ce faire nous avons utilisé le module `turtle`, ce dernier nous permet d'ouvrire une fenetre graphique et de dessiner
aussi bien notre plateau que nos disques, et nos tours.

Nous n'avons pas fais les parties bonus, c'est-à-dire la coloration des tours/disques et une image de fond, car nous avons préférer consacrer notre temps sur le backend.

Nous avons eu des soucis au niveau de l'affichage des disques, en effet ils ne sont pas parfaitement positionné au milieu des tours.

Nous avons essayé de résoudre ce problème en faisait des essais et en modifiant notre code par tatonnement, nous avons réussi à plus ou moins résoudre
ce problème mais le placement du disque n'est toujours pas optimal.

Egalement nous ne savons pas si la hauteur de la tour doit être fixe ou non, à defaut nous l'avons adapté au nombre de disque.

# Partie C - Interactions avec le joueur: 

La partie C est la partie la plus importante du projet, en effet elle contient la boucle de notre jeu ainsi que le main qui nous permet de lancer notre jeu.

Nous n'avons pas renconter de grosse difficulté, à par des soucis d'implementation des partie D et E, mais ces problèmes seront expliqué plus bas dans ce compte rendu.

Nicolas à prit l'initiative de créer une fonction `main` et de l'executé directement dans la partie_c, au lieu d'avoir une suite de commandes écrites à la fin de cette partie, cela semble plus ordonné.

```py
from partie_a import *
from partie_b import *
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

    #creation du dictionnaire qui nous permet de recuperere la paire de mouvement du joueur, en fonction du coup.    "PARTIE D"
    coups = {}      # "PARTIE D"

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
        coups[cpt] = jouer_un_coup(plateau,n)       #"PARTIE D"

        #on propose a l'utilisateur de d'annuler son coup.
        annuler = int(input("Veux-tu annuler ce coup ? (1/0) "))

        #si il accepte, on appelle notre fonction annuler_dernier_coup et on decremente notre compteur.
        if (annuler == 1):
            annuler_dernier_coup(coups, cpt, plateau, n)
            cpt += -1
        
        #on remette notre variable annuler à 0 afin d'éviter des problèmes booleen au prochain tour de boucle.
        annuler = 0

        #on verifie si on a reussi notre jeu, on stock  le resultat dans une variable `win`.
        win = verifier_victoire(plateau,n)
        cpt += 1
    
    #si le joueur à joué trop de coups, il a perdu.
    if (cpt >= cpt_max):
        print("Désolé tu as perdu !")
    
    #sinon il a gagné.
    else:
        print("Formidable ! tu as gagné en:",cpt,"coups ! \nTu es vraiment beaucoup trop fort.")
        nom_joueur = input("Quel est ton nom jeune joueur ?")

    #on ajoute le score de 'nom_joueur' dans notre txt avec l'aide de la fonction 'score_joueur'.
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
```

# Partie D - Annulation de coups:

Dans cette partie nous n'avons pas réussi à récuperer les positions du dernier coup joué en fonction des différentes configurations du plateau.

Afin de pouvoir faire se qui est demandé, nous avons récuperé directement les coordonnées fourni par le joueur dans `boucle_de_jeu` de la partie C.

Notre fichier partie_d n'a donc que 1 fonction, nous l'avons modifier en prenant en argument le plateau et le nombre total de disque, ces nouveau arguments vous nous permettre d'appeler nos fonction `efface_disque` puis `dessine_disque`.

```py
from partie_b import *

def annuler_dernier_coup(dict, num_der_tour, plateau, n):
    #on place les valeurs joué dans un variable.
    val = dict[num_der_tour]

    #on efface le disque du plateau 
    efface_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau, n)
    
    #on supprime la clé et ses valeur du dictionnaire
    del dict[num_der_tour]

    #on retourne ces valeurs afin de d'avoir les valeurs d'annulation.
    val.reverse()

    #on change le disque de position dans le plateau.
    plateau[val[1]] = plateau[val[0]]

    #on redessine le disque à sa nouvelle position.
    dessine_disque(plateau[val[1]][len(plateau[val[1]])-1] ,plateau , n)

    #on décremente le compteur de tour directement dans la fonction `boucle_de_jeu`.
```

# Partie E - Fichier de scores et temps de jeu:

Nous avons
