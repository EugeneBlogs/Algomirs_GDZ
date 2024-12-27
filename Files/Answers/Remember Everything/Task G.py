a, b, c, d = map(int, input().split())
d -= b
c -= a
if d < 0:
    c -= 1
    d += 60
print(c, d)
