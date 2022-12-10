class Cpu:
    stop_cycles = [20 + 40*n for n in range(6)]

    def __init__(self, fichier):
        self._x = 1
        self._c_mul_x = 0
        self._cycle = 0
        self.lecture_fichier(fichier)

    @property
    def cumul_cx(self):
        return self._c_mul_x

    def lecture_fichier(self, fichier):
        with open(fichier) as fh:
            for ligne in fh:
                ligne = ligne.strip()
                l = ligne.split()
                if l[0] == "noop":
                    self.noop()
                else:
                    self.addx(int(l[1]))

    def actualise_x(self, x):
        if self._cycle in Cpu.stop_cycles:
            self._c_mul_x += self._cycle * self._x
        self._x += x

    @property
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, x):
        self._cycle += 1
        self.actualise_x(x)

    def noop(self):
        self.cycle = 0

    def addx(self, x):
        self.cycle = 0
        self.cycle = x


c = Cpu("jeu2.dat")
print(c.cumul_cx)
