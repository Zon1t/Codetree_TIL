def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def apply_gravity(grid):
    for col in range(N):
        pointer = N-1
        for row in range(N-1, -1, -1):
            if grid[row][col]:
                if pointer != row:
                    grid[row][col], grid[pointer][col] = grid[pointer][col], grid[row][col]
                pointer -= 1


def check(grid):
    score = 0
    for row in range(N):
        for col in range(N):
            if not grid[row][col]:
                continue
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue
                if grid[row][col] == grid[next_row][next_col]:
                    score += 1
    return score


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for row in range(N):
    for col in range(N):
        temp_grid = [row[:] for row in grid]
        K = grid[row][col]
        temp_grid[row][col] = 0
        for d in range(4):
            for k in range(1, K):
                next_row, next_col = row + dr[d] * k, col + dc[d] * k
                if not in_range(next_row, next_col):
                    break
                temp_grid[next_row][next_col] = 0

        apply_gravity(temp_grid)
        answer = max(answer, check(temp_grid))

print(answer)