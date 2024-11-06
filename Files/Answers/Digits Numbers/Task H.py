N = int(input())
i = 10
while True:
    i += 1
    M = i
    proizvedenie = 1
    if not ("0" in str(i)):
        while M > 0:
            proizvedenie *= M % 10
            M //= 10
        if proizvedenie == N:
            print(i)
            break
        if i > N ** 2:
            print("No solution")
            break
