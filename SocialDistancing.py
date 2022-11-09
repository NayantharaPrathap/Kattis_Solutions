#Social Distancing
'''
S,N = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
finlist = []

for i in range(1,S):
    if i%2==0:
        finlist.append(i)
        cnt += 1
print(len(finlist)-len(lst))
'''

'''
i =0
j =0
while i <max(lst)-1:
    finlist.append(i)

    i += 1
    cnt += 1

while j>max(lst)+1 and j<S-1:
    finlist.append(j)
    j +=1
    cnt += 1

print(len(finlist)-len(lst))
'''

class Node:
   def __init__(self, my_data):
      self.data = my_data
      self.next = None

class circularLinkedList:  
   def __init__(self):
      self.head = S
   def add_data(self, my_data):
      ptr_1 = Node(my_data)
      temp = self.head    
      ptr_1.next = self.head

      if self.head is not None:
         while(temp.next != self.head):
            temp = temp.next
         temp.next = ptr_1
      else:
         ptr_1.next = ptr_1
      self.head = ptr_1

   def print_it(self):
      temp = self.head
      if self.head is not None:
         while(True):
            print("%d" %(temp.data)),
            temp = temp.next
            if (temp == self.head):
               break
my_list = circularLinkedList()
print("Elements are added to the list ")
S,N = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
finlist = []
for i in range(1,S):
    my_list.add_data (int(input()))
#my_list.add_data (12)
print("The data is : ")
my_list.print_it()
