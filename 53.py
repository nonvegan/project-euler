def n_combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def count_combinations_gt(n_ceiling, floor):
    return sum(map(lambda x: x > floor, [n_combinations(n, r) for n in range(n_ceiling + 1) for r in range(n + 1)]))


print(count_combinations_gt(100, 1000000))
