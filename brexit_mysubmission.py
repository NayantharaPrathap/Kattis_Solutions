import math
from collections import deque

c, p, x, l = map(int, input().split())

AL = dict()
for i in range(p):
    a, b = map(int, input().split())
    if a not in AL:
      AL[a] = []
    AL[a].append(b)
    if b not in AL:
      AL[b] = []
    AL[b].append(a)

visited = dict()
for v in AL:
    visited[v] = math.ceil(len(AL[v]) / 2)

visited[l] = 0
queue = deque([l])
while queue:
    current = queue.popleft()
    #print(current)
    for edge in AL[current]:
      visited[edge] -= 1
      if visited[edge] == 0:
        queue.append(edge)

if visited[x] <= 0:
    print('leave')
else:
    print('stay')