N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.

dp = [0] * (M+1)

for i in range(1, M+1):
    for coin in coins:
        dp[coin] = max(1, dp[coin])
        if coin <= i and dp[i-coin] != 0:
            dp[i] = max(dp[i-coin]+1, dp[i])
print(dp[M])