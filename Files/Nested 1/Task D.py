n = int(input())
summa = 0
current = 1
for i in range(1, n + 1):
    current *= i
    summa += current
print(summa)
