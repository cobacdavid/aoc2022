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
                if cls(m1, M1, m2, M2).possede_partie_commune():
                    cls.somme += 1

    def __init__(self, m1, M1, m2, M2):
        self._m1 = m1
        self._M1 = M1
        self._m2 = m2
        self._M2 = M2

    def possede_partie_commune(self):
        return self._m1 <= self._m2 <= self._M1 \
            or self._m2 <= self._m1 <= self._M2


Paire.lecture_fichier("jeu2.dat")
print(Paire.somme)
