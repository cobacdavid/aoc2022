class Chaine:
    def __init__(self, v):
        self._chaine = v

    @property
    def chaine(self):
        return self._chaine

    @chaine.setter
    def chaine(self, c):
        self ._chaine = c

    def _tous_differents(self, indice, lng):
        reponse = False
        if indice + lng - 1< len(self._chaine):
            reponse = len(set(self._chaine[indice:indice+lng])) == lng
        return reponse

    def pindice_tous_differents(self, lng):
        indice = 0
        while indice < len(self._chaine) and not self._tous_differents(indice, lng):
            indice += 1
        return indice + lng


fichier = "jeu2.dat"
with open(fichier) as fh:
    for ligne in fh:
        ligne = ligne.strip()
        print(Chaine(ligne).pindice_tous_differents(14))
