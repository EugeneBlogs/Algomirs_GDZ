a = list(map(int, input().split()))
summa = 0
count = 0
for i in range(len(a)):
    if i + 1 < len(a):
        if not (a[i] == 2 and a[i + 1] != 2):
            summa += a[i]
            count += 1
    else:
        summa += a[i]
        count += 1
srednee = summa / count
print(int(srednee))
