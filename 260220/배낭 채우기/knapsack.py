N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = [0]+list(w), [0]+list(v)

# Please write your code here.

# dp = [[0] * (M+1) for _ in range(N)]
# for i in range(N):
#     for j in range(M, 0, -1):
#         if w[i] <= j:
#             dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i][j-1], dp[i-1][j])
#         else:
#             if i > 0:
#                 dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#             else:
#                 dp[i][j] = dp[i][j-1]
# print(dp[-1][-1])

dp = [[-1] * (M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for j in range(M, -1, -1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w[i]]+v[i], dp[i-1][j])
print(max(dp[N]))