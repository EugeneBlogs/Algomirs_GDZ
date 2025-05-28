M, N = map(int, input().split())
deliteli = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        deliteli[j] += i

found = False
for i in range(M, N + 1):
    j = deliteli[i]
    if M <= j <= N and i < j and deliteli[j] == i:
        print(i, j)
        found = True

if not found:
    print("Absent")