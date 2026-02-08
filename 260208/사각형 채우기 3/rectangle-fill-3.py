n = int(input())

# Please write your code here.

# 1일 때, 2
# 2일 떄, 7
# 3일 때..??? 7 * 2              +      3 + 3                        +        2
#           nl[-1]*2          위 & 아래(ㄱ, ㄴ뒤집힌 모양)          누워서 2줄..?nl[-2]

mod = 1000000007

dp = [[0, 0], [2, 1], [7, 3]] + [[0, 0] for _ in range(998)] 
for i in range(3, n+1):
    dp[i][0] = (dp[i-1][0] * 2 + dp[i-1][1] * 2 + dp[i-2][0])%mod
    dp[i][1] = (dp[i-1][1] + dp[i-1][0])%mod
print(dp[n][0])
