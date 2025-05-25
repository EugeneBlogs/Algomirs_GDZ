def partition(remaining, max_num, current):
    if remaining == 0:
        print(*current)
        return

    for num in range(1, min(max_num, remaining) + 1):
        current.append(num)
        partition(remaining - num, num, current)
        current.pop()


N = int(input())
partition(N, N, [])
