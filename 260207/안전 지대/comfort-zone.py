n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def find_safe_zone(row, col):
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] != 0:
                q.append((nr, nc))
                visited[nr][nc] = True

max_count = 0
max_count_height = 1

for h in range(1, 101):
    for row in range(n):
        for col in range(m):
            if grid[row][col] <= h:
                grid[row][col] = 0
    temp = 0
    visited = [[False]*m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if grid[row][col] and not visited[row][col]:
                find_safe_zone(row, col)
                temp += 1
    if max_count < temp:
        max_count = temp
        max_count_height = h
print(max_count_height, max_count)