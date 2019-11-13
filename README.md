# INF101: Projet - Les tours de Hanoi
Université de Grenoble, Licence Sciences & Technologies, 1ère année semestre 1.

UE INF101: Algorithmique et Programmation en Python.

2019 - 2020

---

## Infos binome
- Nicolas Fournout <nicolas.fournout@etu.univ-grenoble-alpes.fr>
- Gabriel Chombart <gabriel.chombart@etu.univ-grenoble-alpes.fr>


## Deadlines

**8 Décembre 2019 à 23h59**

### ~Partie A: plateau de jeu et listes~

- [x] 1 - Initialiser le plateau de jeu, `init`.
- [x] 2 - Implémenter `nombre_disques`.
- [x] 3 - Implémenter `disques_superieur`.
- [x] 4 - Implémenter `position_disque`.
- [x] 5 - Implémenter `verifier_deplacement`.
- [x] 6 - Implémenter `verifier_victoire`.

### Partie B: graphisme avec Turtle

- [x] 1 - Implémenter `dessine_plateau`.
- [x] 2 - Implémenter `dessine_disque`.
- [x] 3 - Implémenter `efface_disques`.
- [ ] 4 - Implémenter `dessine_config`.
- [ ] 5 - Implémenter `efface_tout`.

### Partie C: interactions avec le joueur

- [x] 1 - Implémenter `lire_coords`.
- [ ] 2 - Implémenter `jouer_un_coup` qui utilise la fonction numéro 1.
- [ ] 3 - Implémenter `boucle_jeu`.
- [ ] 4 - Implémenter un programme principal qui demande un nbr de disque souhaité et qui intialise le plateau, le dessine et fini par lancer le jeu.
  
### Partie D: anulation de coups

- [ ] 1 - Implémenter `dernier_coup`.
- [ ] 2 - Implémenter `annuler_dernier_coup`.
- [ ] 3 - Modifier `boucle_jeu` afin d'autoriser les annulations.
- [ ] 4 (BONUS) - Créer un système de sauvage de la partie en cours à l'aide du module pickle.

### Partie E: fichier de score et temps de jeu

- [ ] 1 - Implémenter `score`.
- [ ] 2 - Modifier le main afin de demander le nom du joueur en cas de victoire, il faudra utiliser la fonction `score`.
- [ ] 3 - Faire un affichage des meilleurs scores en utilisant le module turtle.
- [ ] 4 - Sauvegader le temps de jeu de la partie.
- [ ] 5 - Implémenter une fonction qui calcul le temps moyen de reflexion du joueur.
- [ ] 6 - Implémenter une fonction qui affiche un tableau de score des joueurs ayant un faible temps de reflexion.