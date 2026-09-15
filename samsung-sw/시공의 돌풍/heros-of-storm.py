# 시작 5:12
# 확산 -> 청소 두 개의 함수로 구분하여 만들면 되겠다.
# 범위 벗어남 or 돌풍 있음 -> 확산 일어나지 않음. 새로운 격자 만들어서 업뎃 ㄱㄱ
# 청소.. 노가다해서 땡기는 로직 만들자.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


def get_dolpung():
    for row in range(N):
        for col in range(M):
            if grid[row][col] == -1:
                return row


def spread():
    update_grid = [[0] * M for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if grid[row][col] <= 0:
                continue

            curr_munji = grid[row][col]
            give_munji = curr_munji // 5

            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                    continue
                update_grid[next_row][next_col] += give_munji
                grid[row][col] -= give_munji

    for row in range(N):
        for col in range(M):
            grid[row][col] += update_grid[row][col]


def clean():
    # 윗 돌풍 청소 진행
    for row in range(upper-1, 0, -1):
        grid[row][0] = grid[row-1][0]
    for col in range(M-1):
        grid[0][col] = grid[0][col+1]
    for row in range(upper):
        grid[row][-1] = grid[row+1][-1]
    for col in range(M-1, 1, -1):
        grid[upper][col] = grid[upper][col-1]
    grid[upper][1] = 0

    # 아랫 돌풍 청소 진행
    for row in range(lower+1, N-1):
        grid[row][0] = grid[row+1][0]
    for col in range(M-1):
        grid[-1][col] = grid[-1][col+1]
    for row in range(N-1, lower, -1):
        grid[row][-1] = grid[row-1][-1]
    for col in range(M-1, 1, -1):
        grid[lower][col] = grid[lower][col-1]
    grid[lower][1] = 0


def print_grid():
    print(f'----munji_grid----')
    for row in grid:
        print(*row)


N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

upper = get_dolpung()
lower = upper + 1

for _ in range(T):
    # 1. 확산하기.
    spread()

    # 2. 청소하기.
    clean()

# 정답 출력
print(sum([sum(row) for row in grid]) + 2)

