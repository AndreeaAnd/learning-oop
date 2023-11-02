from decorators import *
# @timer
# def time_consumer(nr):
#     for _ in range(nr):
#         sum([i ** 2 for i in range(10000)])
#
# time_consumer(6)

@slow_down
def count_down(from_nr):
    if from_nr < 1:
        print('liftoff')
    else:
        print(from_nr)
        count_down(from_nr - 1)

count_down(5)