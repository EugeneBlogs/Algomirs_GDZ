n = int(input())
a = [int(i) for i in input().split()]
minimum = 10 ** 10
maximum = 10 ** (-10)
i_1 = 0
i_2 = 0
for s in a:
    minimum = min(s, minimum)
    maximum = max(s, maximum)
for i in range(len(a)):
    if a[i] == minimum:
        i_1 = i
    elif a[i] == maximum:
        i_2 = i
a[i_1], a[i_2] = a[i_2], a[i_1]
print(*a)
