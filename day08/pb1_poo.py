class Foret:

    def __init__(self, fichier):
        self._foret = []
        self._lecture_foret(fichier)
        self.largeur = len(self._foret[0])
        self.hauteur = len(self._foret)

    def _lecture_foret(self, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                ligne = ligne.strip()
                rang = []
                for h in ligne:
                    rang.append(int(h))
                self._foret.append(rang)

    def visible(self, li, co):
        arbre = self._foret[li][co]
        d = g = h = b = True

        # à droite
        co_act = co + 1
        while d and co_act < self.largeur:
            d = arbre > self._foret[li][co_act]
            co_act += 1
        # à gauche
        co_act = co - 1
        while g and co_act >= 0:
            g = arbre > self._foret[li][co_act]
            co_act -= 1
        # en haut
        li_act = li - 1
        while h and li_act >= 0:
            h = arbre > self._foret[li_act][co]
            li_act -= 1
        # en bas
        li_act = li + 1
        while b and li_act < self.hauteur:
            b = arbre > self._foret[li_act][co]
            li_act += 1

        return d or g or h or b

    def nb_arbres_visibles(self):
        n = 0
        # tab = []
        for li in range(self.hauteur):
            # rang = []
            for co in range(self.largeur):
                v = self.visible(li, co)
                n += 1 if v else 0
                # rang.append(v)
            # tab.append(rang)
        return n #, tab


f = Foret("jeu2.dat")
print(f.nb_arbres_visibles())
