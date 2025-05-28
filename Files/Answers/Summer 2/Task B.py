x = int(input())
divisors = []
for i in range(1, int(x ** 0.5) + 1):
    if i ** 2 == x:
        divisors.append(i)
    elif x % i == 0:
        divisors.append(i)
        divisors.append(x // i)
print(*sorted(divisors))
