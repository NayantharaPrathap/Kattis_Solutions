#Shopping List
'''
def printDuplicates(arr):
    dict = {}
 
    for ele in arr:
        try:
            dict[ele] += 1
        except:
            dict[ele] = 1
             
    for item in dict:
         
         # if frequency is more than 1
         # print the element
        if(dict[item] == m):
            print(item, end=" ")
 
    print("\n")
 
# Driver Code
#if __name__ == "__main__":
n,m = map(int, input().split())
list1 =[]
list2 = []
for i in range(n):
    list1 = [input() for j in range(m)]
    list2.append(list1)
    
printDuplicates(list2)
'''

n = int(input().split()[0])
#print(n)
s = set(input().split())
for _ in range(n-1):
    s.intersection_update(input().split())
print(len(s))
print("\n".join(sorted(s)))
