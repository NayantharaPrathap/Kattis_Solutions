#Modulo Solitaire - 2nd Method
from heapq import heappush, heappop
from math import inf

M, N, S = map(int, input().split())
lst = []
s1 = []

##if M+N+S == 0:
##    break
for _ in range(N):
    s1 = list(map(int, input().split()))
    #s1 = set(a,b)
    lst.append(s1)
#print(lst)
dist = [inf]*M
dist[S] = 0

pq = []
heappush(pq, S)

while pq:
    x = heappop(pq)
    
    for i in range(N):
        y = (x * lst[i][0] + lst[i][1])%M
        if y == inf:
            continue
        if dist[y]!=-1:
            continue
        else:
            dist[y] = dist[x]+1
            heappush(pq,y)
    if x == 0:
        print(dist[0])
        

print(-1)
