S, N = map(int, input().split())
seats = [0 for i in range(S)]
not_empty = [int(i) for i in input().split()]
for s in not_empty:
    seats[s-1] = 1
counter = 0
for i in range(S):
    if i == 0:
        if seats[i+1] == 0 and seats[i] != 1 and seats[-1] != 1:
            seats[i] = 1
            counter += 1
    elif i == S-1:
        if seats[i] == 0 and seats[i-1] != 1 and seats[0] != 1:
            seats[i] = 1 
            counter += 1
    else:
        if seats[i] == 0 and seats[i-1] != 1 and seats[i+1] != 1:
            seats[i] = 1 
            counter += 1
print(counter)
