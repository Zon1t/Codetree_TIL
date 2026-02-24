N = int(input())

# Please write your code here.

mod = 1000000007

dp = [[[0]*3 for _ in range(9)] for _ in range(N+1)]
dp[2][0][0] = 1
dp[2][1][0] = 1
dp[2][2][1] = 1
dp[2][3][0] = 1
dp[2][4][0] = 1
dp[2][5][1] = 1
dp[2][6][1] = 1
dp[2][7][1] = 1
dp[2][8][2] = 1

for day in range(3, N+1):
    for i in range(3):
        dp[day][0][i] += (dp[day-1][0][i] + dp[day-1][3][i] + dp[day-1][6][i]) % mod
        dp[day][0][i] %= mod
        dp[day][3][i] += (dp[day-1][1][i] + dp[day-1][4][i] + dp[day-1][7][i]) % mod
        dp[day][3][i] %= mod
        dp[day][6][i] += (dp[day-1][2][i] + dp[day-1][5][i] + dp[day-1][8][i]) % mod
        dp[day][6][i] %= mod
        dp[day][1][i] += (dp[day-1][0][i] + dp[day-1][3][i] + dp[day-1][6][i]) % mod
        dp[day][1][i] %= mod
        dp[day][4][i] += (dp[day-1][1][i] + dp[day-1][7][i]) % mod
        dp[day][4][i] %= mod
        dp[day][7][i] += (dp[day-1][2][i] + dp[day-1][5][i] + dp[day-1][8][i]) % mod
        dp[day][7][i] %= mod
    for i in range(1, 3):
        dp[day][2][i] += (dp[day-1][0][i-1] + dp[day-1][3][i-1] + dp[day-1][6][i-1]) % mod
        dp[day][2][i] %= mod
        dp[day][5][i] += (dp[day-1][1][i-1] + dp[day-1][4][i-1] + dp[day-1][7][i-1]) % mod
        dp[day][5][i] %= mod
        dp[day][8][i] += (dp[day-1][2][i-1] + dp[day-1][5][i-1]) % mod
        dp[day][8][i] %= mod
total = 0
for i in range(9):
    for j in range(3):
        total += dp[N][i][j]
        total %= mod
print(total)