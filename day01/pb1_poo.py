class Elfe:
    mes_elfes = []

    @classmethod
    def creation_elfes(cls, fichier):
        cls.mes_elfes = []
        elfe_courant = cls()
        #
        with open(fichier) as fh:
            for ligne in fh:
                ligne = ligne.strip()
                if ligne == "":
                    elfe_courant = cls()
                else:
                    elfe_courant.calories = int(ligne)

    @classmethod
    def max_calories(cls):
        return max(un_elfe.calories for un_elfe in cls.mes_elfes)

    @classmethod
    def ajoute_elfe(cls, e):
        cls.mes_elfes.append(e)
    
    def __init__(self):
        self._calories = 0
        self.ajoute_elfe(self)

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, c):
        self._calories += c


Elfe.creation_elfes("jeu2.dat")
print(Elfe.max_calories())
