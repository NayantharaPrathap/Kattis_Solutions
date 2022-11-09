inp_string = input()
ascii_values = []
s = 0
for i in inp_string:
    ascii_values.append(ord(str(i)))
s = sum(ascii_values)
avg = s//len(inp_string)
print(chr(avg))
