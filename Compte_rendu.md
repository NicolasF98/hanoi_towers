- FOURNOUT Nicolas
- CHOMBART Gabriel
- IMA-9

# Projet INF101 - Les Tours de Hanoi.

Pour la répartition du travail nous avons fait chacun de notre coté les différentes parties, nous avons par la suite mis en commun nos codes.

Nicolas à commenté tous les codes, redigé le compte rendu en markdown et créée cette page GitHub qui résume l'avancement du Projet: `https://github.com/NicolasF98/hanoi_towers.py`.

Dans ce compte rendu nous allons expliquer pour chaque exercice de chaque partie les difficultées rencontrés (si il y en a eu), les solutions apportés, ainsi qu'une courte explication de la démarche qui nous a permis de résoudre cet exercice.


# Partie A - Plateau de jeu et Listes:

Dans la partie A on initialise les fonctions de base ainsi que la structure de notre plateau de jeu.

Nous n'avons pas rencontré de problème particulier, nous avons simplement suivi les indications fourni par la fiche de projet.

# Partie B - Graphisme avec Turtle:

Dans la partie B, nous avons créée la partie graphique de notre jeu, pour ce faire nous avons utilisé le module `turtle`, ce dernier nous permet d'ouvrire une fenetre graphique et de dessiner
aussi bien notre plateau que nos disques, et nos tours.

Nous n'avons pas fais les parties bonus, c'est-à-dire la coloration des tours/disques et une image de fond, car nous avons préférer consacrer notre temps sur le backend.

Nous avons eu des soucis au niveau de l'affichage des disques, en effet ils ne sont pas parfaitement positionné au milieu des tours.

Nous avons essayé de résoudre ce problème en faisait des essais et en modifiant notre code par tatonnement, nous avons réussi à plus ou moins résoudre
ce problème mais le placement du disque n'est toujours pas optimal.

Egalement nous ne savons pas si la hauteur de la tour doit être fixe ou non, à defaut nous l'avons adapté au nombre de disque.

# Partie C - Interactions avec le joueur: 

La partie C est la partie la plus importante du projet, en effet elle contient la boucle de notre jeu ainsi que le main qui nous permet de lancer notre jeu. Pour lancer notre jeu il faut donc executer cette partie ( `python3 partie_c.py` dans un terminal bash). 

(On aurait pu faire un fichier `main.py` qui aurait contenu la fonction main de la partie_c, et qu'on aurait executé pour lancer notre jeu, mais nous ne l'avons pas fais car non-explicité dans l'énoncer du projet.)

Nous avons renconté des difficulté d'implémentation des partie D et E, mais ces problèmes seront expliqué dans leur partie dédié  dans ce compte rendu.
Nous avons aussi pris la décision de demander à chaque tour à l'utilisateur si il souhaite abandonner ou annuler son coup.


# Partie D - Annulation de coups:

Dans cette partie nous n'avons pas réussi à récuperer les positions du dernier coup joué en fonction des différentes configurations du plateau.

Afin de pouvoir faire se qui est demandé, nous avons récuperé directement les coordonnées fourni par le joueur dans `boucle_de_jeu` de la partie C.

Notre fichier partie_d n'a donc que 1 fonction, nous l'avons modifier en prenant en argument le plateau et le nombre total de disque, ces nouveau arguments vous nous permettre d'appeler nos fonction `efface_disque` puis `dessine_disque`.

Nous n'avons pas fais la partie bonus.

# Partie E - Fichier de scores et temps de jeu:

Nous avons eu des difficultés sur la manipulation de fichier, on a commencé par utiliser un dictionnaire puis nous l'avons mis dans un fichier avec le module `pickle`, mais nous n'avons pas réussi.

Pour ne pas perdre trop de temps on à écrit en pure dans un fichier déjà existant, ce n'est pas idéal mais ça fonctionne.

Nous n'avons pas fais de scoreboard par faute de temps.

# Partie F - Jeu automatique, fonction récursive:

Nous avons créer une 1ere fonction `IA` va va créer une liste de liste avec tous les mouvements à effectuer pour résoudre nos tours de Hanoi en fonction du nombre de disque, on a aussi fais une fonction `dessine_IA` qui dessine avec le module Turtle les déplacement fourni par notre IA, on a implementé une option dans notre boucle de jeu permettant au joueur de voir la solution complète.

Nous avons utillisé le principe de récursion pour faire cette liste de liste, nous n'avons pas rencontré de problème car Nicolas a déjà fait des programmes utilisant la récursion dans d'autres languages de programmation.