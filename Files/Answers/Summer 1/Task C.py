a = float(input())
b = float(input())
c = float(input())
if abs(a + b - c) < 10 ** (-9):
    print("YES")
else:
    print("NO")
