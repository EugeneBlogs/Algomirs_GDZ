a, b = map(int, input().split())
result = False
for i in range(a, b + 1):
    count = len(str(i))
    if i ** 2 % (10 ** count) == i:
        print(i, end=" ")
        result = True
if not result:
    print(-1)
