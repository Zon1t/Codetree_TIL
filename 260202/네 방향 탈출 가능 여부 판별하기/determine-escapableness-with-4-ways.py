n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
q = [(0, 0)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
while q:
    r, c = q.pop(0)
    if (r, c) == (n-1, m-1):
        break
    for i in range(4):
        if 0 <= r + dr[i] < n and 0 <= c + dc[i] < m and not visited[r + dr[i]][c + dc[i]] and a[r + dr[i]][c + dc[i]]:
            q.append((r + dr[i], c + dc[i]))
            visited[r + dr[i]][c + dc[i]] = True
if visited[n-1][m-1]:
    print(1)
else:
    print(0)