class Purchaser:
    suma_maxima = 0

    def __init__(self, nume, superior=None):
        self.nume=nume
        self.superior=superior

    def aproba_buget(self, suma):
        if suma < self.suma_maxima:
            print(f'{self} Aprob {suma}')
        else:
            print(f'{self} Nu pot aproba {suma}, te trimit la superior {self.superior}')
            self.superior.aproba_buget(suma)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.nume}'


class Manager(Purchaser):
    suma_maxima = 200


class Director(Purchaser):
    suma_maxima = 500


class VP(Purchaser):
    suma_maxima = 1000


class CEO(Purchaser):
    def aproba_buget(self, suma):
            print(f'{self} Aprob {suma}')


Florin = CEO('Florin')
Vasile = VP('Vasile', superior=Florin)
Anamaria = Director('Anamaria', superior=Vasile)
Andrei = Manager('Andrei', superior=Anamaria)

Andrei.aproba_buget(10000)
Andrei.aproba_buget(500)
