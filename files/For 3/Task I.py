n = int(input())
summa = 0
one = 1
for i in range(n + 1):
    summa += 4 * (one / (2 * i + 1))
    one *= -1
print(summa)
