def main():
    import sys
    input = sys.stdin.read
    from collections import deque
    
    data = input().split()
    
    idx = 0
    
    r = int(data[idx])
    c = int(data[idx + 1])
    idx += 2
    
    grid = []
    for _ in range(r):
        grid.append(data[idx])
        idx += 1
    
    n = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(n):
        r1 = int(data[idx]) - 1
        c1 = int(data[idx + 1]) - 1
        r2 = int(data[idx + 2]) - 1
        c2 = int(data[idx + 3]) - 1
        queries.append((r1, c1, r2, c2))
        idx += 4
    
    # Directions for moving north, south, east, west
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Function to perform BFS and label components
    def bfs(start_r, start_c, comp_id):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = comp_id
        comp_type = grid[start_r][start_c]
        
        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0 <= new_r < r and 0 <= new_c < c and visited[new_r][new_c] == -1 and grid[new_r][new_c] == comp_type:
                    visited[new_r][new_c] = comp_id
                    queue.append((new_r, new_c))
    
    # Mark all components
    visited = [[-1] * c for _ in range(r)]
    comp_id = 0
    
    for i in range(r):
        for j in range(c):
            if visited[i][j] == -1:
                bfs(i, j, comp_id)
                comp_id += 1
    
    # Answer each query
    results = []
    for r1, c1, r2, c2 in queries:
        if visited[r1][c1] == visited[r2][c2]:
            if grid[r1][c1] == '0':
                results.append("binary")
            else:
                results.append("decimal")
        else:
            results.append("neither")
    
    # Print results
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
