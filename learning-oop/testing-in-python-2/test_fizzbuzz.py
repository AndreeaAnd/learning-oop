import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_3_returns_fizz(self):
        value = 3
        result = fizzbuzz(value)
        self.assertEqual(result, 'Fizz')

    def test_5_returns_buzz(self):
        value = 5
        result = fizzbuzz(value)
        self.assertEqual(result, 'Buzz')

    def test_15_returns_fizz(self):
        value = 15
        result = fizzbuzz(value)
        self.assertEqual(result, 'FizzBuzz')

    def test_4_returns_4(self):
        value = 4
        result = fizzbuzz(value)
        self.assertEqual(result, value)

    def test_a_raises_exception(self):
        value = 'a'
        with self.assertRaises(TypeError):
            fizzbuzz('a')


unittest.main()

