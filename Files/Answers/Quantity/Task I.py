s, n = map(int, input().split())
users = [int(input()) for el in range(n)]
users.sort()
summa = 0
count = 0
for el in users:
    if summa + el <= s:
        summa += el
        count += 1
    else:
        break
print(count)
