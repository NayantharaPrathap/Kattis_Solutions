tt = []
total = 0
rt = 0
a = [i for i in input().split()]
while(int(a[0])>=0):
	if(a[2] == "right"):
		rt+=1
		total+=int(a[0])
		if(a[1] in tt):
			total += 20*tt.count(a[1])
	else:
		tt.append(a[1])
	a = [i for i in input().split()]
print(rt, total)