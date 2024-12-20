from itertools import product

n = int(input())
p = product("01", repeat=n)
result = []
for x in p:
    result.append("".join(x))
for i in range(len(result) - 1, -1, -1):
    print(result[i])
