- FOURNOUT Nicolas
- CHOMBART Gabriel
- IMA-9

# Projet INF101 - Les Tours de Hanoi.

Pour la répartition du travail nous avons fait chacun de notre coté les différentes parties, nous avons par la suite mis en commun nos codes.

Nicolas à commenté tous les codes, redigé le compte rendu en markdown et créée cette page GitHub qui résume l'avancement du Projet: `https://github.com/NicolasF98/hanoi_towers.py`.

Dans ce compte rendu nous allons expliquer pour chaque exercice de chaque partie les difficultées rencontrés (si il y en a eu), les solutions apportés, ainsi qu'une courte explication de la démarche qui nous a permis de résoudre cet exercice.

## Partie A:

Dans la partie A nous initialisons les fonctions de base ainsi que la structure de notre plateau de jeu.

Nous n'avons pas rencontré de problème particulier, nous avons tout simplement suivi les indications fourni par les consignes de travail.

```py
def init(n):
    #on créer une variable config_init qui contient une liste des nombre de 1 à n.
    config_init = list(range(1, n+1))

    #on inverse notre liste car à sa création elle est inversé.
    config_init.reverse()

    #creation d'une liste de 3 liste qui représente notre plateau et ses 3 tours.
    plateau = [[],[],[]]

    #on ajoute à l'indice 0 (donc à la tour 1) la liste config_init, notre plateau est donc bien initialisé.
    plateau[0] = list(config_init)
    return plateau


def nombre_disques(plateau, numtour):
    #on renvoint le nombre d'éléments situé sur la tour donnée en argument.
    return len(plateau[numtour])


def disque_superieur(plateau, numtour):
    #si la tour est vide on renvoi -1.
    if (len(plateau[numtour]) == 0):
        return -1

    #sinon on renvoi le plus petit élément placé sur la tour.
    return plateau[numtour][len(plateau[numtour])-1]


def position_disque(plateau, numdisque):
    tour, index_disque = 0, 0

    #on parcours toutes les tours
    while (tour != 2):

        #on parcours tous les index de disque
        while (index_disque != len(plateau)):

            #si on trouve notre element, on renvoie sa position
            if (plateau[tour][index_disque] == numdisque):
                return tour, index_disque

            #si on ne le trouve pas on incremente notre index
            index_disque += 1

        #après avoir parcouru tous les index d'une tour, si on ne trouve toujours pas notre element,
        #on reinitialise notre index a 0 et on passe à la tour suivante.
        index_disque = 0 
        tour += 1

    #si on ne trouve toujours pas après avoir parcouru tous les index de toutes les tours,
    #l'élément n'existe pas et on renvoi alors -1
    return -1


def verifier_deplacement(plateau, nt1, nt2):
    #si la tour initial est vide, on return False
    if (len(plateau[nt1]) == 0):
        return False

    #sinon on regarde si la tour final est cohérente
    else:

        #si la tour final est vide, le deplacement est valide, on return True
        if (len(plateau[nt2]) == 0):
            return True

        #si elle n'est pas vide, on verifie que le disque supérieur de la tour inital est inférieur à celui de la tour final
        #si c'est le cas le deplacement est valide (return True), sinon il ne l'est pas (return False)
        elif (len(plateau[nt2]) != 0):
            if (disque_superieur(plateau,nt1) < disque_superieur(plateau,nt2)):
               return True
            else:
                return False


def verifier_victoire(plateau, n):
    #On initialise 2 listes qui vont correspondre au tableau de victoire pour n éléments.
    victoire = [[], [], []]
    
    #on ajoute sur la tour numéro 3 les éléments de 1 à n dans nos deux listes.
    i = n
    while (i >= 1):
        victoire[2].append(i)
        i -= 1

    #on test si notre plateau correspond à une des liste de victoire,
    #si c'est le cas on return True, sinon False
    if (victoire == plateau):
        return True
    return False
```

