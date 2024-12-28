N, i, j = map(int, input().split())
x = i
y1 = -1
y2 = -1
while x != j:
    x += 1
    if x > N:
        x = 1
    y1 += 1
x = i
while x != j:
    x -= 1
    if x < 1:
        x = N
    y2 += 1
print(min(y1, y2))
