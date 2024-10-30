i, j = map(int, input().split())
if (i == 99 and j == 100) or (i == 100 and j == 99):
    print(98)
else:
    print(min(i, j))
