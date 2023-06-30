def frame(column, letter, character):
    matrix[2][column] = letter
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) + abs(dc) == 2:
                matrix[2 + dr][column + dc] = character

word = input().rstrip()
length = len(word)

matrix = []
for row in range(5):
    matrix.append(['.'] * (4 * length + 1))

for index in range(length):
    frame(4 * index + 2, word[index], '#')
for index in range(2, length, 3):
    frame(4 * index + 2, word[index], '*')

for row in matrix:
    print(''.join(row))