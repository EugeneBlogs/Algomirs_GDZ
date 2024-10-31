x = float(input())
p = float(input())
y = float(input())
year = 0
while x < y:
    x *= (p / 100 + 1)  # +p %
    x = int(100 * x) / 100
    year += 1
print(year)
