n = int(input())
ok = False
for A in range(n):
    for B in range(n):
        N = 3 * A + 5 * B
        if n == N:
            print(A, B)
            ok = True
            break
    if ok:
        break
if not ok:
    print("IMPOSSIBLE")
