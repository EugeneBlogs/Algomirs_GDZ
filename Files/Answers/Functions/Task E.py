def prime(x):
    result = "prime"
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            result = "composite"
            break
    print(result)


n = int(input())
prime(n)
