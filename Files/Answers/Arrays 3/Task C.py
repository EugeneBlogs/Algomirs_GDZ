a = [int(i) for i in input().split()]
k = -1
for i in range(len(a) - 1):
    a[k], a[k - 1] = a[k - 1], a[k]
    k -= 1
print(*a)
