def depth_first_search(u):
    visited[u] = True
    for v in AL[u]:
        if visited[v]: continue
        depth_first_search(v)
        
for i in range(int(input())):
    Vertices = int(input())
    Edges = int(input())
    AL = [[] for i in range(Vertices)]
    for i in range(Edges):
        u,v = map(int, input().split())
        AL[u].append(v)
        AL[v].append(u)
        
    num_of_CC = 0
    
    visited = [False] * Vertices
    for u in range(Vertices):
        if not visited[u]:
            num_of_CC += 1
            depth_first_search(u)
    
    print(num_of_CC - 1)