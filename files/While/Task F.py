a = int(input())
b = int(input())
maximum = 1
count = 1
while b != 0:
    while a > b and b != 0:
        count += 1
        a = b
        b = int(input())
        if count > maximum:
            maximum = count
    count = 1
    while a < b and b != 0:
        count += 1
        a = b
        b = int(input())
        if count > maximum:
            maximum = count
    count = 1
    while a == b and b != 0:
        count = 1
        a = b
        b = int(input())
print(maximum)
