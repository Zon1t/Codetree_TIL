# 시작 : 4:32
# 회전 레벨이 L일 때 2<<L 격자 select, 2<<(L-1) 애들 회전.
# 얼음 녹는건 동시에 진행.
# 정답은 빙하의 총 양과 가장 큰 얼음 군집의 크기.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def rotate(start_row, start_col):
    for delta_row in range(chunk):
        for delta_col in range(chunk):
            first_row, first_col = start_row + delta_row, start_col + delta_col
            second_row, second_col = first_row + chunk, first_col + chunk
            temp = grid[first_row][first_col]
            grid[first_row][first_col] = grid[second_row][first_col]
            grid[second_row][first_col] = grid[second_row][second_col]
            grid[second_row][second_col] = grid[first_row][second_col]
            grid[first_row][second_col] = temp


def melt():
    update_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                continue
            cnt = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if in_range(next_row, next_col) and grid[next_row][next_col]:
                    cnt += 1
            if cnt < 3:
                update_grid[row][col] -= 1

    for row in range(N):
        for col in range(N):
            grid[row][col] += update_grid[row][col]


def get_answer():
    answer1 = sum([sum(row) for row in grid])
    answer2 = 0

    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] or not grid[row][col]:
                continue

            visited[row][col] = True
            cnt = 0
            Q = deque([(row, col)])
            while Q:
                curr_row, curr_col = Q.popleft()
                cnt += 1
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or not grid[next_row][next_col]:
                        continue
                    if visited[next_row][next_col]:
                        continue
                    visited[next_row][next_col] = True
                    Q.append((next_row, next_col))

            if answer2 < cnt:
                answer2 = cnt

    return answer1, answer2


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


n, Q = map(int, input().split())
N = 1 << n

grid = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

for rotate_level in commands:
    # 1. 회전시키기.
    if rotate_level:
        size = 1 << rotate_level
        chunk = size >> 1
        for sr in range(0, N, size):
            for sc in range(0, N, size):
                rotate(sr, sc)

    # 2. 녹이기.
    melt()

# 정답 연산 후 출력
answer1, answer2 = get_answer()
print(answer1)
print(answer2)