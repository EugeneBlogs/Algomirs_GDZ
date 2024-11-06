N = int(input())
result = 0
while N > 0:
    result += N % 10
    result *= 10
    N //= 10
print(result // 10)
