n = int(input())
a = n % 10
nearby = False
while n > 0:
    b = a
    n //= 10
    a = n % 10
    if a == b:
        nearby = True
if nearby:
    print("YES")
else:
    print("NO")
