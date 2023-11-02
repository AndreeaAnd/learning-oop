def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'

    return n


if __name__ == '__main__':
    print(fizzbuzz(3))
    print(fizzbuzz(4))
    print(fizzbuzz(5))
    print(fizzbuzz(30))
    print(fizzbuzz(15))