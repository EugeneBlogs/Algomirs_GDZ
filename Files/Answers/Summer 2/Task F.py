from itertools import combinations

n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
max_area = 0

p = combinations(points, 3)
for el in p:
    a, b, c = el
    area = 0.5 * abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))
    max_area = max(area, max_area)

print("{0:.15f}".format(max_area))
