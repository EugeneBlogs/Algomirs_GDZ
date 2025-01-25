n = int(input())
a = list(map(int, input().split()))
mx = 0
numbers = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] * a[j] > mx:
            mx = a[i] * a[j]
            numbers = [a[i], a[j]]
if numbers[0] > numbers[1]:
    numbers[1], numbers[0] = numbers[0], numbers[1]
print(*numbers)
