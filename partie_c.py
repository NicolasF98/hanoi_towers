import partie_b


def lire_coords(plateau):
    valide = 0
    coords = []
    while (valide != 1):
        t_dep = int(input("Choisis tour de départ: "))
        if (0 <= t_dep <= 2 and ((len(plateau[t_dep]) != 0))):
            valide = 1
    coords.append(t_dep)
    while (valide != 0):
        t_arriv = int(input("Choisis tour d'arrivée: "))
        if (0 <= t_arriv <= 2):
            if (len(plateau[t_arriv]) == 0):
                valide = 0
            elif (plateau[t_dep][len(plateau[t_dep])-1] < plateau[t_arriv][len(plateau[t_arriv])-1]):
                valide = 0
    coords.append(t_arriv)
    return coords

def jouer_un_coup(plateau, n):
    coords = lire_coords(plateau)
    val = plateau[coords[0]][len(plateau[coords[0]])-1]
    efface_disque(val, plateau,n)
    plateau[coords[0]].remove(val)
    plateau[coords[1]].append(val)
    dessine_disque(val, plateau, n )

#jouer_un_coup(p,3)
#p = [[1,2,3],[],[]]
#p = [[],[1,2,3],[]]
#p = [[2],[1],[3]]
#dessine_config(p, 3)

def boucle_jeu(plateau, n):
    win = verifier_victoire(plateau,n)
    cpt = 0 #compteur de coups joué
    cpt_max = 10 #on initialise le nbr de coup max à 10
    while ((win != True) and (cpt < cpt_max)):
        jouer_un_coup(plateau,n)
        print(plateau)
        win = verifier_victoire(plateau,n)
        cpt += 1
    print("Formidable ! tu as gagné en:",cpt,"coups ! \nTu es vraiment beaucoup trop fort.")

def main():
    n = int(input("Avec combien de disque souhaites-tu jouer ? "))
    liste_plateau = init(n)
    dessine_plateau(n)
    dessine_config(liste_plateau, n)
    boucle_jeu(liste_plateau, n)

main()