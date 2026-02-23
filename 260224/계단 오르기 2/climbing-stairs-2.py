n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.

dp = [[0]*4 for _ in range(n+1)]
dp[1][1] = coin[1]
dp[2][0] = coin[2]
dp[2][2] = coin[1] + coin[2]

for i in range(3, n+1):
    for order in range(4):
        if order == 0:
            dp[i][order] = dp[i-2][order] + coin[i]
        else:
            dp[i][order] = max(dp[i-1][order-1], dp[i-2][order]) + coin[i] 
print(max(dp[n]))