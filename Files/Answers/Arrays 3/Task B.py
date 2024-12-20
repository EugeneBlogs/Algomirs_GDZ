str = input()
a = []
a.append("0")
a.append("0")
a.append("0")
a.append("0")
a.extend(str)
a = a[-4:]
print(int(a[:2] == a[2:][::-1]))
