from decorators import *

@sum_decorator
def sum_from_args(*args):
    s=0
    for n in args:
        s+=n
    return s

sequence = [i for i in range(11)]
my_sum=sum_from_args(*sequence)
print(my_sum)

