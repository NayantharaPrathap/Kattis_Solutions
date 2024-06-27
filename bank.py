n, time = map(int, input().split())
dict1 = {}
for x in range(n):
    amount, t = map(int, input().split())
    if amount in dict1.keys():
        dict1[amount] += [t]
    else:
        dict1.update({amount: [t]})
sum = 0
times = [""] * time
lst = list(dict1.keys())
lst.sort(reverse=True)
for amount in lst:
    if time >0:
        temp = sorted(dict1.get(amount))
        for m in temp:
            if time > 0:
                temp_time = m
                for x in range(temp_time, -1, -1):
                    if times[x] == "":
                        times[x] = amount
                        break
    else:
        break
for m in times:
    if type(m) is int:
        sum += m
print(sum)