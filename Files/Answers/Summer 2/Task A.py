def fib(n):
    if 0 <= n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))
