import unittest
<<<<<<< HEAD
from homework import Fibonacci, Even, Factorial
=======
from homework import BinomialCoefficients
>>>>>>> 23d2fe501332147611b17b00552e44e8c6375e4a


class HomeworkTest(unittest.TestCase):
    def test_binom(self):
        self.assertEqual(list(BinomialCoefficients(0)), [1])
        self.assertEqual(list(BinomialCoefficients(1)), [1, 1])
        self.assertEqual(list(BinomialCoefficients(5)), [1, 5, 10, 10, 5, 1])

    def Fibonacci_test(self):
        _list = list(Fibonacci(8))
        self.assertEqual(_list, [0, 1, 1, 2, 3, 5, 8, 13])
        _list = list(Fibonacci(10))
        self.assertEqual(_list, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def Even_test(self):
        _list = list(Even(10))
        self.assertEqual(_list, [2, 4, 6, 8, 10])
        _list = list(Even(12))
        self.assertEqual(_list, [2, 4, 6, 8, 10, 12])

    def Factorial_test (self):
        _list = list(Factorial(6))
        self.assertEqual(obj, [1, 2, 6, 24, 120, 720])
        _list= list(Factorial(9))
        self.assertEqual(obj, [1, 2, 6, 24, 120, 720, 5040, 40320, 362880])


if __name__ == '__main__':
    unittest.main()
