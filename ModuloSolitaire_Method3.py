#Modulo Solitaire - Method 3

from math import inf
from heapq import heappush, heappop

M, N, S = map(int, input().split())
AM = [list(map(int, input().split())) for _ in range(M)]

dist = [inf]*M
dist[S] = 0
pq = [(dist[S], S)]
