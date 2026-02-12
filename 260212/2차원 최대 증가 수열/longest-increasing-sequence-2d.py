n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for row in range(1, n):
    for col in range(1, n):
        for i in range(row):
            for j in range(col):
                if grid[row][col] > grid[i][j] and dp[i][j] != 0:
                    dp[row][col] = max(dp[i][j] + 1, dp[row][col])

print(max([max(row) for row in dp]))