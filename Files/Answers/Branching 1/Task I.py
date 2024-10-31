k = int(input())
m = int(input())
n = int(input())
time = 0

if n <= k:
    time = m * 2
elif (2 * n) % k == 0:
    time = (2 * n // k) * m
else:
    time = (1 + (2 * n // k)) * m
print(time)
