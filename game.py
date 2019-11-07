import turtle

def init(n):
    config = list(range(1, n+1))
    config.reverse()
    plateau = [[],[],[]]
    plateau[0] = list(config)
    return plateau

#print(init(3))

def nombre_disques(plateau, numtour):
    return len(plateau[numtour])

#print(nombre_disques(init(3),0))


def disque_superieur(plateau, numtour):
    if (len(plateau[numtour]) == 0):
        return -1
    return plateau[numtour][0]

#print(disque_superieur(init(2),0))

def position_disque(plateau, numdisque):
    i, j = 0, 0
    while (i != 2):
        while (j != len(plateau)):
            if (plateau[i][j] == numdisque):
                return i, j
            j += 1
        i += 1
    return -1

#print(position_disque(init(5),5))

def verifier_deplacement(plateau, nt1, nt2):
    if (len(plateau[nt1]) == 0):
        return False
    else:
        if (len(plateau[nt2]) == 0):
            return True
        elif (len(plateau[nt2]) != 0):
            if (disque_superieur(plateau,nt1) < disque_superieur(plateau,nt2)):
               return True
            else:
                return False
p = [[2],[3],[1]]
#print(verifier_deplacement(p,0,2))


def verifier_victoire(plateau, n):
    i = 0
    while (i != n-2): 
        if (plateau[2][i] > plateau[2][i+1]):
            val = True
        else:
            val = False
        i += 1
    return val

p = [[], [], [3,2,1]]
#print(verifier_victoire(p, 3))



    #################### PARTIE GRAPHIQUE ####################

def dessine_plateau(n):
    turtle.up()
    turtle.goto(-300,-200)
    turtle.down()

    