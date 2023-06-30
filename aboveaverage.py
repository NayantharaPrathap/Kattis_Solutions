#Above Average
import math
C = int(input())

for i in range(C):
    sum = 0
    arr = list(map(int, input().split()))
    N = arr.pop(0)

    for score in arr:
        sum += score
    
    average = sum/len(arr)
    count = 0

    for score in arr:
        if (score > average):
            count += 1

    percentage = (count/len(arr)) * 100

    print("%.3f" % percentage + "%") 
