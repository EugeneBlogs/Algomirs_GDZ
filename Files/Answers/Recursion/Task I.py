def F(h, n):
    if h == n:
        return 1
    elif h > n:
        return 0
    else:
        return F(h + 2, n) + F(h + 3, n)


print(F(0, int(input())))
