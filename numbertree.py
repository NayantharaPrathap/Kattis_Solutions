from functools import reduce

line = open(0).readline().split()

H = int(line[0])
path = line[1] if len(line) == 2 else ''

n = reduce(lambda n, d: n * 2 + (d == 'R'), path, 1)

print(2 ** (H + 1) - n)