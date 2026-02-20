N = int(input())
profit = list(map(int, input().split()))

# Please write your code here.

dp = [-1]*(N+1)
dp[0] = 0
for i in range(N):
    for j in range(i+1, N+1):
        dp[j] = max(dp[j-i-1]+profit[i], dp[j])
print(dp[-1])