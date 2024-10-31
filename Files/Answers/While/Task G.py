a = int(input())
b = a
c = 0
k = 0
while a != 0:
    if b > a and b > c and c != 0:
        k += 1
    c = b
    b = a
    a = int(input())
print(k)
