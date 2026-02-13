N, M = map(int, input().split())
coins = list(map(int, input().split()))

# Please write your code here.

import sys
INT_MAX = sys.maxsize

dp = [INT_MAX] * (M+1)
dp[0] = 0

for i in range(1, M+1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i-coin]+1)
if dp[M] == INT_MAX:
    print(-1)
else:
    print(dp[M])