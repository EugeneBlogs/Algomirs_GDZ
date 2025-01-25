n = int(input())
a = list(map(int, input().split()))
count = 0
mx = max(a)
for el in a:
    if el == mx:
        count += 1
print(count)
