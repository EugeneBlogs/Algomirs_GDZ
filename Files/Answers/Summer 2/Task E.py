x, y = map(int, input().split())
result = []
for i in range(x, y + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        result.append(i)
if len(result) == 0:
    print("Absent")
else:
    for el in result:
        print(el)
