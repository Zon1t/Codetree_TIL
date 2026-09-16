# 시작 3:56
# 달팽이 그리는 문제. 각 이동마다 먼지 퍼뜨리는 과정 잘하기.
# 델타 연산 잘해보기.


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def change_delta(delta_row, delta_col, d):
    if d == 0:
        return delta_row, delta_col
    elif d == 1:
        return -delta_col, delta_row
    elif d == 2:
        return -delta_row, -delta_col
    else:
        return delta_col, -delta_row


delta_lst = [
                              (-2, 0, 2),
                (-1, -1, 10), (-1, 0, 7), (-1, 1, 1),
    (0, -2, 5),
                (1, -1, 10),  (1, 0, 7),  (1, 1, 1),
                              (2, 0, 2)
]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

change_flag, cnt, wanna_be = False, 0, 1

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

center = N>>1
curr_row, curr_col, curr_dir = center, center, 0
answer = 0
while (curr_row, curr_col) != (0, 0):
    curr_row, curr_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    curr_munji = origin_munji = grid[curr_row][curr_col]
    for delta_row, delta_col, ratio in delta_lst:
        moving_munji = (origin_munji * ratio) // 100
        if not moving_munji:
            continue

        curr_munji -= moving_munji
        adjusted_dr, adjusted_dc = change_delta(delta_row, delta_col, curr_dir)
        next_row, next_col = curr_row + adjusted_dr, curr_col + adjusted_dc
        if not in_range(next_row, next_col):
            answer += moving_munji
        else:
            grid[next_row][next_col] += moving_munji

    next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    if not in_range(next_row, next_col):
        answer += curr_munji
    else:
        grid[next_row][next_col] += curr_munji

    cnt += 1
    if cnt == wanna_be:
        if change_flag:
            change_flag = False
            wanna_be += 1
        else:
            change_flag = True
        curr_dir = (curr_dir + 1) % 4
        cnt = 0

print(answer)