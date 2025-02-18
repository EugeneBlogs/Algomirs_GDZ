def min(a, b, c, d):
    if a <= b and a <= c and a <= d:
        print(a)
    elif b <= a and b <= c and b <= d:
        print(b)
    elif c <= b and c <= a and c <= d:
        print(c)
    elif d <= b and d <= c and d <= a:
        print(d)


n = list(map(int, input().split()))
min(n[0], n[1], n[2], n[3])
