x, n = map(int, input().split())
for i in range(n):
    x += x // 10
print(x)
