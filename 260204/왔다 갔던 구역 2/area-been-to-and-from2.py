n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

nl = [0] * 2001
now_position = 1001
for i in range(n):
    if dir[i] == 'R':
        for pos in range(now_position, now_position + x[i]):
            nl[pos] += 1
        now_position += x[i]
    else:
        for pos in range(now_position - x[i], now_position):
            nl[pos] += 1
        now_position -= x[i]
temp = 0
for i in nl:
    if i >= 2:
        temp += 1
print(temp)