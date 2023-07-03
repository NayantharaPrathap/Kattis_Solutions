from math import ceil

h, P = [int(n) for n in input().split()]

d = 0

while 11 * h * d * P / 100000 + ceil(h * d / 8000) * 60 >=\
      60 * h * d * P / 100000 + ceil(h * d / 1000) * 5:
    d += 1

print(d)