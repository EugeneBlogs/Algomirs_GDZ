K, N = map(int, input().split())
result = False
for i in range(K, N + 1):
    d = 2
    prostoe = True
    while d ** 2 <= i and prostoe:
        if i % d == 0:
            prostoe = False
        d += 1
    if prostoe:
        n = i
        summa = 0
        while n > 0:
            summa += n % 10
            n //= 10
        if summa % 2 == 0:
            print(i, end=" ")
            result = True
if not result:
    print(0)
