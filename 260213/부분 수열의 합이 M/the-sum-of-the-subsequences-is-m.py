n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

import sys
INT_MAX = 101

dp = [INT_MAX] * (m+1)
dp[0] = 0

for number in A:
    for i in range(m, number-1, -1):
        dp[i] = min(dp[i-number]+1, dp[i])

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])