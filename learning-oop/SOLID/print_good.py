from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class FaxMixin:
    def fax(self, document):
        print(f'Fax {document}')

class ScanMixin:
        def scan(self, document):
            print(f'Scan {document}')

class OldPrinter(Printer):

    def print(self, document):
        print(f'Printing {document} in black and white')

class ModernPrinter(Printer, FaxMixin, ScanMixin):
    def print(self, document):
        print(f'Printing {document} in color')



mp=ModernPrinter()
mp.fax('some doc')

op=OldPrinter()
op.print('some text')