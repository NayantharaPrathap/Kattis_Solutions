#initial code
'''
conc = set()
for i in range(int(input())):
    assum, concl = map(input().split('->'))
    for x in assum.strip().split():
        if not x in conc:
            print(x+1)
            exit()
    conc.add(concl.strip())
    
print('correct')
'''

#final correct code
n = int(input())
trips = {}
for i in range(0, n):
    ab = input().split()
    a = ab[0]
    b = int(ab[1])
    if a not in trips:
        trips[a] = []
    trips[a].append(b)
for _,val in trips.items():
    val.sort()
k = int(input())
for k in range(0, k):
    ab = input().split()
    a = ab[0]
    b = int(ab[1])
    print(trips[a][b-1])
