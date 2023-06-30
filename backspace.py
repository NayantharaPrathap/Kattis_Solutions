from sys import stdin

inp = stdin.readline().strip()

stack = []
for i in inp:
    if i == '<':
        stack.pop()
    else:
        stack.append(i)

print(''.join(stack))