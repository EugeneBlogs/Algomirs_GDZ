a = list(map(int, input().split()))
count = [0] * 9
for el in a:
    if el != 0:
        count[el - 1] += 1
print(*count)
