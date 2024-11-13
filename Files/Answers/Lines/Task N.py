str = input()
numbers = str.split("*")
proizvedenie = 1
for n in numbers:
    proizvedenie *= int(n)
print(proizvedenie)
