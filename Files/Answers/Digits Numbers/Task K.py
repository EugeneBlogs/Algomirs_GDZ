K = int(input())
count = 0
for i in range(1, K + 1):
    str_i = f"{i}"
    reverse_i = ""
    for s in str_i:
        reverse_i = f"{s}{reverse_i}"
    if str_i == reverse_i:
        count += 1
print(count)
