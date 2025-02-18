def Xor(x, y):
    if (x == 1 and y == 1) or (x == 0 and y == 0):
        print(0)
    elif (x == 1 and y == 0) or (x == 0 and y == 1):
        print(1)


n = list(map(int, input().split()))
Xor(n[0], n[1])
