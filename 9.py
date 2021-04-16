def product_special_pythagorean_triplet(x):
    for c in range(x):
        for b in range(c):
            for a in range(b):
                if pow(a, 2) + pow(b, 2) == pow(c, 2) and a + b + c == 1000:
                    return a * b * c


print(product_special_pythagorean_triplet(1000))
