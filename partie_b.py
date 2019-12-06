#PARTIE B: Graphisme avec Turtle

import turtle

#On augemente la vitesse de dessin de Turtle.
turtle.speed('fastest')

def dessine_plateau(n):
    #On va à la position initiale de notre plateau.
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    #On dessine le plateau en fonction du nombre de disque.
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

    #On dessin nos 3 tours.
    i = 0
    while(i != 3):
        turtle.forward(20 + ((40 + (30*(n-1)))/2))
        turtle.left(90)
        turtle.forward(20 + (40 + (30*(n)))/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward( 20 + (40 + (30*(n)))/2 )
        turtle.left(90)
        turtle.forward((40 + (30*(n-1)))/2 )
        i += 1


def dessine_disque(nd, plateau, n):
    #Initialisation de 3 variables à 0:
    # tour correspond à l'indice de tour.
    # disque à l'indice du disque.
    # sortie nous sert de condition de sortie dans notre boucle while.
    tour, disque, sortie = 0, 0, 0

    #On déclare les nouvelles coordonnées initiales du disque.
    coord_x, coord_y = 0, 0

    #On va chercher la position initiale de notre disque.
    #On boucle temps que l'on est sur une de nos 3 tours et 
    # que la condition de sortie n'est pas valide.
    while (tour < 3 and sortie != 1):

        #On parcourt toutes les positions possible de disque sur une tour précise.
        while (disque < len(plateau[tour]) and sortie != 1):

            #Si on trouve notre disque.
            if (nd == plateau[tour][disque]):

                #La coord initial en x est alors:
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*tour

                #Si notre tour est la tour initiale avec n disque, alors sa position y est:
                if (len(plateau[tour]) == n):
                    coord_y = (20 * (n-nd))
                
                #Sinon:
                else: 
                    coord_y = 20*(len(plateau[tour])-1)

                sortie = 1
            disque += 1
        disque = 0
        tour += 1

    #On se deplace à la position initiale du disque.
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
    #On reutilise la fonction dessine_disque, mais on dessine en blanc afin d'effacer notre disque.
    turtle.color('white')
    dessine_disque(nd, plateau, n)

def dessine_config(plateau, n):
    #On initialise notre index de tour et de disque à 0.
    tour, disque = 0, 0

    #On parcourt toutes nos tours.
    while (tour < 3):

        #On dessine tous nos disques sur 1 tour précise.
        while (disque < len(plateau[tour])):
            if (len(plateau[tour]) != 0):
                dessine_disque(plateau[tour][disque], plateau, n)
            disque += 1
        
        #On reinitilise notre variable disque et on passe à la tour suivante.
        disque = 0
        tour += 1

def efface_tout(plateau, n):
    #On change la couleur en blanc afin de pouvoir effacer tous les disques du plateau.
    turtle.color('white')

    #On utilise la fonction dessine_config.
    dessine_config(plateau, n)