import heapq
import sys

INF = float('inf')

def solve():
    # Read input
    n, m, A, B = map(int, input().split())
    
    # Convert to zero-based indices for easier indexing
    A -= 1
    B -= 1
    
    # Graph representation: adjacency list
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, l, e = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, l, e))
        graph[v].append((u, l, e))
    
    # Priority queue: (titans, shamans, path_length, current_node)
    pq = []
    
    # Distances array: dist[village] = (titans, shamans, path_length)
    dist = [(INF, INF, INF) for _ in range(n)]
    
    # Starting at village A
    heapq.heappush(pq, (0, 0, 0, A))  # (titans, shamans, path_length, node)
    dist[A] = (0, 0, 0)
    
    while pq:
        titans, shamans, path_len, u = heapq.heappop(pq)
        
        # If we reached village B, return the result
        if u == B:
            print(path_len, shamans, titans)
            return
        
        # Explore neighbors
        for v, length, enemy in graph[u]:
            # Calculate the number of shamans and titans encountered on this edge
            new_shamans = shamans + (1 if enemy == 1 else 0)
            new_titans = titans + (1 if enemy == 2 else 0)
            new_path_len = path_len + length
            
            # If we found a better path to village `v`, update it
            if (new_titans, new_shamans, new_path_len) < dist[v]:
                dist[v] = (new_titans, new_shamans, new_path_len)
                heapq.heappush(pq, (new_titans, new_shamans, new_path_len, v))
    
    # If we exit the while loop without having reached village B, it's impossible
    print("IMPOSSIBLE")
solve()