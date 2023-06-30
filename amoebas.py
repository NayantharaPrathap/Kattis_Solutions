#Amoebas - Nov Demos

dr = [ 0, 1, 1, 1, 0,-1,-1,-1] # E/SE/S/SW/W/NW/N/NE
dc = [ 1, 1, 0,-1,-1,-1, 0, 1]

def dfs(r, c):
    grid[r][c] = '.' 
    for d in range(8): 
        nr, nc = r+dr[d], c+dc[d]
        if nr < 0 or nr >= m or nc < 0 or nc >= n: continue        
        if grid[nr][nc] != '#': continue 
        dfs(nr, nc) 

m, n = map(int, input().split())

grid = [list(input()) for _ in range(m)]

numCC = 0
for row in range(m):
    for col in range(n):
        if grid[row][col] == '#':  
            numCC += 1
            dfs(row, col)
        
print(numCC)
