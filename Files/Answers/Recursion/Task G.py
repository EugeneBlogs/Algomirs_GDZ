def reverse(arr, i):
    if i == -1:
        return 0
    print(arr[i])
    return reverse(arr, i - 1)


n = 1
arr = []
while n != 0:
    n = int(input())
    arr.append(n)
reverse(arr, len(arr) - 1)
