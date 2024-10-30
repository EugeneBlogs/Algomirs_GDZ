a = int(input())
b = a
k = 0
while a != 0:
    if a > b:
        k += 1
    b = a
    a = int(input())
print(k)
