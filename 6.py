def sum_pow(a, b):
    if a == 1:
        return 1
    return pow(a, b) + sum_pow(a - 1, b)


def pow_sum(a, b):
    return pow(sum(a), b)


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


def sum_square_diff(a, b):
    return pow_sum(a, b) - sum_pow(a, b)


print(sum_square_diff(100, 2))
