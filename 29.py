def distinc_powers(start, end):
    numbers = []
    for a in range(start, end):
        for b in range(start, end):
            numbers.append(pow(a, b))
    return len(set(numbers))


print(distinc_powers(2, 101))
