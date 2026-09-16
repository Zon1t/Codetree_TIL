# 시간 11:05
# (r, c)에 있는 값이 k가 되면 종료. 초기에 만족할 수도 있음에 유의하자.
# 정렬하면서 개수 세기. -> lst에 담아두면서 하면 될듯? 첨엔 dict?
# 분기문 적절하게 사용하면 될듯


def simulate():
    global curr_row, curr_col, grid
    trans = False
    if curr_col > curr_row:
        grid = [row[:] for row in zip(*grid)]
        curr_row, curr_col = curr_col, curr_row
        trans = True

    new_grid = []
    max_row = 0
    for row in range(curr_row):
        temp = dict()
        for col in range(curr_col):
            if not grid[row][col]:
                continue
            curr_num = grid[row][col]
            temp[curr_num] = temp.get(curr_num, 0) + 1
        lst = [(v, k) for k, v in temp.items()]
        lst.sort()

        new_row = []
        for a, b in lst:
            new_row.append(b)
            new_row.append(a)
        max_row = max(max_row, len(new_row))
        new_grid.append(new_row)

    for idx in range(curr_row):
        diff = max_row - len(new_grid[idx])
        if diff:
            new_grid[idx] += [0]*diff

    curr_col = max_row
    if trans:
        grid = [row[:] for row in zip(*new_grid)]
        curr_row, curr_col = curr_col, curr_row
    else:
        grid = new_grid


def check():
    return R < curr_row and C < curr_col and grid[R][C]==K


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


R, C, K = map(int, input().split())
R -= 1
C -= 1

grid = [list(map(int, input().split())) for _ in range(3)]
curr_row, curr_col = 3, 3

# 실행부
if check():
    print(0)
else:
    for time in range(1, 101):
        # 1. 해당 과정 수행.
        simulate()

        # 2. 종료 체크
        if check():
            print(time)
            break
    else:
        print(-1)