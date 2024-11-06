N = int(input())
while True:
    N += 1
    str_N = f"{N}"
    reverse_N = ""
    for s in str_N:
        reverse_N = f"{s}{reverse_N}"
    if str_N == reverse_N:
        print(str_N)
        break
