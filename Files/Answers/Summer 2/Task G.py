from math import ceil

A = int(input())
min_count = ceil(A / 2)
result = [i for i in range(min_count, A + 1)]
print(*result)
