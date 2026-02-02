n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

visited = [[False]*n for _ in range(n)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

from collections import deque

q = deque([])
for point in points:
    q.append((point[0]-1, point[1]-1))

while q:
    row, col = q.popleft()
    visited[row][col] = True

    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
            q.append((nr, nc))
            visited[nr][nc] = True
total = 0
for i in visited:
    total += sum(i)
print(total)