def parse_rows(file_name):
    return list(map(lambda x: list(map(lambda y: int(y), x.split())), open(file_name, 'r').read().splitlines()))


def max_adjacent_path_sum(rows):
    index = 0
    sum = rows[index][index]
    for row in rows[1:]:
        if row[index + 1] > row[index]:
            index += 1
        sum += row[index]
    return sum


print(max_adjacent_path_sum(parse_rows('input.txt')))
