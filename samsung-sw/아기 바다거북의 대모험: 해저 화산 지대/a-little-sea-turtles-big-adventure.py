# 전형적인 시키는거 잘하면 되는 시뮬레이션 문제.
# 1. 바다 거북의 이동. id가 작은 순서대로 바다 거북이 이동한다.
#       - 산호초, 화석, 다른 바다 거북이 있는 칸은 이동 불가.
#       - 이동 우선순위 : 우 - 하 - 좌 - 상
#       - 안식처(N-1, N-1) 도착시 도착시간 기록 및 제외.
#       - 이동 결과는 항상 반영한 채로 탐색함.

# 2. 화산 압력 증가. 모든 해저 화산의 마그마 압력 10씩 증가.
#       - 좌표를 따로 받아서 관리하면 될듯? dict 쓰자.

# 3. 분출 및 연쇄반응.
#       - 분출 임계치 이상이 되더라도 임계치 만큼의 열기가 발생함. **
#       - 열기는 한 칸 이동할 때마다 절반으로 줄어든다.
#       - 산호초 만나면 중단.
#       - 여러 화산의 열기가 도달하면 합산 -> 이건 grid 새로 만들어서 관리? 혹은 딕셔너리
#       - 연쇄 반응은 현재 마그마 압력 + 해당 칸에 누적된 외부 열기 >= 임계치를 만족해야 함.
#       - 열기 20 이상인 칸에 거북이가 있으면 화석이 됨.. 잔인

# 4. 환경 초기화.
#       - 열기 정보 지우기.
#       - 압력은 그대로 유지. -> 연쇄 반응 연산할 때 조건이 그래서 주어진 듯
#       - 환경 초기화는 따로 안 하도록 세팅

# 다 짜고 보니 뭔가 비효율적인 구석이 많다? 걍 건실하게 했으니 더 읽다가 11시 제출하기.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(idx):
    start_row, start_col = turtles[idx]
    if escape_time[idx] != -1 or turtle_grid[start_row][start_col] == -2:
        return

    dist_grid = [[-1]*N for _ in range(N)]
    dist_grid[-1][-1] = 0

    Q = deque([(N-1, N-1)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_row == start_row and curr_col == start_col:
            break

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or grid[next_row][next_col]:
                continue
            if turtle_grid[next_row][next_col] not in [-1, idx] or dist_grid[next_row][next_col] != -1:
                continue

            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    for d in range(4):
        next_row, next_col = start_row + dr[d], start_col + dc[d]

        if not in_range(next_row, next_col):
            continue

        if dist_grid[start_row][start_col]-1 == dist_grid[next_row][next_col]:
            turtles[idx] = (next_row, next_col)
            turtle_grid[start_row][start_col] = -1

            if next_row == N-1 and next_col == N-1:
                escape_time[idx] = turn
            else:
                turtle_grid[next_row][next_col] = idx

            return


def update_pressure():
    for mount_row, mount_col in mount_info.keys():
        curr_pressure, threshold = mount_info[(mount_row, mount_col)]
        if curr_pressure+10 >= threshold:
            active_lst.append((mount_row, mount_col))
        else:
            mount_info[(mount_row, mount_col)][0] += 10


def action():
    global active_lst
    if not active_lst:
        return

    hot_degree = [[0] * N for _ in range(N)]
    active_set = set()

    while active_lst:
        new_active = []

        for mount_row, mount_col in active_lst:
            if (mount_row, mount_col) in active_set:
                continue
            active_set.add((mount_row, mount_col))

            mount_info[(mount_row, mount_col)][0] = 0
            P = mount_info[(mount_row, mount_col)][1]
            hot_degree[mount_row][mount_col] += P

            Q = deque()
            for d in range(4):
                next_row, next_col = mount_row + dr[d], mount_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col]:
                    continue
                hot_degree[next_row][next_col] += P//2
                Q.append((next_row, next_col, d, P//2))
            while Q:
                curr_row, curr_col, curr_dir, curr_press = Q.popleft()
                if curr_press == 0:
                    continue

                next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
                if not in_range(next_row, next_col) or grid[next_row][next_col]:
                    continue
                hot_degree[next_row][next_col] += curr_press//2
                Q.append((next_row, next_col, curr_dir, curr_press//2))

        for mount_row, mount_col in mount_info.keys():
            if (mount_row, mount_col) in active_set:
                continue

            curr_pressure, threshold = mount_info[(mount_row, mount_col)]
            if curr_pressure + hot_degree[mount_row][mount_col] >= threshold:
                new_active.append((mount_row, mount_col))

        active_lst = new_active

    for turtle_row, turtle_col in turtles:
        if hot_degree[turtle_row][turtle_col] >= 20:
            turtle_grid[turtle_row][turtle_col] = -2


def print_state():
    print(f'-----{turn}-----')
    print(f'----turtle_pos----')
    for idx in range(M):
        print(*turtles[idx])
    print()
    print(f'----volc_info----')
    for k in mount_info.keys():
        press, thre = mount_info[k]
        print(f'curr_press: {press}, threshold: {thre}')
    print()
    print_grid('turtle', turtle_grid)


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)
    print()


# ============================================================
# 세팅

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

turtles = [tuple(map(int, input().split())) for _ in range(M)]
turtle_grid = [[-1] * N for _ in range(N)]
for i, (row, col) in enumerate(turtles):
    turtle_grid[row][col] = i
escape_time = [-1] * M

mount_info = {(row, col): [0, threshold] for row, col, threshold in [tuple(map(int, input().split())) for _ in range(K)]}
active_lst = []

# =============================================================
# 실행부

for turn in range(1, 101):
    # 1. 바다거북 이동하기
    for turtle_idx in range(M):
        move(turtle_idx)

    # 2. 화산 압력 증가
    update_pressure()

    # 3. 화산 분출 및 연쇄 반응
    action()

# 정답 출력
print('\n'.join(map(str, escape_time)))