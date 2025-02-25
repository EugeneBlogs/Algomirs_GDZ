def sum(arr, i):
    if i == -1:
        return 0
    return arr[i] + sum(arr, i - 1)


n = 1
arr = []
while n != 0:
    n = int(input())
    arr.append(n)
print(sum(arr, len(arr) - 1))
