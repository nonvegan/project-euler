from math import sqrt, ceil


def is_prime(n):
    if 1 < n < 4:
        return True
    if not n % 2 or not n % 3:
        return False
    for i in range(5, ceil(sqrt(n) + 1)):
        if not n % i:
            return False
    return True


def nth_prime(n):
    current, count, candidate, step = 3, 2, 5, 2
    while count < n:
        if is_prime(candidate):
            current, count = candidate, count + 1
        candidate, step = candidate + step, 6 - step
    return current


print(nth_prime(10001))
