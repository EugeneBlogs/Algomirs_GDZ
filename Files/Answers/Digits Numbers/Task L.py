N = input()
result = ""
if N == "9" * len(N):
    result = f"1{'0' * (len(N) - 1)}1"
elif 10 <= int(N) <= 999:
    i = int(N)
    while True:
        i += 1
        str_i = str(i)
        i_reverse = str_i[::-1]
        if str_i == i_reverse:
            result = i
            break
else:
    first = ""
    for i in range((len(N) + 1) // 2):
        first += N[i]
    second = ""
    if len(N) % 2 == 0:
        second = first
    else:
        second = first[:-1]
    second = second[::-1]
    number = first + second
    if number <= N:
        first = str(int(first) + 1)
        if len(N) % 2 == 0:
            second = first
        else:
            second = first[:-1]
        second = second[::-1]
        number = first + second
    result = number
print(result)
