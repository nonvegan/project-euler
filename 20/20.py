def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def sum_digits(n):
    return 0 if n == 0 else n % 10 + sum_digits(n // 10)


print(sum_digits(factorial(100)))
