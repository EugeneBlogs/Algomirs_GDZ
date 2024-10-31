a = int(input())
b = int(input())
c = int(input())
f1 = 0
f2 = 0
if a % 2 == 0:
    f2 = 1
else:
    f1 = 1

if b % 2 == 0:
    f2 = 1
else:
    f1 = 1

if c % 2 == 0:
    f2 = 1
else:
    f1 = 1

if f1 != 0 and f2 != 0:
    print("YES")
else:
    print("NO")
