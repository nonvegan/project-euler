from functools import reduce


def pow_digit_sum(base, exp):
    return reduce(lambda x, y: int(x) + int(y), str(pow(base, exp)))


print(pow_digit_sum(2, 1000))
