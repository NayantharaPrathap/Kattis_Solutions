#Method 1 - TLE in test case 2
'''
n, m = input().split()
while(int(n)!=0 and int(m)!=0):
    jack = set()
    jill = set()
    for i in range(int(n)):
        jack.add(input())
    for i in range(int(m)):
        jill.add(input())

    print(len(jack & jill))
    n, m = input().split()
'''

#Method 2: Submitted Code

import sys #using readline since input() is slow
def read_n_m():
    return map(int, sys.stdin.readline().split())

def read_cd():
    return int(sys.stdin.readline())

n, m = read_n_m()

while (n, m) != (0, 0):
    jack = set(read_cd() for _ in range(n))
    jill = set(read_cd() for _ in range(m))

    print(len(jack & jill))

    n, m = read_n_m()
