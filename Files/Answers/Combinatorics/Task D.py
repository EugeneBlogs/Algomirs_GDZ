from itertools import product

n, k = map(int, input().split())
alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
str = alphabet[:int(k)]
p = product(str, repeat=n)
result = []
for x in p:
    result.append("".join(x))
for i in range(len(result) - 1, -1, -1):
    print(result[i])
