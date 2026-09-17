# 7:48 시작
# 델타?로 저번에 풀어본 것 같으니 다른 방식으로 접근해보자.. list에 넣고 역방향 탐색? dp? 그거 해보자
# 세팅만 잘하면 큰 문제 없이 해결 가능 할 듯하다.


def in_range(row, col):
    return 0 <= row < 101 and 0 <= col < 101


def make_curve(g):
    if memo[g]:
        return memo[g]
    delta_lst = make_curve(g-1)
    new_lst = []
    std_row, std_col = delta_lst[-1]
    for row, col in delta_lst[len(delta_lst)-2::-1]:
        row_diff, col_diff = std_row-row, std_col-col
        new_lst.append((std_row-col_diff, std_col+row_diff))

    memo[g] = delta_lst+new_lst
    return memo[g]


N = int(input())
grid = [[0] * 101 for _ in range(101)]
memo = [[(0, 0), (0, 1)]] + [[] for _ in range(10)]

curves = [tuple(map(int, input().split())) for _ in range(N)]
for row, col, d, g in curves:
    deltas = make_curve(g)
    if d == 0:
        for delta_row, delta_col in deltas:
            next_row, next_col = row+delta_row, col+delta_col
            if in_range(next_row, next_col):
                grid[next_row][next_col] = 1
    elif d == 1:
        for delta_row, delta_col in deltas:
            next_row, next_col = row-delta_col, col+delta_row
            if in_range(next_row, next_col):
                grid[next_row][next_col] = 1
    elif d == 2:
        for delta_row, delta_col in deltas:
            next_row, next_col = row-delta_row, col-delta_col
            if in_range(next_row, next_col):
                grid[next_row][next_col] = 1
    else:
        for delta_row, delta_col in deltas:
            next_row, next_col = row+delta_col, col-delta_row
            if in_range(next_row, next_col):
                grid[next_row][next_col] = 1

answer = 0
for row in range(100):
    for col in range(100):
        if grid[row][col] and grid[row+1][col] and grid[row][col+1] and grid[row+1][col+1]:
            answer += 1

print(answer)