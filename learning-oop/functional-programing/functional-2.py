# def pure_multiplication_by_2(numbers):
#     return [number * 2 for number in numbers]
#
#
# input_numbers = [1, 2, 3, 4, 5]
# # print(pure_multiplication_by_2([1, 2, 3, 4, 5]))
# print(pure_multiplication_by_2(input_numbers))
# print(input_numbers)


def write_error(error, count, action):
    for i in range(count):
        action(error)


write_error('Eroare', 5, print)
