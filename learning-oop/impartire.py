def impartire(x, y):
    for arg in (x, y):
        if not isinstance(arg, (int, float)):
            raise TypeError(f'Asteptam numar(int sau float), am primit {type(arg).__name__}')
        if y == 0:
            raise ValueError('Numitorul nu poate fi 0')
        return x / y

try:
    print(impartire(2, '2'))
except Exception as error:
    print(error)
