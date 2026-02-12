n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

dp = [0]*n

for i in range(1, n):
    max_jump = 0
    for j in range(0, i):
        if i-j <= arr[j]:
            max_jump = max(max_jump, dp[j]+1)
    dp[i] = max_jump
    if arr[i] != 0 and dp[i] == 0:
        break
print(dp)
print(max(dp))