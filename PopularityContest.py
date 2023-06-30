#Popularity Contest - Nov Demos

n, m = map(int, input().split())

friends = [0] * n
#cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    friends[x - 1] += 1
    friends[y - 1] += 1

print(" ".join((str(cnt - i - 1) for i, cnt in enumerate(friends))))
