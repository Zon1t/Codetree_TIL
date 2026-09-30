# 15:03
# 정령은 골렘을 타고 내려옴. 내려오는 과정에서의 로직을 올바르게 구현할 필요가 있음.
# 아래 칸을 기준으로 델타 리스트를 만들어서 체크해가면 될 것 같다.
# 그룹핑 결과 + bfs를 활용하여 최남단으로 이동하기.

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

delta_lst = [[(0, -1), (0, 1), (1, 0)],
             [(-2, -1), (-1, -2), (0, -1), (0, -2), (1, -1)],
             [(-2, 1), (-1, 2), (0, 1), (0, 2), (1, 1)]]


def in_range(row, col):
    return 0 <= row < N+3 and 0 <= col < M


def check(curr_row, curr_col, delta_idx):
    for delta_row, delta_col in delta_lst[delta_idx]:
        next_row, next_col = curr_row + delta_row, curr_col + delta_col
        if not in_range(next_row, next_col) or grid[next_row][next_col]:
            return False
    return True


def drop(start_col, direction):
    curr_row, curr_col, curr_dir = 2, start_col, direction
    while True:
        for delta_idx in range(3):
            if check(curr_row, curr_col, delta_idx):
                curr_row += 1
                if delta_idx == 1:
                    curr_col, curr_dir = curr_col-1, (curr_dir-1) % 4
                elif delta_idx == 2:
                    curr_col, curr_dir = curr_col+1, (curr_dir+1) % 4
                break
        else:
            break

    if curr_row <= 4:
        clear()
        return None, None

    curr_row -= 1

    grid[curr_row][curr_col] = 1
    group_grid[curr_row][curr_col] = curr_group
    for d in range(4):
        next_row, next_col = curr_row+dr[d], curr_col+dc[d]
        grid[next_row][next_col] = 2 if d == curr_dir else 1
        group_grid[next_row][next_col] = curr_group

    return curr_row, curr_col


def bfs(start_row, start_col):
    visited = [[False] * M for _ in range(N+3)]
    visited[start_row][start_col] = True

    max_row = start_row
    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or visited[next_row][next_col] or not grid[next_row][next_col]:
                continue
            if grid[curr_row][curr_col] != 2 and group_grid[curr_row][curr_col] != group_grid[next_row][next_col]:
                continue

            visited[next_row][next_col] = True
            Q.append((next_row, next_col))
            max_row = max(max_row, next_row)

    return max_row-2


def clear():
    for row in range(N+3):
        for col in range(M):
            grid[row][col] = 0


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# =======================================================================
# 세팅

N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N+3)]
group_grid = [[0] * M for _ in range(N+3)]
answer = 0

# ========================================================================
# 실행부

for curr_group in range(1, K+1):
    # 1. 골렘 떨구기
    c, d = map(int, input().split())
    start_row, start_col = drop(c-1, d)

    # 2. 정령 탈출하기.
    answer += bfs(start_row, start_col) if start_row is not None else 0

# 정답 출력하기
print(answer)