N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = [0]+list(w), [0]+list(v)

# Please write your code here.

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])