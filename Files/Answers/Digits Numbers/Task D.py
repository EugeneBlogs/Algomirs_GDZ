n = int(input())
str = ""
while n > 0:
    str += f"{n % 2}"
    n //= 2
print(str)
