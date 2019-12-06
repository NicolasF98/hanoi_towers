from partie_a import *
from partie_b import *
from partie_c import *
from partie_d import *
from partie_e import *
from partie_f import *

def main():
    print("-- Bienvenue dans les Tours de Hanoi --")
    n = int(input("Avec combien de disque souhaites-tu jouer ? "))
    liste_plateau = init(n)
    dessine_plateau(n)
    dessine_config(liste_plateau, n)
    boucle_jeu(liste_plateau, n)

main()