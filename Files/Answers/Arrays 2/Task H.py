a = list(map(int, input().split()))
n = a[0]
summa = n * (n + 1) // 2
card_summa = 0
for i in range(1, len(a)):
    card_summa += a[i]
print(summa - card_summa)
