def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a, b = int(input()), int(input())
print(gcd(a, b))
