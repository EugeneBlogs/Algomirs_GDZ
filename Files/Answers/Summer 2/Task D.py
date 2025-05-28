n, m = map(int, input().split())
A = [[0 for i in range(m)] for j in range(n)]

for k in range(n * m):
    i = k // m
    j = k % m
    A[i][j] = i * j

for row in A:
    print(*row)
