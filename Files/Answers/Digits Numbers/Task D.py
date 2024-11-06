n = int(input())
str = ""
while n >= 1:
    str += f"{n % 2}"
    n //= 2
print(str)
