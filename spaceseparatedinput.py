"""
print("Enter the numbers: ")

'''
inp = list(map(int, input().split()))

print(inp)
'''
inp = input()
s = inp.strip(' ')
print(s)

res = int("".join(map(str, list)))
"""
'''
num = 2019
 
# printing number
print("The original number is " + str(num))
 
# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]
 
# printing result
print("The list from number is " + str(res))
'''
'''
lst = [1, 2, 3, 5]
res = ""
for i in lst:
    s = str(lst[i])
    res = res + s + " "

print(res)
'''
A = [123, 23, 456, 756, 84]
print(*A)
