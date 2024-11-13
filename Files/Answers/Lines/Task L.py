n = input()
result = ""
if len(n) < 4:
    print(n)
else:
    count = 1
    n = n[::-1]
    for i in range(len(n)):
        if count != 3:
            result += n[i]
        else:
            if i + 1 == len(n):
                result += n[i]
            else:
                result += f"{n[i]},"
            count = 0
        count += 1
    print(result[::-1])
