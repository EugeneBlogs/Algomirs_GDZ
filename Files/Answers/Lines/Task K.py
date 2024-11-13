str = input()
result = ""
polovina = len(str) // 2
for i in range(polovina):
    result += f"{str[polovina + i]}{str[i]}"
if len(str) % 2 != 0:
    result += str[-1]
print(result)
