n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

# 첫 층을 저장해줄 변수를 따로 따와야하는가?

max_value = 0
dp = [[0]*3 for _ in range(n)]
dp[0][0] = l[0]
dp[1][1], dp[1][2] = m[1]+l[0], r[1]+l[0]
if n == 2:
    max_value = max(max_value, max(dp[1]))
else:
    for i in range(2, n):
        if i == n-1:
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m[i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r[i]
            max_value = max(max_value, max(dp[i]))
            break
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r[i]
dp = [[0]*3 for _ in range(n)]
dp[0][1] = m[0]
dp[1][0], dp[1][2] = l[1]+m[0], r[1]+m[0]
if n == 2:
    max_value = max(max_value, max(dp[1]))
else:
    for i in range(2, n):
        if i == n-1:
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r[i]
            max_value = max(max_value, max(dp[i]))
            break
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r[i]
dp = [[0]*3 for _ in range(n)]
dp[0][2] = r[0]
dp[1][0], dp[1][1] = l[1]+r[0], m[1]+r[0]
if n == 2:
    max_value = max(max_value, max(dp[1]))
else:
    for i in range(2, n):
        if i == n-1:
            dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m[i]
            max_value = max(max_value, max(dp[i]))
            break
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + m[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + r[i]
print(max_value)