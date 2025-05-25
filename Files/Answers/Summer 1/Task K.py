from itertools import product


def main(N, M, coins):
    total = 2 * sum(coins)
    if total < N:
        print(-1)
        return
    if total == N:
        result = coins * 2
        print(len(result))
        print(*result)
        return

    p = product([0, 1, 2], repeat=M)
    for counts in p:
        selected = []
        sum_selected = 0
        for i in range(M):
            selected += [coins[i]] * counts[i]
            sum_selected += coins[i] * counts[i]
            if sum_selected > N:
                break

        if sum_selected == N:
            print(len(selected))
            print(*sorted(selected, reverse=True))
            return

    print(0)


N, M = map(int, input().split())
coins = sorted(list(map(int, input().split())))
main(N, M, coins)
