def smallest_multiple(a, b):
    num = 1
    devisor = a
    while devisor <= b:
        if num % devisor != 0:
            num += devisor - 1
            devisor = a
            continue
        devisor += 1
    return num


print(smallest_multiple(1, 8))
