a, b = map(int, input().split())
result = False
for i in range(a, b + 1):
    if i ** 2 % 100 == i:
        print(i, end=" ")
        result = True
if not result:
    print(-1)
