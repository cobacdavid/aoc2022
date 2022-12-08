class Rep:
    liste_rep = []

    def __init__(self, nom):
        self._nom = nom
        self._taille = 0
        self.liste_rep.append(self)
        # self.trie(self)

    @property
    def taille(self):
        return self._taille

    @taille.setter
    def taille(self, t):
        self._taille += t


class Parser:
    def __init__(self):
        self._pile = []
        self._rep_courant = None

    def cd(self, nom):
        if nom != "..":
            rep = Rep(nom)
            self._rep_courant = rep
            self._pile.append(rep)
        else:
            self._pile.pop()
            self._rep_courant = self._pile[-1]

    def ls(self, chaine):
        if chaine[:3] != "dir":
            taille = int(chaine.split()[0])
            for r in self._pile:
                r.taille = taille


p = Parser()
with open("jeu2.dat") as fh:
    for ligne in fh:
        ligne = ligne.strip()
        #
        if ligne[0] == "$":
            ls_en_cours = False
            cmd = ligne[2:4]
            #
            if cmd == "cd":
                p.cd(ligne[5:])
            elif cmd == "ls":
                ls_en_cours = True
        else:
            p.ls(ligne)

Rep.liste_rep.sort(key=lambda r: r.taille)
restant = 70_000_000 - Rep.liste_rep[-1].taille
a_liberer = 30_000_000 - restant
i = 0
while i < len(Rep.liste_rep) and Rep.liste_rep[i].taille < a_liberer:
    i += 1
print(Rep.liste_rep[i].taille)
