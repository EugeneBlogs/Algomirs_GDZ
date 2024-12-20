from itertools import product

n, k = map(int, input().split())
alphabet = "0123456789"[:int(k)]
p = product(alphabet, repeat=n)
for x in p:
    str = "".join(x)
    print(str)
