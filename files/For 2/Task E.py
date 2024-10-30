a1, a2, N = map(int, input().split())
d = a2 - a1
for i in range(1, N + 1):
    print(a1 + (i - 1) * d, end=" ")
