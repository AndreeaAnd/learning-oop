class NotaValueError(Exception):
    pass


def calculeaza_media(note):
    total = 0
    nr_note = len(note)

    for nota in note:
        if nota < 1 or nota > 10:
            raise NotaValueError('Nota trebuie sa fie intre 1 si 10')
        total += nota

    return round(total / nr_note, 2)


try:
    print(calculeaza_media([]))
except NotaValueError as e:
    print(e)

except ZeroDivisionError as e:
    print('Va rog sa introduceti o lista cu note')

# print(calculeaza_media([9, 10, 10, -3]))

