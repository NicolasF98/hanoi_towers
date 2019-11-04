import turtle

def dessine_plateau(n):
    if n == 1:
        longueur = 20
    else:
        longueur = 20 + 30*n

    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(longueur)
    turtle.right(90)
    turtle.forward(20)

    turtle.forward(longueur * 1/3)
    turtle.left(90)
    turtle.forward(longueur * 1/3)
    
dessine_plateau(3)