n = int(input())
nearby = False
a = n % 10
n //= 10
while n > 0:
    b = n % 10
    if a == b:
        nearby = True
    n //= 10
    a = b
if nearby:
    print("YES")
else:
    print("NO")
