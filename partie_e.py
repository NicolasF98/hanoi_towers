import time

#cette fonction sera utilisé dans la fonction 'boucle_jeu' de la partie c.
def score_joueur(nom, nbr_disque, nbr_coups):
    #nous allons ajouter le nom ainsi que le
    #score du joueur dans note fichier 'score.txt'.
    score = open("score.txt", "a")

    score.write("Nom du joueur: ")
    score.write(nom.upper())
    score.write('\n')
    score.write("Nbr_disque: ")
    score.write(nbr_disque)
    score.write('\n')
    score.write("Nbr_coups: ")
    score.write(nbr_coups)
    score.write('\n')
    score.write('\n')

    #on oublie pas de fermer notre fichier une fois
    #l'ajout effectué.
    score.close()