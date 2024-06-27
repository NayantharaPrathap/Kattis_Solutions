import math

n = int(input())
result = 0
if n < 17: 
    for i in range(0, n + 1):
        result += 1/(math.factorial(i))
else:
    result = 2.7182818284590455
print(result)