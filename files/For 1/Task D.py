N = int(input())
count_p = 0
count_o = 0
count_0 = 0
for i in range(N):
    a = int(input())
    if a > 0:
        count_p += 1
    elif a < 0:
        count_o += 1
    else:
        count_0 += 1
print(count_0, count_p, count_o)
