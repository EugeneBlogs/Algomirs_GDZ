n = int(input())
for j in range(n):
    print("+___", end=" ")
print()
for j in range(1, n + 1):
    print(f"|{j} /", end=" ")
print()
for j in range(n):
    print("|__\\", end=" ")
print()
for j in range(n):
    print("|   ", end=" ")
