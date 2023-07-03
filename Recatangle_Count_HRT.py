def count_rectangles(x, y):
    points = set(zip(x, y))
    count = 0
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            if p1[0] == p2[0]:
                p3 = (p1[0], p2[1])
                p4 = (p2[0], p1[1])
                if p3 in points and p4 in points:
                    if {p1, p2, p3, p4} <= points:
                        count += 1
    return print(count)
count_rectangles(input(),input())
