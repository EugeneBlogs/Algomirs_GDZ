N = int(input())
minimum = 10**10
maximum = 10**(-10)
while N > 0:
    a = N % 10
    if a < minimum:
        minimum = a
    if a > maximum:
        maximum = a
    N //= 10
print(minimum, maximum)