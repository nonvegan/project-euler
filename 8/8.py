def largest_product_series(number_str, adjacent_digits):
    offset = 0
    largest_product = 0
    while offset <= len(number_str) - adjacent_digits:
        product = 1
        for i in range(offset, offset + adjacent_digits):
            product *= int(number_str[i])
            if product > largest_product:
                largest_product = product
        offset += 1
    return largest_product


print(largest_product_series(open("input.txt", "r").readline(), 13))
