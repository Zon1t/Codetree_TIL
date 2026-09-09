# 0 : 빈칸, 1 : 사무실, 2~5 : 왼 위 오 아
# 에어컨이 있는 장소는 동일. 즉 update_matrix를 만들어서 매 분 추가해주는 느낌으로 진행하면
# 될 것 같다? 아예 턴마다 연산해주는 느낌으로.. 기본 grid는 냄겨두고.. 진행할까 싶기도 하다.
# 시원함 정도를 잘 업데이트 해주는 것이 좋다. 벽 있는 경우 처리에 대해서도 잘 생각해볼 필요가 있다.
# 벽도 패턴화해서 업데이트하면 될듯? 틀을 짜보자

from collections import deque


dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
# 에어컨 진행방향
delta_lst = [[(-1, -1), (0, -1), (1, -1)],
             [(-1, -1), (-1, 0), (-1, 1)],
             [(-1, 1), (0, 1), (1, 1)],
             [(1, -1), (1, 0), (1, 1)]]

# 전파 방향에 대해서 확인할 벽의 타입과 상대 좌표를 미리 담아둠. 왼, 위, 오, 아 순서
# (type, row, col)의 양식을 가짐.
check_lst = [[[(0, 0, 0), (1, -1, 0)], [(1, 0, 0)], [(0, 1, 0), (1, 1, 0)]],
             [[(0, 0, -1), (1, 0, 0)], [(0, 0, 0)], [(0, 0, 1), (1, 0, 1)]],
             [[(0, 0, 0), (1, -1, 1)], [(1, 0, 1)], [(0, 1, 0), (1, 1, 1)]],
             [[(0, 1, -1), (1, 0, 0)], [(0, 1, 0)], [(0, 1, 1), (1, 0, 1)]]]
for_mix = [(1, 0), (0, 1)]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 에어컨 인접해 벽X + 격자 벗어남X 를 잘 이용해보자.
def make_update_grid(d, r, c):
    temp = [[0] * N for _ in range(N)]
    start_row, start_col = r + dr[d], c + dc[d]
    temp[start_row][start_col] = 5

    Q = deque([(start_row, start_col, 5)])
    while Q:
        curr_row, curr_col, curr_num = Q.popleft()

        if curr_num == 1:
            break

        for order, (delta_row, delta_col) in enumerate(delta_lst[d]):
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            if not in_range(next_row, next_col):
                continue

            for wt, ddr, ddc in check_lst[d][order]:
                check_row, check_col = curr_row + ddr, curr_col + ddc
                if (check_row, check_col) in (wall_type0 if wt == 0 else wall_type1):
                    break
            else:
                temp[next_row][next_col] = curr_num-1
                Q.append((next_row, next_col, curr_num-1))

    for row in range(N):
        for col in range(N):
            update_grid[row][col] += temp[row][col]


def update():
    for row in range(N):
        for col in range(N):
            air_grid[row][col] += update_grid[row][col]

# 벽 사이 로직을 구현 안했다.. 또 안읽네
def mix():
    temp = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            curr_air = air_grid[row][col]
            for idx, (delta_row, delta_col) in enumerate(for_mix):
                next_row, next_col = row + delta_row, col + delta_col
                if not in_range(next_row, next_col):
                    continue
                if idx == 0 and (next_row, next_col) in wall_type0:
                    continue
                if idx == 1 and (next_row, next_col) in wall_type1:
                    continue

                next_air = air_grid[next_row][next_col]
                D = abs(next_air-curr_air) // 4
                if D:
                    temp[row][col] += D if curr_air < next_air else -D
                    temp[next_row][next_col] -= D if curr_air < next_air else -D

    for row in range(N):
        for col in range(N):
            air_grid[row][col] += temp[row][col]


def reduce():
    for row in range(N):
        if air_grid[row][0]:
            air_grid[row][0] -= 1
        if air_grid[row][-1]:
            air_grid[row][-1] -= 1
    for col in range(1, N-1):
        if air_grid[0][col]:
            air_grid[0][col] -= 1
        if air_grid[-1][col]:
            air_grid[-1][col] -= 1


def check():
    for curr_row, curr_col in office:
        if air_grid[curr_row][curr_col] < K:
            return False
    return True


def print_grid():
    print(f'----air_grid----')
    for row in air_grid:
        print(*row)


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
office, air_cond = [], []
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            office.append((row, col))
        elif 2 <= grid[row][col] <= 5:
            air_cond.append((grid[row][col]-2, row, col))

wall_type0, wall_type1 = set(), set()
for _ in range(M):
    r, c, t = map(int, input().split())
    if t == 0:
        wall_type0.add((r-1, c-1))
    else:
        wall_type1.add((r-1, c-1))

update_grid = [[0] * N for _ in range(N)]
for d, r, c in air_cond:
    make_update_grid(d, r, c)

air_grid = [[0] * N for _ in range(N)]

answer = -1
for turn in range(1, 101):
    # 시원함 업데이트.
    update()

    # 공기 섞기.
    mix()

    # 외벽 감소
    reduce()

    # 종료 체크
    if check():
        answer = turn
        break

# 정답 출력
print(answer)