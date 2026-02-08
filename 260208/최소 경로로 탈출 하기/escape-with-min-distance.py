n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

distance_matrix = [[-1]*m for _ in range(n)]
distance_matrix[0][0] = 0
answer = -1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

q = deque([(0, 0, 0)])
while q:
    r, c, d = q.popleft()
    if (r, c) == (n-1, m-1):
        answer = d
        break
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < m and a[nr][nc] and distance_matrix[nr][nc] == -1:
            q.append((nr, nc, d+1))
            distance_matrix[nr][nc] = d+1
print(answer)