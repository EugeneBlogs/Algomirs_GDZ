def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    print(result)


n = list(map(float, input().split()))
power(n[0], int(n[1]))
