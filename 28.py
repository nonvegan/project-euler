size = 1001
x = y = size // 2
matrix = [[0 for a in range(size)] for b in range(size)]
matrix[x][y] = c = 1
i = 0

while c < pow(size, 2):
    x += 1
    c += 1
    matrix[y][x] = c
    for j in range(2 * i + 1):
        y += 1
        c += 1
        matrix[y][x] = c
    for j in range(2 * i + 2):
        x -= 1
        c += 1
        matrix[y][x] = c
    for j in range(2 * i + 2):
        y -= 1
        c += 1
        matrix[y][x] = c
    for j in range(2 * i + 2):
        x += 1
        c += 1
        matrix[y][x] = c
    i += 1

sum = -1
for a in range(size):
    sum += matrix[a][a]
    sum += matrix[size - 1 - a][a]

print(sum)
