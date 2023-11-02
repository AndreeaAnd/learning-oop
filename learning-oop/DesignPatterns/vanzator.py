class Visitor:
    def visit(self, cladire):
        pass


class Vanzator(Visitor):

    def visit_casa(self, cladire):
        print(f'Vand asigurare PAD catre {cladire}')

    def visit_spital(self, cladire):
        print(f'Vand asigurare spital catre {cladire}')

    def visit_primarie(self, cladire):
        print(f'Vand asigurare primarie catre {cladire}')


class Cladire:
    def accept(self, visitor):
            pass


class Casa(Cladire):
    def accept(self, visitor):
        visitor.visit_casa(self)


class Spital(Cladire):
    def accept(self, visitor):
        visitor.visit_spital(self)


class Primarie(Cladire):
    def accept(self, visitor):
        visitor.visit_primarie(self)


cladiri = [Casa(), Casa(), Spital(), Casa(), Spital(), Primarie()]
vanzator = Vanzator()

print('cladiri', cladiri)
print('vanzator', vanzator)

for cladire in cladiri:
    cladire.accept(vanzator)

