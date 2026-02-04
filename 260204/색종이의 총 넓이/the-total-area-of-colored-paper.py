n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

plane = [[0]*201 for _ in range(201)]

for i in range(n):
    for c in range(x[i]+100, x[i]+108):
        for r in range(y[i]+100, y[i]+108):
            plane[r][c] = 1
print(sum([sum(row) for row in plane]))