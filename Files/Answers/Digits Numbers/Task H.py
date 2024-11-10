n = int(input())
m = 0
razryad = 1
if n < 9:
    m = 10 + n
else:
    while n > 1:
        for i in range(9, 1, -1):
            if n % i == 0:
                n //= i
                m += i * razryad
                razryad *= 10
                break
        if m == 0:
            break
if m == 0:
    print("No solution")
else:
    print(m)
