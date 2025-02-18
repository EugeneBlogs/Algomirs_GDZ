def Election(x, y, z):
    count_1 = x + y + z
    count_0 = 3 - count_1
    if count_1 > count_0:
        print(1)
    else:
        print(0)


n = list(map(float, input().split()))
Election(n[0], n[1], n[2])
