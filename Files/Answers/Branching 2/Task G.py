a = float(input())
b = float(input())
c = float(input())
D = (b ** 2) - (4 * a * c)
if D > 0:
    sqrt_D = D ** 0.5
    x1 = ((-b) + sqrt_D) / (2 * a)
    x2 = ((-b) - sqrt_D) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = (-b) / (2 * a)
    print(x)
