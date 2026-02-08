n = int(input())

# Please write your code here.

# 특정 숫자를 고정할 수 있다고 생각
# -> if n = 4, 1이 제일 위에 있는 경우 -> 5 가지
# 2가 제일 위에 있는 경우 -> 1 * 2 가지
# 3이 제일 위에 있는 경우 -> 2 * 1 가지
# 4가 제일 위에 있는 경우 -> 5 * 1 가지
# 이런 식으로..

dp = [1, 1, 2, 5]
for i in range(4, n+1):
    temp = 0
    for j in range(i):
        temp += dp[-1-j] * dp[j]
    dp.append(temp)
print(dp[n])