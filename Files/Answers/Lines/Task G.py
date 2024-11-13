str = input()
num = str.count("A") + str.count("a") + str.count("B") + str.count("b")
result = ""
for s in str:
    if s == "а":
        result += "b"
    elif s == "A":
        result += "B"
    elif s == "b":
        result += "a"
    elif s == "B":
        result += "A"
    else:
        result += s
print(result)
print(num)
