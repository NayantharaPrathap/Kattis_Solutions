dr = [ 0, 1, 1, 1, 0,-1,-1,-1] # E/SE/S/SW/W/NW/N/NE
dc = [ 1, 1, 0,-1,-1,-1, 0, 1]

def depth_first_search(r, c): #DFS algo
    patterngrid[r][c] = '.' 
    for d in range(8): 
        nr, nc = r+dr[d], c+dc[d]
        if nr < 0 or nr >= m or nc < 0 or nc >= n: continue        
        if patterngrid[nr][nc] != '#': continue 
        depth_first_search(nr, nc) 

m, n = map(int, input().split())
patterngrid = [list(input()) for _ in range(m)] #scan m rows and chop each row to list of chars

no_of_CC = 0
for row in range(m):
    for col in range(n):
        if patterngrid[row][col] == '#':  
            no_of_CC += 1
            depth_first_search(row, col)
        
print(no_of_CC)