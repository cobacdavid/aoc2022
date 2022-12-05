import re


class Stack:
    def __init__(self):
        self._pile = []

    def sommet(self):
        return self._pile[-1]

    def empiler(self, e):
        self._pile.append(e)

    def depiler(self):
        return self._pile.pop()

    def inverser(self):
        P = Stack()
        for _ in range(len(self)):
            P.empiler(self.depiler())
        self._pile = P._pile

    def __len__(self):
        return len(self._pile)

    def __str__(self):
        s = ""
        for crate in self._pile:
            s += crate.contenu
        return s


class Crate:
    def __init__(self, c):
        self._contenu = c

    @property
    def contenu(self):
        return self._contenu

    @contenu.setter
    def contenu(self, c):
        self._contenu = c


class Cargo:
    def __init__(self, fichier):
        self._lst_piles = []
        self._mvts = []
        with open(fichier) as fh:
            def_piles = True
            for ligne in fh:
                if len(self._lst_piles) == 0:
                    n_stacks = len(ligne) // 4
                    for _ in range(n_stacks):
                        self.ajoute_pile()
                if def_piles and len(ligne) != 1:
                    if ligne[1] == "1":
                        def_piles = False
                        for pile in self._lst_piles:
                            pile.inverser()
                    else:
                        for i in range(n_stacks):
                            j = i * 4 + 1
                            if ligne[j] != " ":
                                cr = Crate(ligne[j])
                                self._lst_piles[i].empiler(cr)
                elif len(ligne) > 1:
                    m = re.search("move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)",
                                  ligne)
                    self.move(int(m[1]), int(m[2]), int(m[3]))

    def ajoute_pile(self):
        self._lst_piles.append(Stack())

    def _from_to(self, i, j):
        element = self._lst_piles[i-1].depiler()
        self._lst_piles[j-1].empiler(element)

    def move(self, n, i, j):
        for _ in range(n):
            self._from_to(i, j)

    def sommets(self):
        message = ""
        for pile in self._lst_piles:
            message += pile.sommet().contenu if len(pile) >= 1 else " "
        return message

    def __str__(self):
        s = ""
        for pile in self._lst_piles:
            s += str(pile) + "\n"
        return s


c = Cargo("jeu2.dat")
print(c.sommets())
