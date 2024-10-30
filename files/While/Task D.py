a = int(input())
mx = 10 ** (-10)
k = 0
while a != 0:
    if a > mx:
        mx = a
        k = 1
    elif a == mx:
        k += 1
    a = int(input())
print(k)
