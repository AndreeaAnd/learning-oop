from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f'Printing {document} in black and white')

    def fax(self, document):
        raise NotImplementedError('Fax is not supported')

    def scan(self, document):
        raise NotImplementedError('Scan is not supported')


class ModernPrinter(Printer):
    def print(self, document):
        print(f'Printing {document} in color')

    def fax(self, document):
        print(f'Fax {document}')

    def scan(self, document):
        print(f'Scan {document}')


op=OldPrinter()
op.fax('some text')

mp=ModernPrinter()
mp.fax('some doc')