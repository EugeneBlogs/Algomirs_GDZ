n = int(input())
a = list(map(int, input().split()))
maximum = -10 ** 10
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
print(maximum)
