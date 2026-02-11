n = int(input())
m = list(map(int, input().split()))

# Please write your code here.

dp = [0]*n
dp[0] = 1

for i in range(1, n):
    max_count = 1
    for j in range(i-1, -1, -1):
        if m[i] < m[j]:
            max_count = max(max_count, dp[j]+1)
    dp[i] = max_count
print(max(dp))