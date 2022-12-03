class chifoumi:
    opposant = {'A': 'R', 'B': 'P', 'C': 'S'}
    moi = {'X': ('R', 1), 'Y': ('P', 2), 'Z': ('S', 3)}
    regles = [('R', 'S'), ('S', 'P'), ('P', 'R')]

    @classmethod
    def etude_un_jeu(cls, opp, moi):
        choix_opp = cls.opposant[opp]
        choix_moi = cls.moi[moi]

        if choix_moi[0] == choix_opp:
            score_partie = 3
        else:
            if (choix_moi[0], choix_opp) in cls.regles:
                score_partie = 6
            else:
                score_partie = 0

        return choix_moi[1] + score_partie

    def __init__(self, fic):
        self._score = 0
        self._lecture_parties(fic)

    def _lecture_parties(self, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                opp, moi = ligne.strip().split()
                self.score = self.etude_un_jeu(opp, moi)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        self._score += s


print(chifoumi('jeu2.dat').score)
