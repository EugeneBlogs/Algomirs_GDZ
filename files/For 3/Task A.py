N = int(input())
nol = False
for i in range(N):
    a = int(input())
    if a == 0:
        nol = True
if nol:
    print("YES")
else:
    print("NO")
