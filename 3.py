from math import sqrt


def highest_prime_factor(n):
    h = 2
    while n % 2 == 0:
        n /= 2
    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            n /= i
            h = i
    if n != 1:
        h = n
    return h


print(highest_prime_factor(600851475143))
