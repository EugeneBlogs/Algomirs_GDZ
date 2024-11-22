n = int(input())
a = list(map(int, input().split()))
minimum = 10 ** 10
maximum = -10 ** 10
ok = False
for i in range(n):
    if a[i] % 2 == 0 and a[i] > 0:
        if a[i] < minimum:
            minimum = a[i]
            ok = True
        elif a[i] > maximum:
            maximum = a[i]
            ok = True
if ok:
    print(minimum, maximum)
else:
    print(-1, -1)
