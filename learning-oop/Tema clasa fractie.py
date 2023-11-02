"""
Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
○ __init__ : instanțiem numărător și numitor
○ __str__ : afisam "numărător/numitor"
○ __add__ : returnam o noua fractie care reprezinta adunarea
○ __sub__: returnam o nouă fracție care reprezinta scădearea
○ inverse: returnează o nouă fracție (inversa fracției)

"""


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        return Fractie(self.numarator + other.numarator, self.numitor + other.numitor)

    def __sub__(self, other):
        return Fractie(self.numarator - other.numarator, self.numitor + other.numitor)

    def inverse(self):
        return f'{self.numitor}/{self.numarator}'


prima_fractie = Fractie(2, 4)
a_doua_fractie = Fractie(1, 2)

print('Fractie', prima_fractie)
print('Fractie adunata cu doi', prima_fractie + a_doua_fractie)
print('Fractie scazuta cu patru', prima_fractie - a_doua_fractie)
print('Inversa fractiei', prima_fractie.inverse())

