class Elfe:
    mes_elfes = []

    @classmethod
    def somme(cls):
        return sum(lf.calories for lf in cls.mes_elfes)

    @classmethod
    def maj_elfes(cls, e):
        cls.mes_elfes.append(e)
        n = len(cls.mes_elfes)
        #
        indice = n - 2
        while (indice >= 0 
              and cls.mes_elfes[indice].calories <
               cls.mes_elfes[indice + 1].calories):
            cls.mes_elfes[indice + 1], cls.mes_elfes[indice] = \
                cls.mes_elfes[indice], cls.mes_elfes[indice + 1]
            indice -= 1
        #
        if n > 3:
            cls.mes_elfes.pop()
    
    @classmethod
    def creation_elfes(cls, fichier):
        with open(fichier) as fh:
            somme = 0
            for ligne in fh:
                ligne = ligne.strip()
                if ligne == "":
                    lf = cls()
                    lf.calories += somme
                    cls.maj_elfes(lf)
                    somme = 0
                else:
                    somme += int(ligne)
            lf = cls()
            lf.calories += somme
            cls.maj_elfes(lf)

    @classmethod
    def max_calories(cls):
        return max(un_elfe.calories for un_elfe in cls.mes_elfes)

    @classmethod
    def ajoute_elfe(cls, e):
        cls.mes_elfes.append(e)
    
    def __init__(self):
        self._calories = 0
        # self.ajoute_elfe(self)

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, c):
        self._calories += c


Elfe.creation_elfes("jeu2.dat")
print(Elfe.somme())
