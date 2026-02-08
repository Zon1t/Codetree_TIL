n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.

from collections import deque

def select_wall(start, temp_list):
    if len(temp_list) == k:
        broken_wall_comb.append(temp_list[:])
        return
    for i in range(start, len(wall_list)):
        temp_list.append(wall_list[i])
        select_wall(i+1, temp_list)
        temp_list.pop()

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = -1

wall_list = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]
broken_wall_comb = []
select_wall(0, [])
for broken_wall_list in broken_wall_comb:
    visited = [[False]*n for _ in range(n)]
    visited[r1][c1] = True
    q = deque([(r1, c1, 0)])
    while q:
        r, c, d = q.popleft()
        if (r, c) == (r2, c2):
            if answer != -1:
                answer = min(answer, d)
            else:
                answer = d
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] == 0 or (nr, nc) in broken_wall_list:
                    q.append((nr, nc, d+1))
                    visited[nr][nc] = True
print(answer)