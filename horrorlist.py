#Horror List - Nov Demos

from collections import deque
from math import inf

N, H, L = map(int, input().split())
horror_list = list(map(int, input().split()))

qe = deque(horror_list)
horror_index = [inf]*N

for i in horror_list:
    horror_index[i] = 0
    
AL = [[] for _ in range(N)]
for _ in range(L):
    a,b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a) #this is for bidirectional
    
while qe: #not empty
    s = qe.popleft()
    
    for t in AL[s]:
        if horror_index[t] != inf:
            continue
        horror_index[t] = horror_index[s] + 1
        qe.append(t)
       
#print(horror_index)
print(horror_index.index(max(horror_index)))
