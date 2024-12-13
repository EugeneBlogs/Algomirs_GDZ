x, n = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(x)
    x += 1
print(*a)
