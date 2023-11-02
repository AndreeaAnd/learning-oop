import unittest


class MultipleAsserts(unittest.TestCase):
    def test_multiple_asserts(self):
        print('1 == 1')
        self.assertEqual(1, 1)
        print('1 != 2')
        self.assertNotEqual(1, 2)
        print('2 == 2')
        self.assertEqual(2, 2)


class SingleAsserts(unittest.TestCase):

    def test_1(self):
        print('1 == 1')
        self.assertEqual(1, 1)

    def test_2(self):
        print ('1 == 2')
        self.assertEqual (1, 2)


    def test_3(self):
        print('2 == 2')
        self.assertEqual(2, 2)


class ForExample(unittest.TestCase):

    def test_for(self):
        expected_equal = [
            (1, 1),
            (1, 2),
            (2, 2),
            (3, 3),
            (4, 3)
        ]
        for numar_1, numar_2 in expected_equal:
            self.assertEqual(numar_1, numar_2)


unittest.main()