def phib(n):
    if n > 2:
        return phib(n - 1) + phib(n - 2)
    return 1


n = int(input())
if n == 0:
    print(0)
else:
    print(phib(n))
