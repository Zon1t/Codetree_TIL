n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

import sys
INT_MAX = sys.maxsize

dp = [INT_MAX] * (m+1)
dp[0] = 0

for number in A:
    for i in range(m, -1, -1):
        if dp[i] != INT_MAX and i+number <= m:
            dp[i+number] = min(dp[i]+1, dp[i+number])

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])