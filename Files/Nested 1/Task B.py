H = int(input())
now_symbols = 1
symbols = 1 + (H - 1) * 2
for i in range(H):
    probel = (symbols - now_symbols) // 2
    for j in range(probel):
        print(" ", end="")
    for j in range(now_symbols):
        print("*", end="")
    print()
    now_symbols += 2
