from itertools import product

n = int(input())
p = product("01", repeat=n)
for x in p:
    str = "".join(x)
    print(str)