# Partie B:

Dans la partie B, nous créons la partie graphique de notre jeu, pour ce faire nous avons utilisé le module `turtle`, ce dernier nous permet d'ouvrire une fenetre graphique et de dessiner
aussi bien notre plateau que nos disques, et nos tours.

Nous avons eu des soucis au niveau de l'affichage des disques, en effet ils ne sont pas parfaitement positionné au milieu des tours.

Nous avons essayé de resoudre ce problème en faisait des essais et en modifiant notre code par tatonnement, nous avons reussi à plus ou moins resoudre 
ce problème mais le placement du disque n'est toujours pas optimal.

Egalement nous ne savons pas si la hauteur de la tour doit être fixe ou non, à defaut nous l'avons adapté au nombre de disque.

```py
import turtle

#on augemente la vitesse de dessin de Turtle
turtle.speed('fastest')

def dessine_plateau(n):
    #position initial de notre plateau
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    #dessin du plateau
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

    #dessin des tours
    i = 0
    while(i != 3):
        turtle.forward(20 + ((40 + (30*(n-1)))/2))
        turtle.left(90)
        turtle.forward(20 + (40 + (30*(n-1)))/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward( 20 + (40 + (30*(n-1)))/2 )
        turtle.left(90)
        turtle.forward((40 + (30*(n-1)))/2 )
        i += 1


def dessine_disque(nd, plateau, n):
    #initialisation de 3 variables à 0.
    #tour correspond à l'indice de tour.
    #disque à l'indice du disque.
    #sortie nous sert de condition de sortie.
    tour, disque, sortie = 0, 0, 0
    coord_x, coord_y = 0, 0

    #on va chercher la position initiale de notre disque.
    #on boucle temps qu'on est sur une de nos 3 tours et 
    #que la condition de sortie n'est pas valide.
    while (tour < 3 and sortie != 1):

        #on parcour toutes les positions possible de disque sur une tour précise.
        while (disque < len(plateau[tour]) and sortie != 1):

            #si on trouve notre disque
            if (nd == plateau[tour][disque]):

                #la coord initial en x est alors:
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*tour

                #si notre tour est la tour initiale avec n disque, alors sa position y est:
                if (len(plateau[tour]) == n):
                    coord_y = (20 * (n-nd))
                
                #sinon:
                else: 
                    coord_y = 20*(len(plateau[tour])-1)

                sortie = 1
            disque += 1
        disque = 0
        tour += 1

    #on se deplace à la position initiale du disque
    turtle.up()
    turtle.goto((-300) + coord_x, (-200) + coord_y)
    turtle.down()
    
    #on dessine le disque
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward((40 + (30*(nd-1))))
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.color('black')


def efface_disque(nd, plateau, n):
    #on re-utilise la fonction dessine_disque, mais on dessine en blanc
    turtle.color('white')
    dessine_disque(nd, plateau, n)


def dessine_config(plateau, n):
    #on initialise notre index tour et disque à 0.
    tour, disque = 0, 0

    #on parcours toutes nos tours.
    while (tour < 3):

        #on dessine tous nos disques.
        while (disque < len(plateau[tour])):
            if (len(plateau[tour]) != 0):
                dessine_disque(plateau[tour][disque], plateau, n)
            disque += 1
        
        #on reinitilise notre variable disque et on passe à la tour suivante.
        disque = 0
        tour += 1


def efface_tout(plateau, n):
    #on change la couleur en blanc afin de pouvoir effacer.
    turtle.color('white')

    #on utilise la fonction dessine_config
    dessine_config(plateau, n)
```

# Partie C:

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

# Partie D:

Dans cette partie nous n'avons pas su comment recuperer les positions du dernier coup joué en fonction des différentes configuration du plateau.

Afin de pouvoir faire se qui est demandé nous avons recuperer directement les coordonnées fourni par le joueur dans la partie C et à l'aide de la foncton lire_coords.

