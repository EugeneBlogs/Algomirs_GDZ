n = int(input())
a = [int(i) for i in input().split()]
k = int(input())
k %= n
a = a[n - k:] + a[:n - k]
print(*a)
