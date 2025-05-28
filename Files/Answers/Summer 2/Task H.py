n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = True

for i in range(n):
    for j in range(i + 1, n):
        if arr[i][j] != arr[j][i]:
            result = False
            break
    if not result:
        break

if result:
    print("yes")
else:
    print("no")
