a = list(map(int, input().split()))
para = []
for i in range(len(a) - 1):
    if (a[i] < 0 and a[i + 1] < 0) or (a[i] > 0 and a[i + 1] > 0):
        para = [a[i], a[i + 1]]
        break
print(*para)
