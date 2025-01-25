n = int(input())
a = list(map(int, input().split()))
result = []
if a[0] == a[1]:
    result.append(a[0])
for i in range(1, n - 1):
    if a[i] == a[i - 1] + a[i + 1]:
        result.append(a[i])
if a[-1] == a[-2]:
    result.append(a[-1])
print(*result)
