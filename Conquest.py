#PS-7B - Conquest

import heapq

N,M = map(int, input().split())

nation = {i:[] for i in range(1, N+1)}

for i in range(M):
    u, v = map(int, input().split())
    nation[u].append(v)
    nation[v].append(u)

arr = [0]
for i in range(N): arr.append(int(input()))

#R = int(input())
a = 1

spanningarmy = arr[a]
visited = [False]*(N+1)
visited[a] = True

x = [(arr[i], i) for i in nation[a]]
heapq.heapify(x)

while x:
    nextnode = heapq.heappop(x)
    if visited[nextnode[1]]:
        continue
    if nextnode[0] >= spanningarmy:
        break

    visited[nextnode[1]] = True
    spanningarmy += arr[nextnode[1]]
    
    for n in nation[nextnode[1]]:
        heapq.heappush(x, (arr[n], n))

print(spanningarmy)
