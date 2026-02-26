N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.

dp = [[-1]*N for _ in range(M+1)]
for idx, start in enumerate(s):
    if start == 1:
        dp[1][idx] = 0

for day in range(1, M+1):
    for i in range(N):
        start, end = s[i], e[i]
        if start > day  or day > end:
            continue
        now_max = 0
        for j in range(N):
            if dp[day-1][j] != -1:
                now_max = max(now_max, dp[day-1][j] + abs(v[i]-v[j]))
        dp[day][i] = now_max
print(max(dp[-1]))