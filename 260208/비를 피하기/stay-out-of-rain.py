n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

start_list = []
answer_list = [[0]*n for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for row in range(n):
    for col in range(n):
        if grid[row][col] == 2:
            start_list.append((row, col))

for row, col in start_list:
    visited = [[False]*n for _ in range(n)]
    visited[row][col] = True
    q = deque([(row, col, 0)])
    while q:
        r, c, d = q.popleft()
        if grid[r][c] == 3:
            answer_list[row][col] = d
            break
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc, d+1))
                visited[nr][nc] = True
    if not answer_list[row][col]:
        answer_list[row][col] = -1
for row in answer_list:
    print(*(row))