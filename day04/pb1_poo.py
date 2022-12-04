class Paire:
    somme = 0

    @classmethod
    def lecture_fichier(cls, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                ligne = ligne.strip()
                e1, e2 = ligne.split(",")
                m1, M1 = map(int, e1.split("-"))
                m2, M2 = map(int, e2.split("-"))
                if cls(m1, M1, m2, M2).est_inclus():
                    cls.somme += 1

    def __init__(self, m1, M1, m2, M2):
        self._m1 = m1
        self._M1 = M1
        self._m2 = m2
        self._M2 = M2

    def est_inclus(self):
        return self._m1 <= self._m2 and self._M1 >= self._M2 \
            or self._m1 >= self._m2 and self._M1 <= self._M2


Paire.lecture_fichier("jeu2.dat")
print(Paire.somme)
