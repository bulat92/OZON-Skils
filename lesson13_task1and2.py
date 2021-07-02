from calculate_credit import calculate_credit as func
import unittest

class Test_calculate_credit(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(func(5, 6, 8), 2, 'Неверные вычисления')

    def test_correctness2(self):
        self.assertEqual(func(9, 8, 7), '6', 'Неверные вычисления')

    def test_correctness3(self):
        self.assertEqual(type(func(9, 9, 9)), int, 'Неверные вычисления')

    def test_correctness4(self):
        self.assertEqual(func(5, 5, 56), 'два', 'Неверные вычисления')

