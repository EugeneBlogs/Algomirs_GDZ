n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
max_len = 0
result = []
for x, y in points:
    distance = (x ** 2 + y ** 2) ** 0.5
    if distance >= max_len:
        max_len = distance
        result = [x, y]
print(*result)
