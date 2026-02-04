n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

plane = [[0]*201 for _ in range(201)]

for i in range(n):
    color = 1 if i%2 else -1
    for x in range(x1[i]+100, x2[i]+100):
        for y in range(y1[i]+100, y2[i]+100):
            plane[x][y] = color
temp = 0
for col in range(201):
    for row in range(201):
        if plane[row][col]==1:
            temp += 1
print(temp)