inp = input()
l = len(inp)
st = ""
if l<1 or l>250:
    sys.exit()
else:
    for i in range(l):
        if i == 0 or inp[i] != inp[i-1]:
            st = st + inp[i]
            
print(st)
