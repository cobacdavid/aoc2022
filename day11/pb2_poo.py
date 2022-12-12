import re
import operator


class Monkey:
    items = {}
    lst_mky = []
    fct = {"+": operator.add,
           "-": operator.sub,
           "*": operator.mul}
    le_mod = 1

    @classmethod
    def lecture_fichier(cls, fichier):
        with open(fichier) as fh:
            for i, ligne in enumerate(fh):
                ligne = ligne.strip()
                reste = i % 7
                if reste == 0:
                    cur_id_monk = int(re.search("\w+\s(\d)+:", ligne).group(1))
                    cur_monk = cls(cur_id_monk)
                    cls.lst_mky.append(cur_monk)
                    cls.items[cur_id_monk] = []
                elif reste == 1:
                    cdc_nb = ligne.split(":")[1].split(',')
                    lst_nb = map(int, cdc_nb)
                    cls.items[cur_id_monk].extend(lst_nb)
                elif reste == 2:
                    op = ligne.split("=")[1]
                    cur_monk._symb = op[5:6]
                    cur_monk._opd = op[7:]
                elif reste == 3:
                    cur_monk._test = int(ligne.split("by")[1])
                    cls.le_mod *= cur_monk._test
                elif reste == 4:
                    cur_monk._to[True] = int(ligne.split("monkey")[1])
                elif reste == 5:
                    cur_monk._to[False] = int(ligne.split("monkey")[1])

    def __init__(self, idt):
        self._idt = idt
        self._ops = 0
        self._symb = None
        self._opd = 0
        self._test = 1
        self._to = {True: None, False: None}

    @property
    def ops(self):
        return self._ops

    def _operation(self, item, cdc_op, opd):
        opd = item if opd == "old" else int(opd)
        return self.fct[cdc_op](item, opd)

    def traitement(self):
        liste_items = Monkey.items[self._idt]
        while len(liste_items) != 0:
            self._ops += 1
            item = liste_items.pop(0)
            item = self._operation(item, self._symb, self._opd)
            item = item % self.le_mod
            bool_test = item % self._test == 0
            Monkey.items[self._to[bool_test]].append(item)


Monkey.lecture_fichier("jeu2.dat")
for _ in range(10_000):
    for m in Monkey.lst_mky:
        m.traitement()
lst_ops = []
for m in Monkey.lst_mky:
    lst_ops.append(m.ops)
lst_ops.sort()
print(lst_ops[-2] * lst_ops[-1])
