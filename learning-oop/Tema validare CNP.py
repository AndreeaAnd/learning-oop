"""
Validare CNP
Validarea oricărui CNP se realizează prin calcularea cifrei de control. Dacă cifra de control calculată este egală cu
cea specificată în CNP, atunci codul numeric personal este valid și corect.
Algoritmul de calculare a cifrei de control folosește următoarele 12 cifre: 279146358279. Fiecare cifra din constantă
este înmulțită cu cifra corespondentă din CNP. De exemplu, dacă prima cifră din CNP-ul persoanei este 1 (1 semnifică
persoana de sex masculin născută între 1900-1999), aceasta este înmulțită cu prima cifră din constantă adică 2.
Rezultatele înmulțirilor sunt însumate, iar numărul rezultat se împarte la 11.
Dacă restul împărțirii este mai mic decât 10, atunci acel număr reprezintă cifra de control, cea de 13-a cifra a CNP-ului.
În schimb, dacă restul împărțirii este 10, atunci cifra de control este 1.
Să luăm de exemplu următorul CNP: 2990219469000. În cazul de față trebuie sa vedem dacă cifra de control pe care o
calculam este egala cu 0. Dacă rezultatul nu este 0, atunci CNP-ul este incorect.
Vom înmulți fiecare dintre primele 12 cifre ale CNP-ului cu valoarea constantă corespunzătoare.
Implementati un program care valideaza un CNP, si in cazul in care nu este valid ridicati exceptii:
Daca CNP-ul nu are exact 13 cifre
Daca cifra de control este gresita

"""


class InvalidCnpError(ValueError):
    pass


def control_number(CNP):
    result_1=int(CNP[0]) * 2
    result_2 = int(CNP[1]) * 7
    result_3 = int(CNP[2]) * 9
    result_4 = int(CNP[3]) * 1
    result_5 = int (CNP[4]) * 4
    result_6 = int (CNP[5]) * 6
    result_7 = int (CNP[6]) * 3
    result_8 = int (CNP[7]) * 5
    result_9 = int (CNP[8]) * 8
    result_10 = int (CNP[9]) * 2
    result_11 = int (CNP[10]) * 7
    result_12 = int (CNP[11]) * 9

    sums = result_1 + result_2 + result_3 + result_4 + result_5 + result_6 + result_7 + result_8 + result_9 + result_10 + result_11 + result_12

    if sums % 11 == int(CNP[12]):
        return True
    else:
        return False


def CNP_validator(CNP):
    if len(CNP) != 13:
        raise InvalidCnpError('CNP-ul trebuie sa aiba 13 caractere')
    if not control_number(CNP):
        raise InvalidCnpError('cifra de control a CNP-ului este gresita')
    else:
        return 'CNP-ul introdus este corect'


CNP_input=input('Introduceti CNP-ul: ')

try:
    print(CNP_validator(CNP_input))
except InvalidCnpError as e:
    print(e)

