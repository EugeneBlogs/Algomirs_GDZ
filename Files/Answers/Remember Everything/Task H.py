n = int(input())
current = 1
count = 0
result = []
for i in range(n):
    if current == count:
        count = 0
        current += 1
    result.append(f"{current}")
    count += 1
print(" ".join(result))
