n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def bfs(row, col):
    grid[row][col] += 1
    q = deque([(row, col)])
    s = 0
    while q:
        r, c = q.popleft()
        s += 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                grid[nr][nc] += 1
                q.append((nr, nc))
    s_list.append(s)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

s_list = []
count = 0
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            bfs(row, col)
            count += 1
s_list.sort()
print(count)
for i in s_list:
    print(i)