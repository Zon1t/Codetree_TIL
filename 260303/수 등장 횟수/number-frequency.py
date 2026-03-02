n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.

cnt_dict = dict()

for num in arr:
    if cnt_dict.get(num):
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1

for num in nums:
    print(cnt_dict[num] if cnt_dict.get(num) else 0, end = ' ')