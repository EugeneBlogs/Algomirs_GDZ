n = int(input())
a = list(map(int, input().split()))
b = [0] * n
for i in range(n - 1):
    b[i + 1] = a[i]
b[0] = a[n - 1]
print(*b)
