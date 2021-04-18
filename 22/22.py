from functools import reduce


def parse_names(file_name):
    return sorted(open(file_name, 'r').read().replace("\"", "").split(","))


def score(char, offset):
    return ord(char) + offset


def add(x, y):
    return x + y


def names_score(names):
    return reduce(add,
                  map(lambda name, index: (index + 1) * reduce(add, map(lambda letter: score(letter, -ord("A")), list(name))),
                      names, range(len(names))))


print(names_score(parse_names('names.txt')))
