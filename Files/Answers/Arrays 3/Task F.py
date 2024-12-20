a = [int(i) for i in input().split()]
k, c = list(map(int, input().split()))
a.append(c)
n = len(a) - 1
if k < 0:
    k = len(a) + k
if n != k:
    for i in range(len(a) - 1, -1, -1):
        a[i], a[i - 1] = a[i - 1], a[i]
        n -= 1
        if n == k:
            break
print(*a)
