n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cnt = 0
max_cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        max_cnt = cnt if max_cnt < cnt else max_cnt
        cnt = 0
print(cnt if max_cnt < cnt else max_cnt)