n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

nl = [0] * 200001
now_pos = 100001

for i in range(n):
    if dir[i] == 'R':
        for pos in range(now_pos, now_pos+x[i]):
            nl[pos] = 1
        now_pos += x[i]-1
    else:
        for pos in range(now_pos-x[i]+1, now_pos+1):
            nl[pos] = -1
        now_pos -= x[i]-1
w = b = 0
for i in nl:
    if i == 1:
        b += 1
    elif i == -1:
        w += 1
print(w, b)