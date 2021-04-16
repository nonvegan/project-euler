from functools import reduce


def first_digits_large_sum(file_name, digits):
    numbers = list(map(lambda x: int(x.rstrip('\n')), open(file_name, 'r').readlines()))
    sum = reduce(lambda x, y: x + y, numbers)
    return str(sum)[:digits]


print(first_digits_large_sum('input.txt', 10))
