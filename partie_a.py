#PARTIE A: Plateau de et listes

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
    #on revoint le nombre d'élements situé sur la tour donnée en argument.
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
    victoire_rev = [[], [], []]

    #on ajoute sur la tour numéro 3 les éléments de 1 à n dans nos deux listes.
    i = 1
    while (i <= n):
        victoire[2].append(i)
        victoire_rev[2].append(i)
        i += 1

    #on retourne notre liste victoire_rev
    victoire_rev.reverse()

    #on test si notre plateau correspond à une des liste de victoire,
    #si c'est le cas on return True, sinon False
    if (victoire == plateau or victoire_rev == plateau):
        return True
    return False