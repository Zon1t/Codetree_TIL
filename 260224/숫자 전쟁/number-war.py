n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

# Please write your code here.

dp = [[-1]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        dp[i+1][j+1] = max(dp[i][j], dp[i+1][j+1])
        if first_cards[i] > second_cards[j]:
            dp[i][j+1] = max(dp[i][j] + second_cards[j], dp[i][j+1])
        elif first_cards[i] < second_cards[j]:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])
print(max([max(row) for row in dp]))
