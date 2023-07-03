N = int(input())
for _ in range(N):
  str1 = input()
  str2 = input()
  print(str1)
  print(str2)
  for c1, c2 in zip(str1, str2):
    if c1 == c2:
      print('.', end='')
    else:
      print('*', end='')
  print()
