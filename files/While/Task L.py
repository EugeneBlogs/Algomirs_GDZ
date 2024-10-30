x = int(input())
k = 0
d = 1
while d < x ** 0.5:
    if x % d == 0:
        k += 1
    d += 1
if x ** 0.5 == int(x ** 0.5):
    print(k * 2 + 1)
else:
    print(k * 2)
