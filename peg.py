peg = [input() for i in range(7)]
count = 0
for i in range(7):
    for j in range(7):
        if peg[i][j] == 'o':
            if j < 5 and peg[i][j+1] == 'o' and peg[i][j+2] == '.':
                count += 1
            if j > 1 and peg[i][j-1] == 'o' and peg[i][j-2] == '.':
                count += 1
            if i < 5 and peg[i+1][j] == 'o' and peg[i+2][j] == '.':
                count += 1
            if i > 1 and peg[i-1][j] == 'o' and peg[i-2][j] == '.':
                count += 1
print(count)