"""
1.
Напишите итератор Fibonacci(n), который генерирует числа Фибоначчи до
n включительно.
"""


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.fib1 = 1
        self.fib2 = 1
        if self.n == 1 or self.n == 0:
            return 1
        else:
            for i in range(2, n):
                fib1, fib2 = self.fib2, self.fib1 + self.fib2
                return fib2
        


"""
2.
Напишите класс, объектом которого будет итератор производящий только
чётные числа до n включительно.
"""


class Even:
    def __init__(self, n, start):
        n.self = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.n:
            return self.start + 2
        else:
            raise StopIteration


"""
3.
Напишите итератор factorials(n), генерирующий последовательность
факториалов натуральных чисел.
"""


class Factorial:
    def __init__(self, n):
        self.n = n
        self.start = 1
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.n:
            self.result *= self.start
            self.start += 1
            return self.result
        else:
            raise StopIteration


"""
4.*
Напишите итератор BinomialCoefficients(n), генерирующий последовательность
биномиальных коэффициентов C0n,C1n,…,Cnn
Запрещается использовать факториалы.
"""


class BinomialCoefficients:
    def __init__(self, n):
        self.n = n
        self.numerator = 1
        self.count = 0
        self.denominator = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.n:
            result = self.numerator // self.denominator
            self.numerator *= (self.n - self.count)
            self.denominator *= (self.count + 1)
            self.count += 1
            return result
        raise StopIteration
