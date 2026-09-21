# 시작 19:38
# 업기 처리를 잘해야 할 것 같다. 올려두는거? 그냥 append처리 하면 될듯?
# 파란칸 & 격자 밖 동일하게 처리.
# 빨간칸 뒤집기 잘하기

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(idx):
    curr_row, curr_col, curr_dir = mal_info[idx]
    next_row, next_col, next_dir = curr_row + dr[curr_dir], curr_col + dc[curr_dir], curr_dir
    if not in_range(next_row, next_col) or color_grid[next_row][next_col] == 2:
        next_dir ^= 1
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

    mal_info[idx][2] = next_dir
    if in_range(next_row, next_col) and color_grid[next_row][next_col] < 2:
        start_idx = mal_grid[curr_row][curr_col].index(idx)
        move_object = mal_grid[curr_row][curr_col][start_idx:] if color_grid[next_row][next_col] == 0 else \
            mal_grid[curr_row][curr_col][start_idx:][::-1]
        mal_grid[curr_row][curr_col] = mal_grid[curr_row][curr_col][:start_idx]
        for move_idx in move_object:
            mal_info[move_idx][0], mal_info[move_idx][1] = next_row, next_col
        mal_grid[next_row][next_col].extend(move_object)
    else:
        next_row, next_col = curr_row, curr_col
    return len(mal_grid[next_row][next_col])


# ==============================================================
# 세팅

N, K = map(int, input().split())
color_grid = [list(map(int, input().split())) for _ in range(N)]

mal_grid = [[[] for _ in range(N)] for _ in range(N)]
mal_info = [None] * K
for idx in range(K):
    r, c, d = map(lambda x: int(x)-1, input().split())
    mal_grid[r][c] = [idx]
    mal_info[idx] = [r, c, d]

# ==============================================================
# 실행부

answer = -1
for turn in range(1, 1001):
    for i in range(K):
        if move(i) >= 4:
            answer = turn
            break
    else:
        continue
    break
print(answer)