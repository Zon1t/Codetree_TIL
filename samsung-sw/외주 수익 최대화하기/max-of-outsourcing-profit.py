N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for idx, (time, money) in enumerate(arr):
    if idx+time <= N:
        dp[idx+time] = max(dp[idx+time], max(dp[:idx+1])+money)

print(max(dp))