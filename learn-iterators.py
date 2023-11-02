l = [1, 2, 3, 4]
for x in l:
    print(x)

double = [x*2 for x in l]
print(double)

first, second, third, forth = l

print('first', first)
print('second', second)
print('third', third)
print('forth', forth)

# ia toate elementele pana la ultimul; *_ => nu le foloseste
*_, last = l
print(_)
print(last)

first, second, *_ = l
print(first)
print(second)
print(_)