def self_powers_sum(n):
    return sum(pow(x, x) for x in range(1, n + 1))


def last_digits(num, digits):
    return str(num)[-digits:]


print(last_digits(self_powers_sum(1000), 10))
