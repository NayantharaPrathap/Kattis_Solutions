n, m = map(int, input().split())
result = (n * (n - 1)) // 2

dic = set()
lst = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if (j+i) not in dic:
            lst.append((i,j))
            dic.add(i+j) 
        
        if len(lst) == m:
            break

    if len(lst) == m:
        break

if len(lst)<m or m>result or m < n-1:
    print(-1)
else:
    for l in lst:
        print(l[0], l[1])