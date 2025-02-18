N, M, x, y = map(int, input().split())
if N > M:
    N,M=M,N
dist_x = min(N-x, N - (N-x))
dist_y = min(M-y, M - (M-y))
print(min(dist_x, dist_y))