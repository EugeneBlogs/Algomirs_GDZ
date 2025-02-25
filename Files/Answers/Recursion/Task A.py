def F(n):
    if n > 2:
        return F(n - 1) + F(n - 2)
    return 1


n = int(input())
if n == 0:
    print(0)
else:
    print(F(n))
