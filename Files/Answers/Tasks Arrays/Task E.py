a = list(map(int, input().split()))
result = 0
while True:
    index = []
    for i in range(0, 10):
        for j in range(len(a)):
            if a[j] == i:
                index.append(j)
            else:
                if len(index) >= 3:
                    break
                else:
                    index.clear()
        if len(index) >= 3:
            break
    if len(index) < 3:
        break
    else:
        result += len(index)
        a = a[:min(index)] + a[max(index) + 1:]
print(result)
