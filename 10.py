from math import ceil, sqrt


def get_primes_up_to_n_using_list(n):
    prime_candidates = [False] * 2 + [True] * (n - 2)
    for i in range(2, ceil(sqrt(n))):
        if prime_candidates[i]:
            for j in range(2 * i, n, i):
                prime_candidates[j] = False
    return [candidate for candidate, is_prime in enumerate(prime_candidates) if is_prime]


def get_primes_up_to_n_using_set(n):
    primes = set(range(2, n))
    for prime_candidate in primes.copy():
        if prime_candidate in primes:
            for remove_prime in range(2 * prime_candidate, n, prime_candidate):
                if remove_prime in primes:
                    primes.remove(remove_prime)
    return primes


print(sum(get_primes_up_to_n_using_list(2000000)))
print(sum(get_primes_up_to_n_using_set(2000000)))  # 7x slower
