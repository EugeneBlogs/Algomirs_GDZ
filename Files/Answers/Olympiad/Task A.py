N, M, K = map(int, input().split())
buses = (N + M) / K
if buses != int(buses):
    buses = int(buses) + 1
if buses <= M / 2:
    print(int(buses))
else:
    print(0)
