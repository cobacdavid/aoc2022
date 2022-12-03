class Chifoumi:
    opposant = {'A': 'R', 'B': 'P', 'C': 'S'}
    gain = {'R': 1, 'P': 2, 'S': 3}
    regles_vers_perdant = {'R': 'S', 'S': 'P', 'P': 'R'}
    regles_vers_gagnant = {'S': 'R', 'P': 'S', 'R': 'P'}

    @classmethod
    def etudie_un_jeu(cls, opp, action):
        choix_opp = cls.opposant[opp]

        if action == 'X':
            choix_moi = cls.regles_vers_perdant[choix_opp]
            score_partie = cls.gain[choix_moi] + 0
        elif action == 'Y':
            score_partie = cls.gain[choix_opp] + 3
        else:
            choix_moi = cls.regles_vers_gagnant[choix_opp]
            score_partie = cls.gain[choix_moi] + 6

        return score_partie

    def __init__(self, fic):
        self._score = 0
        self._lecture_parties(fic)

    def _lecture_parties(self, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                opp, moi = ligne.strip().split()
                self.score = self.etudie_un_jeu(opp, moi)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        self._score += s


print(Chifoumi('jeu2.dat').score)
