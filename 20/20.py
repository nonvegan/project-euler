from functools import reduce


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def sum_digits(n, base):
    if n == 0:
        return 0
    return reduce(lambda quocient, remainder: remainder + sum_digits(quocient, base), divmod(n, base))


print(sum_digits(factorial(100), 10))
