n = int(input())
a = list(map(int, input().split()))
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
print(*a)