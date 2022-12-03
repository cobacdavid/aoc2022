class Joueur_chifoumi:
    choix_possibles = ('R', 'S', 'P')
    
    def __init__(self):
        self._score = 0
        self._choix = None

    @property
    def score(self):
        return self._score

    def ajoute_score(self, s):
        self._score += s

    @property
    def choix(self):
        return self._choix

    @choix.setter
    def choix(self, c):
        self._choix = c


class Chifoumi:
    gain_type = {'R': 1, 'P': 2, 'S': 3}
    gain_jeu = [0, 3, 6]
    regles = (('R', 'S'), ('S', 'P'), ('P', 'R'))

    def __init__(self, joueur1=None, joueur2=None):
        self._j1 = joueur1
        self._j2 = joueur2

    def fais_un_tour(self):
        choix1 = self._j1.choix
        choix2 = self._j2.choix

        self._j1.ajoute_score(Chifoumi.gain_type[choix1])
        self._j2.ajoute_score(Chifoumi.gain_type[choix2])
        
        if choix1 == choix2:
            self._j1.ajoute_score(Chifoumi.gain_jeu[1])
            self._j2.ajoute_score(Chifoumi.gain_jeu[1])
        elif (choix1, choix2) in Chifoumi.regles:
            self._j1.ajoute_score(Chifoumi.gain_jeu[2])
            self._j2.ajoute_score(Chifoumi.gain_jeu[0])
        else:
            self._j1.ajoute_score(Chifoumi.gain_jeu[0])
            self._j2.ajoute_score(Chifoumi.gain_jeu[2])


def traitement_parties(fichier):
    j1 = Joueur_chifoumi()
    j2 = Joueur_chifoumi()
    jeu = Chifoumi(j1, j2)
    with open(fichier) as fh:
        corr_j1 = {'A': 'R', 'B': 'P', 'C': 'S'}
        corr_j2 = {'X': 'R', 'Y': 'P', 'Z': 'S'}
        for ligne in fh:
            opp, moi = ligne.strip().split()
            j1.choix = corr_j1[opp]
            j2.choix = corr_j2[moi]
            jeu.fais_un_tour()


print(traitement_parties('jeu2.dat'))
