t = int(input())
sum1 = 0
lst = []
for i in range(t):
    for j in range(2):
        object = [int(n) for n in input().split()]
        res = int("".join(map(str, object)))
        sum1 = sum1 + res
    lst.append(sum1)
    sum1 = 0
temp = ''
tem = ''
for i in lst:
    #print(i)
    temp = str(i)
    #print(temp)
    #print(type(temp))
    for k in temp:
        tem = tem + k + ' '
    print(tem)
    tem = ""
