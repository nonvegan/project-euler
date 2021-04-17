def first_n_digits_fib_number(digits):
    index, curr, prev = 1, 1, 0
    while curr < pow(10, digits - 1):
        index, curr, prev, = index + 1, curr + prev, curr
    return index


print(first_n_digits_fib_number(1000))
