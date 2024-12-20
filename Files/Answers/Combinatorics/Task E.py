from itertools import permutations

str = input()
letters = str[0] + str[4:]
numbers = str[1:4]
result = []
p1 = permutations(letters, 3)
for x1 in p1:
    p2 = permutations(numbers, 3)
    for x2 in p2:
        str_1 = "".join(x1)
        str_2 = "".join(x2)
        res = str_1[0] + str_2 + str_1[1:]
        if res not in result:
            result.append(res)
print(len(result))
for s in result:
    print(s)
