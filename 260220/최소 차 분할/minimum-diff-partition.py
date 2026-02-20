n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)
temp = total//2
dp = [False] * (temp+1)
dp[0] = True
for num in arr:
    for i in range(temp, num-1, -1):
        if dp[i-num]:
            dp[i] = True
A_value = 0
for i in range(temp, -1, -1):
    if dp[i]:
        A_value = i
        break

print(total-A_value-A_value)