from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = ['>', 'v', '<', '^']

def bfs(row, col):
    Q = deque([(row, col)])
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True
    while Q:
        curr_row, curr_col = Q.popleft()
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
                continue
            if arr[next_row][next_col] == '.' or visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            Q.append((next_row, next_col))
    return curr_row, curr_col


N, M = map(int, input().split())
arr = [input() for _ in range(N)]

find = False
for row in range(N):
    for col in range(M):
        if arr[row][col] == '#':
            sr, sc = bfs(row, col)
            find = True
            break
    if find:
        break

er, ec = bfs(sr, sc)
if sr < er or (sr == er and sc < ec):
    sr, sc, er, ec = er, ec, sr, sc

for d in range(4):
    next_r, next_c = sr + dr[d], sc + dc[d]
    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M:
        continue
    if arr[next_r][next_c] == '#':
        start_dir = d
        break

curr_row, curr_col, curr_dir = sr, sc, start_dir
start_dir = dir[start_dir]

print(curr_row+1, curr_col+1)
print(start_dir)

answer = ''
while curr_row != er or curr_col != ec:
    for d in range(4):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if next_row < 0 or N <= next_row or next_col < 0 or M <= next_col:
            continue
        if arr[next_row][next_col] == '#':
            if d == curr_dir:
                answer += 'A'
            elif d == (curr_dir + 1) % 4:
                answer += 'RA'
            elif d == (curr_dir - 1) % 4:
                answer += 'LA'
            else:
                continue
            curr_row, curr_col = curr_row + dr[d] * 2, curr_col + dc[d] * 2
            curr_dir = d
            break

print(answer)