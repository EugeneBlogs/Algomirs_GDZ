K, N = map(int, input().split())
page = 1
while N > K:
    N -= K
    page += 1
print(page, N)
