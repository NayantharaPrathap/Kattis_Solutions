#Working from Home - Calgary Collegiate Programming Contest 2021
m, p, n = map(int, input().split())
lst = []
cnt = 0
for i in range(n):
    lst.append(int(input()))

for i in lst:
    if i>m:
        temp = i
        p_percent_val = (temp - m)*(p/100)
        if temp >= m-p_percent_val:
            cnt += 1
        else:
            m = m - p_percent_val

    else:
        extra_time_needed = m - i
        cnt = 0
        #m = i - p_percent_val
print(cnt)
