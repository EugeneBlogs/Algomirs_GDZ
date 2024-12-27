n = int(input())
lines = list(map(int, input().split()))
count = 0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if lines[i] + lines[j] > lines[k] and lines[i] + lines[k] > lines[j] and lines[k] + lines[j] > lines[i]:
                count += 1
print(count)
