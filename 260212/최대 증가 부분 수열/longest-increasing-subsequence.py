n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

dp = [0]*n
dp[0] = 1

for i in range(1, n):
    temp_max = 0
    for j in range(i-1, -1, -1):
        if m[j] < m[i]:
            temp_max = max(temp_max, dp[j]+1)
        dp[i] = temp_max
print(max(dp))