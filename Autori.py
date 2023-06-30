s = input()
st = ''
for i in range(len(s)):
    if i == 0:
        st = st + (s[i])
    if s[i] == '-'and i<(len(s)-1):
        st = st + (s[i+1])
print(st)
