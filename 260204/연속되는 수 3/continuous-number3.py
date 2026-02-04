N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

def is_plus(num):
    return num > 0

cnt = 1
max_cnt = 0
for i in range(N):
    if i != 0 and (is_plus(arr[i]) == is_plus(arr[i-1])):
        cnt += 1
    else:
        max_cnt = cnt if max_cnt < cnt else max_cnt
        cnt = 1
max_cnt = cnt if max_cnt < cnt else max_cnt
print(max_cnt)