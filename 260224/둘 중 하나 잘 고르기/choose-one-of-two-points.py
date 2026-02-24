n = int(input())
red = [0]
blue = [0]

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = dp[i-1][0] + blue[i]
    dp[0][i] = dp[0][i-1] + red[i]

for turn in range(1, 2*n):
    temp = min(turn, n)
    for i in range(temp, turn-temp, -1):
        j = turn - i + 1
        dp[i][j] = max(dp[i-1][j] + blue[turn+1], dp[i][j-1] + red[turn+1])

print(dp[n][n])