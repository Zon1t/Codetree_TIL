n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

from collections import deque

def find_block(row, col, val):
    global large_block

    q = deque([(row, col)])
    s = 0
    visited[row][col] = True

    while q:
        r, c = q.popleft()
        s += 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == val:
                q.append((nr, nc))
                visited[nr][nc] = True
    if large_block < s:
        large_block = s
    return s >= 4

visited = [[False]*n for _ in range(n)]
count = 0
large_block = 0

for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            if find_block(row, col, grid[row][col]):
                count += 1
print(count, large_block)