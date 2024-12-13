n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append([0] * m)
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j] + a[i][j - 1]
for el in a:
    print(*el)
