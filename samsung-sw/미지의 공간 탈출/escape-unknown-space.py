# 15:09
# 1. 시간의 벽에서의 탈출
#       - 각 face별로 이동을 잘 해야할 듯? 해당 과정은 하드코딩
#       - 도착 지점은 미리 세팅해두면 될 것
# 2. 미지의 공간에서의 탈출
#       - 도착 지점을 기점으로 bfs 진행
#       - 이상 현상의 경우 미리 격자 업데이트 해두기

from collections import deque

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
INF = float('inf')

from_to_face = [[3, 2, -1, 4],
                [2, 3, -1, 4],
                [0, 1, -1, 4],
                [1, 0, -1, 4],
                [0, 1,  2, 3]]


def in_range(row, col, bound):
    return 0 <= row < bound and 0 <= col < bound


def apply_obstacle(start_row, start_col, direction, velocity):
    obstacle_grid[start_row][start_col] = 0
    curr_row, curr_col, curr_time = start_row + dr[direction], start_col + dc[direction], velocity
    while in_range(curr_row, curr_col, N) and not space[curr_row][curr_col]:
        obstacle_grid[curr_row][curr_col] = min(obstacle_grid[curr_row][curr_col], curr_time)
        curr_row += dr[direction]
        curr_col += dc[direction]
        curr_time += velocity


def find():
    start_row, start_col = -1, -1
    for row in range(N):
        for col in range(N):
            if space[row][col] == 3:
                start_row, start_col = row, col
                break
        if start_row != -1:
            break

    for row in range(start_row-1, start_row+M+1):
        for col in range(start_col-1, start_col+M+1):
            if not in_range(row, col, N) or space[row][col]:
                continue

            start = (row, col)
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]

                if not in_range(next_row, next_col, N) or space[next_row][next_col] != 3:
                    continue

                if d == 0: return (1, M-1, next_row-start_row), start
                if d == 1: return (0, M-1, M-1-next_row+start_row), start
                if d == 2: return (3, M-1, M-1+start_col-next_col), start
                if d == 3: return (2, M-1, next_col-start_col), start


def convert(curr_face, curr_row, curr_col, direction):
    if curr_face < 4:
        if direction == 0: return curr_row, 0
        if direction == 1: return curr_row, M-1

        if curr_face == 0: return M-1-curr_col, M-1
        if curr_face == 1: return curr_col, 0
        if curr_face == 2: return M-1, curr_col
        if curr_face == 3: return 0, M-1-curr_col

    if direction == 0: return 0, M-1-curr_row
    if direction == 1: return 0, curr_row
    if direction == 2: return 0, curr_col
    if direction == 3: return 0, M-1-curr_col


def escape_wall():
    start_row, start_col = -1, -1
    for row in range(M):
        for col in range(M):
            if wall[4][row][col] == 2:
                start_row, start_col = row, col
                break
        if start_row != -1:
            break

    visited = [[[-1] * M for _ in range(M)] for _ in range(5)]
    visited[4][start_row][start_col] = 0

    Q = deque([(4, start_row, start_col)])
    while Q:
        curr_face, curr_row, curr_col = Q.popleft()

        if (curr_face, curr_row, curr_col) == WALL_EXIT:
            return visited[curr_face][curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col, M):
                next_face = from_to_face[curr_face][d]
                if next_face == -1: continue
                next_row, next_col = convert(curr_face, curr_row, curr_col, d)
            else:
                next_face = curr_face

            if visited[next_face][next_row][next_col] != -1 or wall[next_face][next_row][next_col]:
                continue
            visited[next_face][next_row][next_col] = visited[curr_face][curr_row][curr_col]+1
            Q.append((next_face, next_row, next_col))
    for face in range(5):
        for row in visited[face]:
            print(*row)
    return -1


def escape_space():
    curr_turn = answer + 1
    start_row, start_col = SPACE_START
    if obstacle_grid[start_row][start_col] <= curr_turn:
        return -1

    visited = [[-1] * N for _ in range(N)]
    visited[start_row][start_col] = curr_turn

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if space[curr_row][curr_col] == 4:
            return visited[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col, N) or space[next_row][next_col] in [1, 3]:
                continue
            if visited[next_row][next_col] != -1:
                continue
            if obstacle_grid[next_row][next_col] <= visited[curr_row][curr_col]+1:
                continue

            visited[next_row][next_col] = visited[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return -1


# =============================================================
# 세팅

N, M, F = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
wall = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]

obstacle_grid = [[INF]*N for _ in range(N)]
for _ in range(F):
    r, c, d, v = map(int, input().split())
    apply_obstacle(r, c, d, v)

WALL_EXIT, SPACE_START = find()

# ==============================================================
# 실행부

answer = escape_wall()
if answer != -1:
    answer = escape_space()

print(answer)