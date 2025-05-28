K, L = map(int, input().split())
result = False

for a in range(1, 10 ** 4):
    for b in range(1, 10 ** 4):
        if (a - 1) * (b - 1) == K and (a - 1) * b + (b - 1) * a == L:
            print(a, b)
            result = True
            break
    if result:
        break
