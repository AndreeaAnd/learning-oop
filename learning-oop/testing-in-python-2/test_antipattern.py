import unittest

# sa nu folosim aceeasi variabila in teste


class PassingState(unittest.TestCase):
    def test_1(self):
        self.value = 10
        self.assertTrue(True)

    def test_2(self):
        self.assertEqual(self.value, 10)


unittest.main()
