n = int(input())
a = list(map(int, input().split()))
maximum = -10 ** 10
number = 0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        number = i + 1
print(number)
