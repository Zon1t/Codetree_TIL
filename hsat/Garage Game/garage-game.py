from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(row, col, grid, v):
    return_grid = [row[:] for row in grid]
    color = grid[row][col]
    cnt = 0
    min_row, max_row, min_col, max_col = row, row, col, col
    Q = deque([(row, col)])
    v[row-2*N][col] = True
    while Q:
        curr_row, curr_col = Q.popleft()
        return_grid[curr_row][curr_col] = 0
        cnt += 1

        if curr_row < min_row: min_row = curr_row
        if max_row < curr_row: max_row = curr_row
        if curr_col < min_col: min_col = curr_col
        if max_col < curr_col: max_col = curr_col

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if next_row < 2*N or 3*N <= next_row or next_col < 0 or N <= next_col:
                continue
            if v[next_row-2*N][next_col] or grid[next_row][next_col] != color:
                continue
            v[next_row-2*N][next_col] = True
            Q.append((next_row, next_col))

    return cnt, (max_row-min_row+1) * (max_col-min_col+1), return_grid


def apply_gravity(grid):
    for col in range(N):
        pointer = 3*N-1
        for row in range(3*N-1, -1, -1):
            if grid[row][col]:
                if row != pointer:
                    grid[row][col], grid[pointer][col] = grid[pointer][col], grid[row][col]
                pointer -= 1

def backtrack(stage, now_score, curr_grid):
    if stage == 3:
        global answer
        answer = max(answer, now_score)
        return

    temp = [row[:] for row in curr_grid]
    apply_gravity(temp)

    visited = [[False] * N for _ in range(N)]
    for row in range(2*N, 3*N):
        for col in range(N):
            if visited[row-2*N][col]:
                continue
            block_score, lectangle_score, next_grid = bfs(row, col, temp, visited)
            backtrack(stage+1, now_score+block_score+lectangle_score, next_grid)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(3*N)]
answer = 0
backtrack(0, 0, arr)
print(answer)