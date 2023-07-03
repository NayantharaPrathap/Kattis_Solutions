#Illuminati Spotti - PS6 A

#def countingTriangle(g, isDirected):
#    nodes = len(g)
n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())

mat = [[int(lst[x][y]) for x in range (n)] for y in range(n)]
 
count_Triangle = 0
nodes = n
     
    # Considering all possible triplets of edges in graph
for i in range(nodes):
    for j in range(i+1,nodes):
        for k in range(j+1,nodes):
                
            if(mat[i][j] == mat[j][k] == mat[k][i] == 1):
                count_Triangle += 1
                
print(count_Triangle)
    # If graph is directed , division is done by 3 else division by 6 is done
'''
    if isDirected:
      return count_Triangle//3 
    else: return count_Triangle//6
'''

#print(countingTriangle(mat, False))
