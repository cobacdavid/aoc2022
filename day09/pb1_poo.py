class Position:
    mv = {'R': (1, 0),
          'L': (-1, 0),
          'U': (0, 1),
          'D': (0, -1)}

    @staticmethod
    def distance(pos1, pos2):
        return max(abs(p1 - p2) for p1, p2 in zip(pos1.pos, pos2.pos))

    @staticmethod
    def ajoute(coords1, coords2):
        return [a + b for a, b in zip(coords1, coords2)]

    @staticmethod
    def diff(pos1, pos2):
        # pos1 - pos2
        return [a - b for a, b in zip(pos1.pos, pos2.pos)]

    @staticmethod
    def demi_diff(pos1, pos2):
        # (pos1 - pos2) / 2
        return [(a - b) // 2 for a, b in zip(pos1.pos, pos2.pos)]

    def __init__(self):
        self._pos = [0, 0]

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, xy):
        self._pos = xy

    def bouge(self, choix):
        self._pos = self.ajoute(self._pos, self.mv[choix])


class Corde:
    def __init__(self, fichier):
       self.H = Position()
       self.T = Position()
       self.ens_pos_T = set()
       self.lecture_fichier(fichier)

    def lecture_fichier(self, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                ligne = ligne.strip()
                dr, it = ligne.split()
                self.h_bouge(dr, int(it))

    def h_bouge(self, direction, amplitude):
        for _ in range(amplitude):
            self.H.bouge(direction)
            self._t_vers_h()
            self.ens_pos_T.add(tuple(self.T.pos))

    def _t_vers_h(self):
        if  Position.distance(self.H, self.T) >= 2:
            d = Position.diff(self.H, self.T)
            d = [a//2 if abs(a) == 2 else a for a in d]
            self.T.pos = self.T.ajoute(self.T.pos, d)


c = Corde("jeu2.dat")
print(len(c.ens_pos_T))
