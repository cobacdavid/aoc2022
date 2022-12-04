class Rucksack:
    lst = []
    somme = 0

    @staticmethod
    def priorite_groupe(t1, t2, t3):
        i = 0
        while i < 52 and t1[i] * t2[i] * t3[i] == 0:
            i += 1
        return i + 1

    @classmethod
    def _traitement_somme(cls):
        cls.somme += cls.priorite_groupe(
                        *[r.contenu for r in cls.lst]
        )
        cls.lst = []

    @classmethod
    def lecture_contenus(cls, fichier):
        with open(fichier) as fh:
            for i, contenu in enumerate(fh):
                if i % 3 == 0 and i != 0:
                    cls._traitement_somme()
                contenu = contenu.strip()
                cls().contenu = contenu
            cls._traitement_somme()

    @classmethod
    def ajoute_sac(cls, r):
        cls.lst.append(r)

    def __init__(self):
        self._contenu = [0 for _ in range(52)]
        self._taille_comp = 0
        self.ajoute_sac(self)

    @property
    def contenu(self):
        return self._contenu

    @contenu.setter
    def contenu(self, chaine):
        n = len(chaine)
        self._taille_comp = n
        for i in range(n):
            o = ord(chaine[i])
            o -= 97 if o > 90 else 65 - 26
            self._contenu[o] += 1


Rucksack.lecture_contenus("jeu2.dat")
print(Rucksack.somme)
