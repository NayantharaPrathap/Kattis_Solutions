#Modulo Solitaire
from math import ceil
from math import inf
from heapq import heappush, heappop

def calcrest(mh, ea, eh):
    attacks = ceil (eh / A ) - 1
    rest = mh - ea * attacks
    return rest

A, H = map(int, input().split())
n, m = map(int, input().split())

AL = [[] for _ in range(n)]

for _ in range(m):
    e,b,a,h = map(int, input().split())
    AL[e-1].append((b-1,[a,h]))
    AL[b-1].append((e-1,[a,h]))

cost = [inf for _ in range(n)]
cost[0] = 0
pq = []
heappush(pq, (0, n-1))

while len(pq) > 0:                    
    hpLost, area = heappop(pq)                  
    
    if (hpLost > cost[area]): continue          
    
    for h, w in AL[a]:          
        remainingHP = calcrest(H-hpLost,w[0],w[1])
        newHPLost = H - remainingHP     
        if (cost[area]+newHPLost >= cost[area] or remainingHP <= 0): continue

        cost[area] = cost[area] + newHPLost
        heappush(pq, (cost[area], area))  
    

if cost[n-1] == inf:
    print("Oh no")
else:
    print(H-cost[n-1])
