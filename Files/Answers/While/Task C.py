a = int(input())
mx = 10 ** (-10)
while a != 0:
    if a > mx:
        mx = a
    a = int(input())
print(mx)
