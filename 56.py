from functools import reduce


def digit_sum(n):
    return sum(map(int, str(n)))


def powerful_digits(a_ceil, b_ceil):
    return [pow(a, b) for a in range(a_ceil) for b in range(b_ceil)]


def greatest_power_digits_sum(a_ceil, b_ceil):
    return reduce(lambda x, y: y if y > x else x, map(digit_sum, powerful_digits(a_ceil, b_ceil)))


print(greatest_power_digits_sum(100, 100))
