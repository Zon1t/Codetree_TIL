n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dp = [[0]*m for _ in range(n+1)]

for f in range(1, n+1):
    for r in range(m):
        for p in range(m):
            if r == p:
                continue
            
            dp[f][r] = dp[f-1][p] if dp[f][r] < dp[f-1][p] else dp[f][r]
        dp[f][r] += a[f-1][r]
print(max(dp[-1]))