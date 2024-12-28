str = input()
numbers = []
numbers.extend(str)
numbers.sort()
if numbers[0] == "0" and numbers[1] == "0" and numbers[2] == "0":
    numbers[0], numbers[3] = numbers[3], numbers[0]
if numbers[0] == "0" and numbers[1] == "0":
    numbers[0], numbers[2] = numbers[2], numbers[0]
if numbers[0] == "0":
    numbers[0], numbers[1] = numbers[1], numbers[0]
print("".join(numbers))
