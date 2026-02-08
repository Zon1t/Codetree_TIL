n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# not visited and grid 값이 1인 경우 -> -2로 변환 출력
# 처음 0인 부분도 따로 받아서 나중에 -1처리..?

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

start_points = []

for row in range(n):
    for col in range(n):
        if grid[row][col] == 2:
            start_points.append((row, col, 0))

visited = [[False]*n for _ in range(n)]
for r, c, _ in start_points:
    visited[r][c] = True

q = deque(start_points[:])
while q:
    r, c, t = q.popleft()
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
            grid[nr][nc] = t+1
            visited[nr][nc] = True
            q.append((nr, nc, t+1))

for row in range(n):
    for col in range(n):
        if grid[row][col]==0:
            grid[row][col] = -1
        elif grid[row][col]==1 and not visited[row][col]:
            grid[row][col] = -2

for r, c, _ in start_points:
    grid[r][c] = 0

for row in grid:
    print(*(row))