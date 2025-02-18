x, y = map(int, input().split())
if (x - 1) % (y - (x - 1)) == 0:
    print('YES')
else:
    print('NO')