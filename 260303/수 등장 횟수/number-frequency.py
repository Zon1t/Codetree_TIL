n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.

cnt_arr = [0] * 100001

for num in arr:
    cnt_arr[num] += 1

for num in nums:
    print(cnt_arr[num], end=' ')