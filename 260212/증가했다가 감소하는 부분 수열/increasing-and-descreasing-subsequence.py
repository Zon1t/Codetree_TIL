n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

dp = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(i):
        if sequence[-1-j] < sequence[-1-i]:
            dp2[-1-i] = max(dp2[-1-i], dp2[-1-j]+1)
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max([dp[i]+dp2[i] for i in range(n)])-1)