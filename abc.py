lst = input().split()
lst_n = []
for i in lst: 
    lst_n.append(int(i))
lst_n.sort()
for i, char in enumerate(input().lower()):
	print(lst_n[ord(char) - 97], end=" ")