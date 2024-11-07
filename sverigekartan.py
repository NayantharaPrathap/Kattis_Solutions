from collections import deque

def get_landmass(grid, start_row, start_col):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    land_count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
                land_count += 1
    
    return land_count, visited

def update_landmass(grid, visited, row, col):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(row, col)])
    visited[row][col] = True
    land_count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
                land_count += 1
    
    return land_count

def main():
    n = int(input().strip())
    m = int(input().strip())
    q = int(input().strip())
    
    grid = []
    stockholm_pos = (-1, -1)
    
    for i in range(n):
        line = list(input().strip())
        grid.append(line)
        if 'S' in line:
            stockholm_pos = (i, line.index('S'))
            grid[i][line.index('S')] = '#'
    
    # Initial landmass calculation from Stockholm position
    initial_landmass, visited = get_landmass(grid, stockholm_pos[0], stockholm_pos[1])
    print(initial_landmass)
    
    # Handle each query
    for _ in range(q):
        r, c = map(int, input().strip().split())
        r -= 1
        c -= 1
        
        if grid[r][c] == '.':
            # Change water to land
            grid[r][c] = '#'
            
            # Check if it's connected to the existing landmass
            if any(0 <= r + dx < n and 0 <= c + dy < m and visited[r + dx][c + dy] 
                   for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                # Update visited and landmass count
                additional_landmass = update_landmass(grid, visited, r, c)
                initial_landmass += additional_landmass
        
        print(initial_landmass)

if __name__ == "__main__":
    main()
