N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = [0]+list(w), [0]+list(v)

# Please write your code here.

# 굳이 이렇게 풀 이유가 없었다.
# dp = [[0] * (M+1) for _ in range(N+1)]
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         if j >= w[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])

dp = [0] * (M+1)
for i in range(1, N+1):
    for j in range(w[i], M+1):
        dp[j] = max(dp[j-w[i]]+v[i], dp[j])
print(max(dp))