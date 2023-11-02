l = [1, 2, 3, 4]
for x in l:
    print(x)

double = [x*2 for x in l]
print(double)

first, second, third, forth = l

# forth = l[-1]

print('first', first)
print('second', second)
print('third', third)
print('forth', forth)

*_, last = l
print(_) 
print(last)

print('........')
first, second, *_ = l

print(first)
print(second)
print(_)
