n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(0, n - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(*a)
