import sys

def sequence_gen(sequence):
    for item in sequence:
        yield item

print(list(sequence_gen([1, 2, 3, 4,5])))
print(sys.getsizeof(sequence_gen([1, 2, 3, 4,5])))

squared_nums_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(squared_nums_gc))
print(squared_nums_gc)
print(list(squared_nums_gc))


