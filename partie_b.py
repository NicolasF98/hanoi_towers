#PARTIE B: Graphisme avec Turtle

import turtle

#on augemente la vitesse de dessin de Turtle
turtle.speed('fastest')

def dessine_plateau(n):
    #position initial
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    #plateau
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward( (20*4) + ((40 + (30*(n-1)))*3) + (6*3))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

    #tours
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
    i, j, sortie = 0, 0, 0
    while (i < 3 and sortie == 0):
        while (j < len(plateau[i]) and sortie == 0):
            if (nd == plateau[i][j]):
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*i
                if (len(plateau[i]) == 1):
                    coord_y = 0
                elif (len(plateau[i]) == 2):
                    coord_y = 20*(len(plateau[i])-1)
                else:
                    coord_y = (20 * (n-nd))
                sortie = 1
            j += 1
        j = 0
        i += 1

    turtle.up()
    turtle.goto((-300) + coord_x, (-200) + coord_y)
    turtle.down()
    
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward((40 + (30*(nd-1))))
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

#p = [[],[1,2,3],[]]
#p = [[],[],[1,2,3]]
#p = [[1,2,3],[],[]]
#dessine_disque(2, p, 3)
#dessine_disque(3, p, 3)
#dessine_disque(1, p, 3)

def efface_disque(nd, plateau, n):
    turtle.color('white')
    #turtle.speed('fastest')
    i, j, sortie = 0, 0, 0
    while (i < 3 and sortie == 0):
        while (j < len(plateau[i]) and sortie == 0):
            if (nd == plateau[i][j]):
                coord_x = (20 + 15*(n-nd)) + (40 + (30*n))*i
                if (len(plateau[i]) == 1):
                    coord_y = 0
                elif (len(plateau[i]) == 2):
                    coord_y = 20*(len(plateau[i])-1)
                else:
                    coord_y = (20 * (n-nd))
                sortie = 1
            j += 1
        j = 0
        i += 1

    turtle.up()
    turtle.goto((-300) + coord_x, (-200) + coord_y)
    turtle.down()
    
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward((40 + (30*(nd-1))))
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.color('black')

def dessine_config(plateau, n):
    i, j = 0, 0
    while (i < 3):
        while (j < len(plateau[i])):
            if (len(plateau[i]) != 0):
                dessine_disque(plateau[i][j], plateau, n)
            j += 1
        j = 0
        i += 1

#p = [[],[1,2,3],[]]
#dessine_config(p, 3)

def efface_tout(plateau, n):
    turtle.color('white')
    i, j = 0, 0
    while (i < 3):
        while (j < len(plateau[i])):
            if (len(plateau[i]) != 0):
                dessine_disque(plateau[i][j], plateau, n)
            j += 1
        i += 1