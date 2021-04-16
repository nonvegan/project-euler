def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def n_lattice_combinations_se(size):
    return binomial_coefficient(2 * size, size)


print(n_lattice_combinations_se(20))
