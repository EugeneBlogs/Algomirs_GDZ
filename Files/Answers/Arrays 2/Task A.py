n = int(input())
a = list(map(int, input().split()))
para = False
for i in range(n - 1):
    if (a[i] < 0 and a[i + 1] < 0) or (a[i] > 0 and a[i + 1] > 0):
        para = True
        break
if para:
    print("YES")
else:
    print("NO")
