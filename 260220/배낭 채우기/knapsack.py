N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

dp = [[0] * (M+1) for _ in range(N)]
for i in range(N):
    for j in range(w[i], M+1):
        dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])