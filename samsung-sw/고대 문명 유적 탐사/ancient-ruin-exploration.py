# 16:34

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def rotate(start_row, start_col, cnt):
    temp_grid = [row[:] for row in grid]
    move_data = [row[start_col:start_col+3] for row in grid[start_row:start_row+3]]
    if cnt == 1:
        move_data = [row[::-1] for row in zip(*move_data)]
    if cnt == 2:
        move_data = [row[::-1] for row in move_data[::-1]]
    if cnt == 3:
        move_data = [row for row in zip(*move_data)][::-1]

    for delta_row in range(3):
        for delta_col in range(3):
            temp_grid[start_row+delta_row][start_col+delta_col] = move_data[delta_row][delta_col]
    return temp_grid


def check(grid):
    return_lst = []
    visited = [[False] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if visited[row][col]:
                continue
            visited[row][col] = True

            lst = [(row, col)]
            pointer, cnt = 0, 1
            while pointer < cnt:
                curr_row, curr_col = lst[pointer]
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if grid[curr_row][curr_col] != grid[next_row][next_col]:
                        continue
                    visited[next_row][next_col] = True
                    lst.append((next_row, next_col))
                    cnt += 1
                pointer += 1

            if cnt < 3:
                continue
            return_lst += lst
    return return_lst


def find():
    standard = (0, 0, 0, 0)
    for row in range(3):
        for col in range(3):
            for cnt in range(1, 4):
                temp_grid = rotate(row, col, cnt)
                pos = check(temp_grid)
                standard = max(standard, (len(pos), -cnt, -col, -row))
    return -standard[3], -standard[2], -standard[1], standard[0]


def print_grid():
    for row in grid:
        print(*row)


# =================================================================
# 세팅

K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
fill_lst = list(map(int, input().split()))
pointer = 0
answer = []

# ==================================================================
# 실행부

for _ in range(K):
    # 0. 돈 초기화.
    temp = 0
    
    # 1. 회전부 찾기.
    start_row, start_col, cnt, keep = find()
    if not keep:
        break

    # 2. 실제 회전시키기.
    grid = rotate(start_row, start_col, cnt)

    # 3. 계속 얻기
    while True:
        pos = check(grid)
        if pos:
            pos.sort(key=lambda x: (x[1], -x[0]))
            for row, col in pos:
                grid[row][col] = fill_lst[pointer]
                temp += 1
                pointer += 1
        else:
            break
    answer.append(temp)

# 정답 출력
print(*answer)