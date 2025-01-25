n = int(input())
s = [el for el in input().lower()]
a = [chr(el) for el in range(97, 123)]
count = [0] * 26
for el in s:
    if el.isalpha():
        index = 0
        for i in range(len(a)):
            if el == a[i]:
                index = i
        count[index] += 1
print(*count)
