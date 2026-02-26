n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

dp = [[0]*3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = l[0], m[0], r[0]
for f in range(1, n):
    dp[f][0] = max(dp[f-1][1], dp[f-1][2]) + l[f]
    dp[f][1] = max(dp[f-1][0], dp[f-1][2]) + m[f]
    dp[f][2] = max(dp[f-1][0], dp[f-1][1]) + r[f]
print(max(dp[-1]))