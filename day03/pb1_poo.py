class Rucksack:
    lst = []

    @classmethod
    def lecture_contenus(cls, fichier):
        with open(fichier) as fh:
            for contenu in fh:
                contenu = contenu.strip()
                cls().comp = contenu

    @classmethod
    def ajoute_sac(cls, r):
        cls.lst.append(r)

    @classmethod
    def affiche_priorites(cls):
        p = []
        for r in cls.lst:
            p.append(r.priorite())
        return p

    def __init__(self):
        self._comp = [[0, 0] for _ in range(52)]
        self._taille_comp = 0
        self.ajoute_sac(self)

    @property
    def comp(self):
        return self._comp

    @comp.setter
    def comp(self, chaine):
        n = len(chaine)
        self._taille_comp = n // 2
        for i in range(n):
            o = ord(chaine[i])
            o -= 97 if o > 90 else 65 - 26
            indice = 0 if i < self._taille_comp else 1
            self._comp[o][indice] += 1

    def _commun(self):
        i = 0
        while (i < 52
               and self._comp[i][0] * self._comp[i][1] == 0):
            i += 1
        return i

    def priorite(self):
        return self._commun() + 1


Rucksack.lecture_contenus("jeu2.dat")
print(sum(Rucksack.affiche_priorites()))
