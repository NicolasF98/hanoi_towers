import turtle

def dessine_plateau(n):
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()
    i = 0
    if n == 1:
        longueur = 20
    else:
        longueur = (40 + 30*n)

    turtle.forward(longueur*n + 6*n + 20*n+1)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(longueur*n + 6*n + 20*n+1)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    while (i != n):
        turtle.forward(20 + longueur/2)
        turtle.left(90)
        turtle.forward(longueur/2)
        turtle.right(90)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward(longueur/2)
        turtle.left(90)
        turtle.forward(longueur/2)
        i += 1

dessine_plateau(3)