#dans cette partie nous allons utiliser un dictionnaire qui correspond a l'état courant du plateau en fonction du tour.
#la clé est le numéro du tour
#la valeur la config du plateau

def dernier_coup(dict, num_der_tour):
    return dict[numer_der_tour]

def annuler_dernier_coup(dict, num_der_tour):
    return dict[num_der_tour].reverse()
    