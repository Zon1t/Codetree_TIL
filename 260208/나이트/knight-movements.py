n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.

from collections import deque

dr = [-1, 1, 2, 2, 1, -1, -2, -2]
dc = [2, 2, 1, -1, -2, -2, -1, 1]

answer = -1
visited = [[False]*n for _ in range(n)]
visited[r1-1][c1-1] = True
q = deque([(r1-1, c1-1, 0)])
while q:
    r, c, t = q.popleft()
    if (r, c) == (r2-1, c2-1):
        answer = t
        break
    for i in range(8):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            q.append((nr, nc, t+1))
            visited[nr][nc] = True
print(answer)