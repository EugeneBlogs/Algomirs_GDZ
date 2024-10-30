N = int(input())
temp = input().split(" ")
count = 0
maximum = 0
for i in range(N):
    if int(temp[i]) > 0:
        count += 1
    else:
        count = 0
    if count > maximum:
        maximum = count
print(maximum)
