import unittest
from calculate_credit import Calculator

class Test_calc(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.sum = Calculator.sum
        self.mult = Calculator.mult

    def test_correctness(self):
        self.assertEqual(self.sum(5, 8), 13, 'Неверные вычисления')

    def test_correctness2(self):
        self.assertEqual(self.mult(9, 7), '63', 'Неверные вычисления')

    def test_correctness3(self):
        self.assertEqual(self.sum(9, 9), 18, 'Неверные вычисления')

    def test_correctness4(self):
        self.assertEqual(self.mult(5, 56), 61, 'Неверные вычисления')

if __name__ == '__main__':
    unittest.main()