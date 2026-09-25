# [] / 11:24 시작
# 포인터 사용해서 문제 풀이하기. 머리 사람 위치만 기록. 정방향 역방향 여부 판단.
# 공 던지기 완탐 잘하기.


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def write(row, col):
    start_row, start_col = row, col
    group_grid[start_row][start_col] = group_idx
    order_grid[start_row][start_col] = 0

    for d in range(4):
        curr_row, curr_col = start_row + dr[d], start_col + dc[d]
        if not in_range(curr_row, curr_col):
            continue
        if grid[curr_row][curr_col] == 2:
            group_grid[curr_row][curr_col] = group_idx
            order_grid[curr_row][curr_col] = 1
            break

    curr_idx = curr_cnt = 2
    while True:
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or group_grid[next_row][next_col] != -1:
                continue
            if not grid[next_row][next_col]:
                continue

            if grid[next_row][next_col] != 4:
                curr_cnt += 1

            group_grid[next_row][next_col] = group_idx
            order_grid[next_row][next_col] = curr_idx
            curr_row, curr_col = next_row, next_col
            curr_idx += 1
            break
        else:
            break

    human_cnt[group_idx] = curr_cnt
    length[group_idx] = curr_idx


def move_head():
    for idx in range(M):
        heads[idx] = (heads[idx] + (-1 if init_dir[idx] else 1)) % length[idx]


def is_there_human(curr_row, curr_col):
    global answer
    curr_group, curr_index = group_grid[curr_row][curr_col], order_grid[curr_row][curr_col]
    curr_order = ((curr_index - heads[curr_group]) * (1 if init_dir[curr_group] else -1)) % length[curr_group]
    if curr_order < human_cnt[curr_group]:
        answer += (curr_order+1) ** 2
        heads[curr_group] = (heads[curr_group]+(human_cnt[curr_group]-1 if init_dir[curr_group] else 1-human_cnt[curr_group])) % length[curr_group]
        init_dir[curr_group] ^= True
        return True
    return False


def throw_ball(status, order):
    if status == 0:
        for col in range(N):
            if group_grid[order][col] != -1 and is_there_human(order, col):
                return
    elif status == 1:
        for row in range(N-1, -1, -1):
            if group_grid[row][order] != -1 and is_there_human(row, order):
                return
    elif status == 2:
        for col in range(N-1, -1, -1):
            if group_grid[-1-order][col] != -1 and is_there_human(-1-order, col):
                return
    else:
        for row in range(N):
            if group_grid[row][-1-order] != -1 and is_there_human(row, -1-order):
                return


def print_grid(what, grid):
    print('----', what, '----')
    for row in grid:
        print(*row)


# =================================================================
# 사전 세팅

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
period = N << 2

group_grid = [[-1]*N for _ in range(N)]
order_grid = [[-1]*N for _ in range(N)]
human_cnt = [-1]*M
length = [-1]*M

group_idx = -1
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            group_idx += 1
            write(row, col)

init_dir = [True] * M
heads = [0] * M
answer = 0

# =================================================================
# 실행부

for turn in range(K):
    # 1. 머리사람 이동
    move_head()

    # 2. 공 던지기
    throw_ball((turn%period)//N, turn%N)

# 정답 출력
print(answer)