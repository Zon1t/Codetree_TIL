dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
direction_dict = {'U': 3, 'D': 1, 'R': 0, 'L': 2}


def formatting(data):
    row, col, direction, weight = data.split()
    return int(row)-1, int(col)-1, direction_dict[direction], int(weight)


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move():
    new_grid = [[0] * N for _ in range(N)]
    for idx in range(1, M+1):
        if pos[idx] is None:
            continue

        curr_row, curr_col, curr_dir, _ = pos[idx]
        next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
        if not in_range(next_row, next_col):
            next_row, next_col = curr_row, curr_col
            pos[idx][2] = (curr_dir + 2) % 4
        else:
            pos[idx][0], pos[idx][1] = next_row, next_col

        if new_grid[next_row][next_col]:
            that_idx = new_grid[next_row][next_col]
            pos[idx][3] += pos[that_idx][3]
            pos[that_idx] = None

        new_grid[next_row][next_col] = idx
    return new_grid


def print_grid():
    for row in grid:
        print(*row)


# ===========================================================================
# 세팅

N, M, T = map(int, input().split())

grid = [[0] * N for _ in range(N)]
pos = [None]
for idx in range(1, M+1):
    row, col, direction, weight = formatting(input())
    grid[row][col] = idx
    pos.append([row, col, direction, weight])

# ===========================================================================
# 실행부

for _ in range(T):
    grid = move()

print(len([1 for p in pos if p is not None]), max([data[3] for data in pos if data is not None]))