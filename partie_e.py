import time

def score_joueur(nom, nbr_disque, nbr_coups):
    #On écrit dans notre fichier 'score.txt', préalablement créer.
    score = open("score.txt", "a")

    #Nous allons ajouter le nom ainsi que le
    # score du joueur dans un fichier 'score.txt'.
    score.write("Nom du joueur: ")
    score.write(nom.upper())
    score.write('\n')
    score.write("Nbr_disque: ")
    score.write(nbr_disque)
    score.write('\n')
    score.write("Nbr_coups: ")
    score.write(nbr_coups)
    score.write('\n')

    #On enregistre la date de la partie avec le module time.
    score.write("Date partie: ")
    temps = time.ctime()
    score.write(str(temps))
    score.write('\n')
    score.write('\n')
    score.close()