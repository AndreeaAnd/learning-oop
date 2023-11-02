import sys

def sequence_gen(sequence):
    for item in sequence:
        yield item

# Yield intoarce un elem la un moment dat
print(list(sequence_gen([1, 2, 3, 4, 5])))
print(sys.getsizeof(sequence_gen([1, 2, 3, 4, 5])))

# or
# for i in sequence_gen(100):
#     print(i)

squared_nums_gc = (i ** 2 for i in range(1000))
print(sys.getsizeof(squared_nums_gc))
print(list(squared_nums_gc))

# squared_nums_lc = [i**2 for i in range(1000)]
# print(sys.getsizeof(squared_nums_lc))