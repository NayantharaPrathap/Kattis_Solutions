import heapq

n, k = map(int, input().split())
d = {}
arr = map(int, input().split())
for i in arr:
  d[i] = 1 + d.get(i, 0)

li = []
for i in d:
    li.append(-d[i])

heapq.heapify(li)

for _ in range(k):
  t = heapq.heappop(li)
  t += 1
  heapq.heappush(li, t)

print(-heapq.heappop(li))
