def IA(n , tour_deb, tour_arriv, tour_sec, tour):
    tour += 1 
    coups_IA = []
    if n == 1:
        coups_IA.append([tour_deb, tour_arriv])
        print ("Disque 1 de la tour",tour_deb,"à la tour",tour_arriv)
        return
    coups_IA.append([tour_deb, tour_arriv])
    IA(n-1, tour_deb, tour_sec, tour_arriv,tour)
    coups_IA.append([tour_deb, tour_arriv])
    print ("Disque",n,"de la tour",tour_deb,"à la tour",tour_arriv)
    IA(n-1, tour_sec, tour_arriv, tour_deb, tour)
    coups_IA.append([tour_deb, tour_arriv])

    return coups_IA

print(IA(3,"1","3","2", 0))