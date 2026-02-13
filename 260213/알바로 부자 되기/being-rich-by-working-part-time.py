n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

s = [jobs[i][0] for i in range(n)]
e = [jobs[i][1] for i in range(n)]
v = [jobs[i][2] for i in range(n)]

# Please write your code here.

dp = [0] * n
for i in range(n):
    dp[i] = v[i]
    for j in range(i):
        if e[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+v[i])
print(max(dp))