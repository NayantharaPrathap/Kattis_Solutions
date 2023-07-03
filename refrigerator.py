from math import inf, ceil

pa, ka, pb, kb, n = map(int, input().split())
a, cost, min_a, min_b = 0, float(inf), 0, 0

while a < n // ka + 1:
    b = ceil((n - a * ka) / kb)
    if pa * a + pb * b < cost:
        min_a, min_b, cost = a, b, pa * a + pb * b
    a += 1
print(min_a, min_b, cost)