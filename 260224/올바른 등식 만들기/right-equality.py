N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.

dp = [[0]*41 for _ in range(N)]
dp[0][20 + nums[0]] = 1
dp[0][20 - nums[0]] = 1

for i in range(1, N):
    for j in range(41):
        num = j - 20
        if dp[i-1][j] == 0:
            continue
        if num + nums[i] <= 20:
            dp[i][j + nums[i]] += dp[i-1][j]
        if num - nums[i] >= -20:
            dp[i][j - nums[i]] += dp[i-1][j]
print(dp[-1][M+20])