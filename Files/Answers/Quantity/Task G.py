n = int(input())
a = list(map(int, input().split()))
result = []
for i in range(n):
    count = 0
    for el in a:
        if el == a[i]:
            count += 1
    if count > 1 and a[i] not in result:
        result.append(a[i])
print(*result)
