from math import sqrt
P, N = map(int, input().split())
store = []
time = []
player = []
point = []
count = 0
for i in range(N):
    pi, xi, yi, ti = map(int, input().split())
    store.append([pi,xi,yi,ti])
    sorted_store = sorted(store)
    time.append(ti)
    player.append(pi)
    point.append([xi,yi])

for k in range(N):
    for j in range(N):
        if abs(time[k]-time[j])<=10 and (sqrt((point[k][0]-point[j][0])**2 + (point[k][1]-point[j][1])**2)<1000):
            count += 1
        
        if(count!=0):
            print(player[k]," ",player[j])

print(count)
