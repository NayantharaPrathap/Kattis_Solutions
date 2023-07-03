from math import log2, ceil
 
# Function to return the minimum
# number of steps required
def minOperations(N):
    x = log2(N)
 
    ans = ceil(x)
 
    return ans
 
# Driver Code
if __name__ == '__main__':
    N = 4
    print(minOperations(N))
