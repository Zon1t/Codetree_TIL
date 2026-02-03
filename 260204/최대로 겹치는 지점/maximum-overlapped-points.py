n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
nl = [0]*101
for start, end in segments:
    for i in range(start, end+1):
        nl[i] += 1
print(max(nl))