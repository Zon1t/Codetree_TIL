# 15:10 시작
# 플레이어들이 한 칸씩 이동. 이동 이후 독점 계약을 진행. k턴 동안 유지.
# 이동 우선순위를 잘 따져야 한다. 독점 계약을 맺지 않은 칸. -> 본인이 계약한 땅.
# 해당 칸이 여러개인 경우 우선순위를 따지기. 바라보고 있는 방향은 그 직전에 이동한 방향.
# 한 칸에 여럿 존재하는 경우 작은 플레이어만 살아남음. 살아 남은 애만 계약 진행하면 될듯


dr = [None, -1, 1, 0, 0]
dc = [None, 0, 0, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move():
    new_grid = [[0] * N for _ in range(N)]
    update_lst = []
    for human_idx in range(1, M+1):
        if not alive[human_idx]:
            continue

        curr_row, curr_col, curr_dir = human[human_idx]
        for d in priority[human_idx][curr_dir]:
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if dokjum[next_row][next_col][0] >= turn:
                continue
            next_dir = d
            break
        else:
            for d in priority[human_idx][curr_dir]:
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col):
                    continue
                if dokjum[next_row][next_col][1] == human_idx:
                    next_dir = d
                    break

        if new_grid[next_row][next_col]:
            alive[human_idx] = False
        else:
            human[human_idx] = (next_row, next_col, next_dir)
            new_grid[next_row][next_col] = human_idx
            update_lst.append((next_row, next_col, human_idx))

    for row, col, idx in update_lst:
        dokjum[row][col] = (turn+K, idx)

    return new_grid


def print_grid(grid):
    print(f'----grid----')
    for row in grid:
        print(*row)


# ====================================================================
# 세팅

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
directions = [None] + list(map(int, input().split()))
priority = [None] + [[None] + [list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
dokjum = [[(-1, -1) for _ in range(N)] for _ in range(N)]

human = [None] * (M+1)
alive = [True] * (M+1)
for row in range(N):
    for col in range(N):
        idx = grid[row][col]
        if not idx:
            continue
        human[idx] = (row, col, directions[idx])
        dokjum[row][col] = (K, idx)

# ===============================================================
# 실행부

answer = -1
for turn in range(1, 1000):
    # 1. 움직이기.
    grid = move()

    # 종료체크
    if sum(alive[1:]) == 1:
        answer = turn
        break

# 정답 출력
print(answer)