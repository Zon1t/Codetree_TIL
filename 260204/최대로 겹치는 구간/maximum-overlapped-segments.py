n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
nl = [0] * 201

for start, end in segments:
    for i in range(start+100, end+101):
        nl[i] += 1
print(max(nl))