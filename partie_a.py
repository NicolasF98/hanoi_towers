#PARTIE A: Plateau de et listes

def init(n):
    #On créer une variable config_init qui contient une liste des nombre de 1 à n.
    config_init = list(range(1, n+1))

    #On inverse notre liste car à sa création elle est inversé.
    config_init.reverse()

    #Création d'une liste de 3 listes qui représente notre plateau et ses 3 tours.
    plateau = [[],[],[]]

    #On ajoute à l'indice 0 (donc à la tour 1) la liste config_init, notre plateau est donc bien initialisé.
    plateau[0] = list(config_init)

    return plateau


def nombre_disques(plateau, numtour):
    #On revoint le nombre d'élements situé sur la tour donnée en argument.
    return len(plateau[numtour])


def disque_superieur(plateau, numtour):
    #Si la tour est vide on renvoi -1.
    if (len(plateau[numtour]) == 0):
        return -1

    #Sinon on renvoi le plus petit élément placé sur la tour.
    return plateau[numtour][len(plateau[numtour])-1]


def position_disque(plateau, numdisque):
    tour, index_disque = 0, 0

    #On parcourt toutes les tours.
    while (tour != 2):

        #On parcourt tous les index de disque.
        while (index_disque != len(plateau)):

            #Si on trouve notre élément, on renvoit sa position.
            if (plateau[tour][index_disque] == numdisque):
                return tour, index_disque

            #Si on ne le trouve pas on incrémente notre index.
            index_disque += 1

        #Après avoir parcouru tous les index d'une tour, si on ne trouve toujours pas notre élément,
        #on reinitialise notre index à 0 et on passe à la tour suivante.
        index_disque = 0 
        tour += 1

    #Si on ne trouve toujours notre élément pas après avoir parcouru tous les index de toutes les tours,
    # alors l'élément n'existe pas et on renvoi alors -1.
    return -1


def verifier_deplacement(plateau, nt1, nt2):
    #Si la tour initial est vide, on return False.
    if (len(plateau[nt1]) == 0):
        return False

    #Sinon on regarde si la tour final est cohérente.
    else:

        #si la tour final est vide, le déplacement est valide, on return True.
        if (len(plateau[nt2]) == 0):
            return True

        #Si elle n'est pas vide, on vérifie que le disque supérieur de la tour inital est inférieur à celui de la tour final,
        # si c'est le cas le déplacement est valide (return True), sinon il ne l'est pas (return False).
        elif (len(plateau[nt2]) != 0):
            if (disque_superieur(plateau,nt1) < disque_superieur(plateau,nt2)):
               return True
            else:
                return False


def verifier_victoire(plateau, n):
    #On initialise une listes qui vas correspondre au tableau de victoire pour n éléments.
    victoire = [[], [], []]
    
    #on ajoute sur la tour numéro 3 les éléments de 1 à n dans notre liste.
    i = n
    while (i >= 1):
        victoire[2].append(i)
        i -= 1

    #On test si notre plateau correspond à la liste de victoire,
    # si c'est le cas on return True, sinon False.
    if (victoire == plateau):
        return True
    return False