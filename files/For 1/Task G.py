N = int(input())
summa = 0
for i in range(1, N + 1):
    summa += i
for i in range(N - 1):
    summa -= int(input())
print(summa)
