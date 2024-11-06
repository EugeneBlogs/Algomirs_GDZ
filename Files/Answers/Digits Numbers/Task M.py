n = int(input())
similar = False
count = 0
current_number = 0
while current_number != 10:
    a = n
    while a > 0:
        number = a % 10
        a //= 10
        if number == current_number:
            count += 1
    if count > 1:
        similar = True
        break
    count = 0
    current_number += 1
if similar:
    print("YES")
else:
    print("NO")
