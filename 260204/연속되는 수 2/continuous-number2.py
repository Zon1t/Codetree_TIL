n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt = 1
max_cnt = 0
for i in range(n):
    if i != 0 and arr[i] == arr[i-1]:
        cnt += 1
    else:
        max_cnt = cnt if max_cnt < cnt else max_cnt
        cnt = 1
max_cnt = cnt if max_cnt < cnt else max_cnt
print(max_cnt)