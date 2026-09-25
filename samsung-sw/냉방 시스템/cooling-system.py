# 10:33 시작   [] /
# 사전 세팅이 중요한 문제. 퍼지는 로직은 bfs로 만들기. 벽 처리는 grid로 해도 되고

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

deltas = [[(-1, -1), (-1, 0), (-1, 1)],
          [(-1, -1), (0, -1), (1, -1)],
          [(1, -1), (1, 0), (1, 1)],
          [(-1, 1), (0, 1), (1, 1)]]

check_lst = [[[(0, 0, -1), (1, 0, 0)], [(0, 0, 0)], [(0, 0, 1), (1, 0, 1)]],
              [[(0, 0, 0), (1, -1, 0)], [(1, 0, 0)], [(0, 1, 0), (1, 1, 0)]],
              [[(0, 1, -1), (1, 0, 0)], [(0, 1, 0)], [(0, 1, 1), (1, 0, 1)]],
              [[(0, 0, 0), (1, -1, 1)], [(1, 0, 1)], [(0, 1, 0), (1, 1, 1)]]]

direction_dict = {2: 1, 3: 0, 4: 3, 5: 2}


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def apply_aircond(row, col, d):
    visited = [[False] * N for _ in range(N)]

    start_row, start_col = row+dr[d], col+dc[d]
    if not in_range(start_row, start_col):
        return

    update_grid[start_row][start_col] += 5
    Q = deque([(start_row, start_col, 4)])
    while Q:
        curr_row, curr_col, write_num = Q.popleft()

        if write_num == 0:
            break

        for order, delta in enumerate(check_lst[d]):
            next_row, next_col = curr_row + deltas[d][order][0], curr_col + deltas[d][order][1]
            if not in_range(next_row, next_col) or visited[next_row][next_col]:
                continue

            for t, delta_row, delta_col in delta:
                check_row, check_col = curr_row + delta_row, curr_col + delta_col
                if wall_grid[t][check_row][check_col]:
                    break
            else:
                visited[next_row][next_col] = True
                update_grid[next_row][next_col] += write_num
                Q.append((next_row, next_col, write_num-1))


def make_cool():
    for row in range(N):
        for col in range(N):
            cool_grid[row][col] += update_grid[row][col]


def mix():
    delta_grid = [[0]*N for _ in range(N)]
    for curr_row in range(N):
        for curr_col in range(N):
            curr_cool = cool_grid[curr_row][curr_col]
            for d in range(2):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or wall_grid[d][curr_row][curr_col]:
                    continue
                next_cool = cool_grid[next_row][next_col]
                
                D = abs(curr_cool-next_cool) // 4
                if D:
                    delta_grid[curr_row][curr_col] -= D if curr_cool > next_cool else -D
                    delta_grid[next_row][next_col] += D if curr_cool > next_cool else -D
    
    for row in range(N):
        for col in range(N):
            cool_grid[row][col] += delta_grid[row][col]


def minus():
    for col in range(N):
        if cool_grid[0][col]:
            cool_grid[0][col] -= 1
        if cool_grid[-1][col]:
            cool_grid[-1][col] -= 1
    
    for row in range(1, N-1):
        if cool_grid[row][0]:
            cool_grid[row][0] -= 1
        if cool_grid[row][-1]:
            cool_grid[row][-1] -= 1


def check():
    for office_row, office_col in office:
        if cool_grid[office_row][office_col] < K:
            return False
    return True


def print_grid(what, grid):
    print('----', what, '----')
    for row in grid:
        print(*row)


# ===============================================================
# 세팅

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cool_grid = [[0]*N for _ in range(N)]
update_grid = [[0]*N for _ in range(N)]
office = []

wall_grid = [[[0]*N for _ in range(N)] for _ in range(2)]
for _ in range(M):
    r, c, d = map(int, input().split())
    wall_grid[d][r-1][c-1] = 1

for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            office.append((row, col))
        elif 2 <= grid[row][col] <= 5:
            apply_aircond(row, col, direction_dict[grid[row][col]])

answer = -1

# ==============================================================
# 실행부

for time in range(1, 101):
    # 1. 시원하게 만들기
    make_cool()

    # 2. 시원한 공기 섞기
    mix()

    # 3. 외벽 감소
    minus()

    # 4. 시원함 체크
    if check():
        answer = time
        break

# 정답 출력
print(answer)