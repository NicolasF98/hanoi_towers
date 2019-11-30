#PARTIE B: Graphisme avec Turtle

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