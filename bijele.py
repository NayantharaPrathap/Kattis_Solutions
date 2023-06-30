inp = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
temp = 0
final_list = []
for i in range(6):
    if inp[i] == chess[i]:
        final_list.append(0)
    else:
        temp = (chess[i] - inp[i])
        final_list.append(temp)
        temp = 0
ll = ""
for i in range(6):
    q = str(final_list[i])
    ll = ll + q + " "
print(ll)
