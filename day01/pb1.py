with open("jeu1.dat") as fh:
    mx = 0
    somme = 0
    for ligne in fh:
        ligne = ligne.strip()
        if ligne == "":
            somme = 0
        else:
            somme += int(ligne)
            if somme > mx:
                mx = somme
    print(mx)
