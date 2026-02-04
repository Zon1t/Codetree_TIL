n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

nl = [[0, 0] for _ in range(200001)]
color_list = [0] * 200001
now_pos = 100001

for i in range(n):
    if dir[i] == 'R':
        for pos in range(now_pos, now_pos + x[i]):
            color_list[pos] = 1
            nl[pos][0] += 1
        now_pos += x[i]-1
    else:
        for pos in range(now_pos, now_pos - x[i], -1):
            color_list[pos] = -1
            nl[pos][1] += 1
        now_pos -= x[i]-1

b, w, g = 0, 0, 0
for i in range(200001):
    if nl[i][0] >= 2 and nl[i][1] >= 2:
        g += 1
    else:
        if color_list[i] == 1:
            b += 1
        elif color_list[i] == -1:
            w += 1
print(w, b, g)