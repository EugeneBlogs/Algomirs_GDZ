x = int(input())
d = int(input())
count = 0
while x > 0:
    n = x % 10
    if n == d:
        count += 1
    x //= 10
print(count)