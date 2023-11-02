"""
Creati o metoda de validare a numelui unei persoane.
Restrictiile sunt:
   - trebuie sa inceapa cu litera mare
   - trebuie sa fie maxim 25 de caractere
   - trebuie sa nu contina caractere speciale (!@#$%^&*() )
Creati exceptii pentru fiecare tip de eroare pornind de la urmatorul cod:
class NameInvalidException(ValueError):
     pass
Pentru cazul 1 (numele nu incepe cu litera mare), ca modalitate de tratare a exceptiei inlocuiti valoarea folosind
una din metodele title/upper de pe string.

"""


class NameInvalidException(ValueError):
    pass


nume = input('Numele meu este: ')


def validare_nume(nume):
    caractere_speciale = ['!', '@', '#', '$', '%', '^', '&', '*', '()']
    if len(nume) > 25:
        raise NameInvalidException('numele trebuie nu depaseasca 25 de caractere')
    for i in nume:
        if i in caractere_speciale:
            raise NameInvalidException('numele nu trebuie sa contina caractere speciale precum !@#$%^&*()')
        else:
            pass
    if not nume[0].isupper():
        # return f'numele trebuie sa inceapa cu litera mare'
        return f'Numele meu este: {nume.title()}'
    else:
        return f'Numele meu este: '


try:
    print(validare_nume(nume))
except ValueError as e:
    print(e)
