x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

plane = [[0] * 2001 for _ in range(2001)]
for x in range(x1[0]+1000, x2[0]+1000):
    for y in range(y1[0]+1000, y2[0]+1000):
        plane[x][y] = 1
for x in range(x1[1]+1000, x2[1]+1000):
    for y in range(y1[1]+1000, y2[1]+1000):
        plane[x][y] = 0

minx = 2000
maxx = 0
miny = 2000
maxy = 0

for x in range(2001):
    for y in range(2001):
        if plane[x][y]:
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)

print((maxx-minx+1)*(maxy-miny+1))