n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((b, a))
# Please write your code here.

data.sort()

cnt = 0
now_end = 0
for end, start in data:
    if now_end < start:
        cnt += 1
        now_end = end
print(cnt)