str = input()
result = ""
for s in str:
    if s != " ":
        result += s
    else:
        if result != "":
            break
print(result)
