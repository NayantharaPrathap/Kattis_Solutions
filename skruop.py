v = 7

n = int(input())

for _ in range(n):
    if input() == 'Skru op!':
        v = min(v + 1, 10)

    else:
        v = max(v - 1, 0)

print(v)