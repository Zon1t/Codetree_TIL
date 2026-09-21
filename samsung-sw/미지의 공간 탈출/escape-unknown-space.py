# 1. 시간의 벽 탈출. 출구가 하나이므로 시간의 벽을 탈출하는 것이 우선시 되어야 한다.
# 2. 미지의 공간 탈출. 탈출구 4로 이동해야 한다.
# 이 두 가지를 메인 목표로 하여 차근차근 해결해나가보자.

# bfs 응용 문제. 시간의 벽은 입체이므로 면과 면 사이의 이동에 대해서 유의해야 한다..
# from_to_mat을 정의. from_to_mat[curr_grid][direction] = next_grid 이런 식으로 정의하면 될 듯?
# 좌표는 어쩌게? 하드 코딩하면 되긴 할듯..? 더 쉬운 방법? 없으면 걍 하드코딩 ㄱㄱ
# 이상 현상을 따로 grid 만들어서 관리해도 될 듯. 근데 이상현상이 시간의 벽 타고 올라갈 수도 있음?
# 위 경우는 어짜피 탈출 불가니까 생각하지 말아야겠다. turn <= ob_grid[row][col] 이면 못지나감.
# 구현 들어가 보자. 설계 하다보면 보이겠지.


from collections import deque

INF = float('inf')
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 0,  1,  2, 3, 4
# 동, 서, 남, 북, 윗 순서 고려 잘하기.
from_to_mat = [[3, 2, -1, 4],
               [2, 3, -1, 4],
               [0, 1, -1, 4],
               [1, 0, -1, 4],
               [0, 1, 2, 3]]


def in_ragne(row, col, bound):
    return 0 <= row < bound and 0 <= col < bound


def apply_ob(sr, sc, d, t):
    curr_row, curr_col, curr_time = sr, sc, 0
    while in_ragne(curr_row, curr_col, N) and space_grid[curr_row][curr_col] == 0:
        ob_grid[curr_row][curr_col] = min(ob_grid[curr_row][curr_col], curr_time)

        curr_row, curr_col = curr_row + dr[d], curr_col + dc[d]
        curr_time += t


def find_wall_pos():
    for row in range(N):
        for col in range(N):
            if space_grid[row][col] == 3:
                return row, col

def find_wall_exit():
    for row in range(wall_sr-1, wall_sr+M+1):
        for col in range(wall_sc-1, wall_sc+M+1):

            if not in_ragne(row, col, N) or space_grid[row][col] in (1, 3):
                continue

            for direction in range(4):
                next_row, next_col = row+dr[direction], col+dc[direction]

                if not in_ragne(next_row, next_col, N) or space_grid[next_row][next_col] != 3:
                    continue

                if direction == 0: return (1, M-1, row-wall_sr), (row, col)
                if direction == 1: return (0, M-1, M-1-row+wall_sr), (row, col)
                if direction == 2: return (3, M-1, M-1-col+wall_sc), (row, col)
                if direction == 3: return (2, M-1, col-wall_sc), (row, col)


def find_start():
    for row in range(M):
        for col in range(M):
            if wall_grid[4][row][col] == 2:
                return row, col


def convert(curr_grid, curr_row, curr_col, direction):
    if curr_grid == 0:
        if direction == 0: return curr_row, 0
        if direction == 1: return curr_row, M-1
        if direction == 3: return M-1-curr_col, M-1
    if curr_grid == 1:
        if direction == 0: return curr_row, 0
        if direction == 1: return curr_row, M-1
        if direction == 3: return curr_col, 0
    if curr_grid == 2:
        if direction == 0: return curr_row, 0
        if direction == 1: return curr_row, M-1
        if direction == 3: return M-1, curr_col
    if curr_grid == 3:
        if direction == 0: return curr_row, 0
        if direction == 1: return curr_row, M-1
        if direction == 3: return 0, M-1-curr_col
    if curr_grid == 4:
        if direction == 0: return 0, M-1-curr_row
        if direction == 1: return 0, curr_row
        if direction == 2: return 0, curr_col
        if direction == 3: return 0, M-1-curr_col


def escape_wall():
    dist_grid = [[[-1]*M for _ in range(M)] for _ in range(5)]
    dist_grid[4][start_row][start_col] = 0

    Q = deque([(4, start_row, start_col)])
    while Q:
        curr_grid, curr_row, curr_col = Q.popleft()

        if (curr_grid, curr_row, curr_col) == EXIT:
            return dist_grid[curr_grid][curr_row][curr_col]

        for d in range(4):
            next_grid, next_row, next_col = curr_grid, curr_row+dr[d], curr_col+dc[d]

            if not in_ragne(next_row, next_col, M):
                next_grid = from_to_mat[curr_grid][d]
                if next_grid == -1: continue
                next_row, next_col = convert(curr_grid, curr_row, curr_col, d)

            if dist_grid[next_grid][next_row][next_col] != -1 or \
                wall_grid[next_grid][next_row][next_col]:
                continue

            dist_grid[next_grid][next_row][next_col] = dist_grid[curr_grid][curr_row][curr_col]+1
            Q.append((next_grid, next_row, next_col))

    return -1


def escape_space():
    start_row, start_col = START
    visited = [[-1] * N for _ in range(N)]
    visited[start_row][start_col] = answer+1

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if space_grid[curr_row][curr_col] == 4:
            return visited[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row+dr[d], curr_col+dc[d]
            if not in_ragne(next_row, next_col, N) or visited[next_row][next_col] != -1:
                continue
            if space_grid[next_row][next_col] in (1, 3) or visited[curr_row][curr_col]+1 >= ob_grid[next_row][next_col]:
                continue

            visited[next_row][next_col] = visited[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return -1


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


def print_status():
    print(f'----EXIT----')
    print(EXIT)
    print(f'----start_coordinate----')
    print(*START)


# ================================================================================
# 세팅

N, M, F = map(int, input().split())
space_grid = [list(map(int, input().split())) for _ in range(N)]
wall_grid = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
wall_sr, wall_sc = find_wall_pos()

ob_grid = [[INF] * N for _ in range(N)]
for _ in range(F):
    sr, sc, d, t = map(int, input().split())
    apply_ob(sr, sc, d, t)

start_row, start_col = find_start()
EXIT, START = find_wall_exit()

# ==============================================================
# 실행부

answer = escape_wall()
if answer != -1:
    answer = escape_space()

# 정답 출력
print(answer)