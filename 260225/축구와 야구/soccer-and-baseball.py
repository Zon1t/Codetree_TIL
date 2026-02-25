n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.

dp = [[0]*12 for _ in range(10)]
for i in range(n):
    for j in range(min(9, i+1), -1, -1):
        for k in range(min(11, i+1-j), -1, -1):
            if j == 0:
                if k == 0:
                    continue
                else:
                    dp[j][k] = max(dp[j][k], dp[j][k-1] + s[i])
            else:
                if k == 0:
                    dp[j][k] = max(dp[j][k], dp[j-1][k] + b[i])
                else:    
                    dp[j][k] = max(dp[j][k], dp[j-1][k] + b[i], dp[j][k-1] + s[i])
print(dp[9][11])