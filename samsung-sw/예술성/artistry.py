# 15:17 시작
# 굉장히 귀찮은 문제. 돌리는 로직 잘 짜기. 인접한 변의 수, 그룹 별 개수 카운팅 잘하면 되는 문제이다.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_info(start_row, start_col, curr_group, group_grid):
    return_info = dict()
    lst = [(start_row, start_col)]
    pointer, cnt = 0, 1
    while pointer < cnt:
        curr_row, curr_col = lst[pointer]
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col):
                continue

            next_group = group_grid[next_row][next_col]
            if next_group:
                if next_group != curr_group:
                    return_info[group_grid[next_row][next_col]] = return_info.get(group_grid[next_row][next_col], 0) + 1
            else:
                if grid[next_row][next_col] == grid[curr_row][curr_col]:
                    group_grid[next_row][next_col] = curr_group
                    lst.append((next_row, next_col))
                    cnt += 1
        pointer += 1

    return return_info, cnt


def calc_beauty():
    group_grid = [[0] * N for _ in range(N)]
    curr_group, acc_sum, group_cnt = 0, 0, [None]
    for row in range(N):
        for col in range(N):
            if group_grid[row][col]:
                continue

            curr_group += 1
            group_grid[row][col] = curr_group

            info, cnt = get_info(row, col, curr_group, group_grid)
            group_cnt.append((cnt, grid[row][col]))

            for neighbor_idx, line_cnt in info.items():
                neighbor_cnt, value = group_cnt[neighbor_idx]
                acc_sum += (cnt + neighbor_cnt) * grid[row][col] * value * line_cnt

    return acc_sum


def rotate_center():
    for k in range(1, center+1):
        temp = grid[center-k][center]
        grid[center-k][center] = grid[center][center+k]
        grid[center][center+k] = grid[center+k][center]
        grid[center+k][center] = grid[center][center-k]
        grid[center][center-k] = temp


def rotate_side(sr, sc):
    temp = [row[sc:sc+center] for row in grid[sr:sr+center]]
    temp = [row[::-1] for row in zip(*temp)]
    for row in range(center):
        for col in range(center):
            grid[sr+row][sc+col] = temp[row][col]


# ===============================================================
# 세팅

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
center = N >> 1

# ===============================================================
# 실행부

answer = 0
for i in range(4):
    # 1. 예술성 평가
    answer += calc_beauty()

    if i == 3:
        break

    # 2. 회전
    rotate_center()
    rotate_side(0, 0)
    rotate_side(center+1, 0)
    rotate_side(0, center+1)
    rotate_side(center+1, center+1)

# 정답 출력
print(answer)