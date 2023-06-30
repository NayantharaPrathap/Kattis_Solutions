#Integer Lists - Kattis Question

n = int(input())

output = [''] * n

def reversing(l):
    if len(l) != 0:
        return l.reverse()
    else:
        return 'error'
    
def drop(l):
    if len(l) != 0:
        l.pop()
        return l
    else:
        return 'error'

for i in range(n):
    operation = input()
    lengthoflist = int(input())
    temp = ''
    if lengthoflist!=0:
        lst = list(map((input()))

        for x in operation:
            if x == 'R':
                temp = reversing(lst)
            elif x == 'D':
                temp = drop(lst)
            
        output.append(temp)
    else:
        output.append('error')
for o in output: print(o)
