#PS4b - Convoy

import heapq
from heapq import *

N, K = list(map(int, input().split()))

time_taken = []
people = N

for i in range(N):
    time_taken.append(int(input()))

sorted_time = sorted(time_taken)

sorted_time = sorted_time[0:min(K,N)]

sorted_time = [[i,i,0] for i in sorted_time]

heapify(sorted_time)
#print(sorted_time)

while people > 0:
    t = heappop(sorted_time)
    st = t[0]
    t[0] = t[0] + (2*t[1])
    if t[2] == 0:
        people -= 5
    else:
        people -= 4

    t[2] += 1

    heappush(sorted_time, t)
    #print(sorted_time)

print(st)

