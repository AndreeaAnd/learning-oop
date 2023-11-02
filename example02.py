# from decorators import *
# @multiply_by_decorator(2)
# def sum_from_args(*args):
#     """ Gets a variable length arguments and sums them """
#     s=0
#     for n in args:
#         s+=n
#     return s
#
# sequence = [i for i in range(11)]
# my_sum=sum_from_args(*sequence)
# print(my_sum)
#
# print(sum_from_args.__name__)
# print(sum_from_args.__doc__)


from decorators import *
@timer
def sum_from_args(*args):
    """ Gets a variable length arguments and sums them """
    s=0
    for n in args:
        s+=n
    return s

sequence = [i for i in range(1111)]
my_sum=sum_from_args(*sequence)
print(my_sum)

print(sum_from_args.__name__)
print(sum_from_args.__doc__)


