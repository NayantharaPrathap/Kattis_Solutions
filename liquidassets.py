import string
n, m = int(input()), input().strip().split()
for i in range(n):
    s, t, t1 = m[i], '', ''
    for j in string.ascii_lowercase:
        while True:
            s1 = s.replace(j*2, j)
            if s1 == s: break
            s = s1
    if s and s[0] in 'aeiou': t, s = s[0], s[1:]
    if s and s[-1] in 'aeiou': t1, s = s[-1], s[:-1]
    for p in 'aeiou': s = s.replace(p, '')
    m[i] = t+s+t1
print(' '.join(m))
