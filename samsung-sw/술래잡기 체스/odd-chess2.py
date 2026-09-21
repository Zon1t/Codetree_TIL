# 11:32 시작
# 0, 0 잡고 시작.
# 도둑말은 빈칸이나 도둑말이 있는 칸으로 이동 가능. 이동 불가시 45 반시계로 돌면서 탐색. 없으면 그대로
# 술래말은 가진 방향에 대해서 한칸 이상 이동 가능 but 빈칸은 X. 이동 가능한 칸 없으면 종료
# custom_print 이쁘게 만드는거 연습하자.


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
hwasal = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']


def in_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4


def move(grid, info, SUL):
    return_grid = [row[:] for row in grid]
    doduk = [lst[:] for lst in info]

    for idx in range(1, 17):
        if not alive[idx]:
            continue

        curr_row, curr_col, curr_dir = doduk[idx]
        for delta_d in range(8):
            next_dir = (curr_dir + delta_d) % 8
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
            if not in_range(next_row, next_col) or (next_row, next_col) == SUL:
                continue

            next_idx = return_grid[next_row][next_col]
            if next_idx:
                doduk[next_idx][0], doduk[next_idx][1] = curr_row, curr_col
            doduk[idx] = [next_row, next_col, next_dir]
            return_grid[curr_row][curr_col], return_grid[next_row][next_col] = next_idx, idx

            break

    return return_grid, doduk


def backtrack(curr_row, curr_col, curr_dir, curr_score, curr_grid, curr_info):
    global answer
    if answer < curr_score:
        answer = curr_score

    next_grid, next_info = move(curr_grid, curr_info, (curr_row, curr_col))

    # print_grid(next_grid, next_info)
    for k in range(1, 4):
        next_row, next_col = curr_row+dr[curr_dir]*k, curr_col+dc[curr_dir]*k
        if not in_range(next_row, next_col) or next_grid[next_row][next_col] == 0:
            continue

        next_idx = next_grid[next_row][next_col]
        next_dir = next_info[next_idx][2]
        next_grid[next_row][next_col] = 0
        alive[next_idx] = False

        backtrack(next_row, next_col, next_dir, curr_score+next_idx, next_grid, next_info)

        next_grid[next_row][next_col] = next_idx
        alive[next_idx] = True


def print_grid(grid, info):
    print(f'----grid----')
    for row in grid:
        for component in row:
            if component:
                print(component, hwasal[info[component][2]], end=' ')
            else:
                print('   ', end=' ')
        print()


# ==================================================
# 세팅

doduk = [[] for _ in range(17)]
alive = [True] * 17
doduk_grid = [[0] * 4 for _ in range(4)]
for row in range(4):
    temp = list(map(int, input().split()))
    for col in range(4):
        p, d = temp[col*2], temp[col*2+1]-1
        doduk[p] = [row, col, d]
        doduk_grid[row][col] = p

idx = doduk_grid[0][0]
doduk_grid[0][0] = 0
alive[idx] = False

# ===================================================
# 실행부

answer = idx
backtrack(0, 0, doduk[idx][2], idx, doduk_grid, doduk)
print(answer)