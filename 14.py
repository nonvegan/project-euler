def longest_collatz_sequence_starting_num(max):
    largest_n = largest_counter = 1
    for i, n in zip(range(1, max), range(1, max)):
        counter = 1
        while i != 1:
            i = 3 * i + 1 if i % 2 else i // 2
            counter += 1
        if counter > largest_counter:
            largest_n = n
            largest_counter = counter
    return largest_n


print(longest_collatz_sequence_starting_num(1000000))
