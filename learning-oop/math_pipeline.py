def to_square(numbers):
    return (numbers ** 2 for number in numbers)

def to_cube(numbers):
    return (numbers ** 3 for number in numbers)

def to_even(numbers):
    return (number for number in numbers if number % 2 == 0)
def to_odd(numbers):
    return (number for number in numbers if number % 2 != 0)

def to_str(numbers):
    return (str(number) for number in numbers )

