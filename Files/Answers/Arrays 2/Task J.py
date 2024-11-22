a = list(map(int, input().split()))
result = -1
for i in range(len(a)):
    if a[i] == 1:
        for j in range(i, len(a)):
            if a[j] == 0:
                itog = j - i - 1
                if itog < result or result == -1:
                    result = itog
print(result)
