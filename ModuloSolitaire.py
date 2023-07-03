#Modulo Solitaire
from math import ceil
from math import inf
from heapq import heappush, heappop

A, H = map(int, input().split())
n, m = map(int, input().split())

AL = [[] for _ in range(V)]

for _ in range(m):
    e,b,a,h = map(int, input().split())
    AL[e].append((a,h))
    AL[b].append((a,h))

cost = [inf for _ in range(n)]
cost[0] = 0
pq = []
heappush(pq, (0, s))

while (len(pq) > 0):                    
    d, a = heappop(pq)                  
    if (d > dist[a]): continue          
    for h, w in AL[a]:                  
        if (dist[a]+h >= dist[a]): continue
        dist[h] = dist[a]+e
        heappush(pq, (dist[h], h))  
    
def calcrest(mh, ea, eh):
    attack = eh / A + (eh % A)
    rest = mh - ea * (attack - 1)
    return rest
