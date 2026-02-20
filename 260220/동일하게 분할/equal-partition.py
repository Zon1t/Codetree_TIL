n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

total = sum(arr)
if total%2:
    print('No')
else:
    temp = total//2
    dp = [False] * (temp+1)
    dp[0] = True
    for i in range(n):
        for j in range(temp, arr[i]-1, -1):
            if dp[j-arr[i]]:
                dp[j] = True
    if dp[-1]:
        print('Yes')
    else:
        print('No')