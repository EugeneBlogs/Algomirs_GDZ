a = int(input())
b = int(input())
n = int(input())
a *= n
b *= n
a += b // 100
b -= (b // 100) * 100
print(a, b)
