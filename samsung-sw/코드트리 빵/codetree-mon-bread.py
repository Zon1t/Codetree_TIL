# 16:57 시작 [] /
# 1. 사람들 우선 순위에 의거하여 움직이기.
# 2. 모두 이동한 이후 blocking
# 3. 현재 시간이 t분일 떄 t<m의 경우 베이스 캠프 배치. + blocking

from collections import deque


dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move():
    new_human = human[:]
    for idx in range(M):
        if human[idx] is None or arrive[idx]:
            continue

        start_row, start_col = human[idx]
        end_row, end_col = target[idx]
        next_dir = -1

        visited = [[False]*N for _ in range(N)]
        visited[start_row][start_col] = True

        Q = deque()
        for d in range(4):
            next_row, next_col = start_row+dr[d], start_col+dc[d]
            if not in_range(next_row, next_col) or block_grid[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            Q.append((next_row, next_col, d))

        while Q:
            curr_row, curr_col, init_dir = Q.popleft()

            if curr_row == end_row and curr_col == end_col:
                next_dir = init_dir
                break

            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or visited[next_row][next_col]:
                    continue
                if block_grid[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                Q.append((next_row, next_col, init_dir))

        next_row, next_col = start_row + dr[next_dir], start_col + dc[next_dir]
        if next_row == end_row and next_col == end_col:
            block_lst.append((end_row, end_col))
            arrive[idx] = True
        new_human[idx] = (next_row, next_col)
    return new_human


def find(idx):
    find = []
    target_row, target_col = target[idx]
    visited = [[False]*N for _ in range(N)]
    visited[target_row][target_col] = True

    Q = deque([(target_row, target_col)])
    while Q:
        if find:
            find.sort()
            return find[0][0], find[0][1]

        for _ in range(len(Q)):
            curr_row, curr_col = Q.popleft()
            for d in range(4):
                next_row, next_col = curr_row+dr[d], curr_col+dc[d]
                if not in_range(next_row, next_col) or visited[next_row][next_col]:
                    continue
                if block_grid[next_row][next_col]:
                    continue

                visited[next_row][next_col] = True
                Q.append((next_row, next_col))

                if grid[next_row][next_col]:
                    find.append((next_row, next_col))

    return -1, -1


def print_status():
    print('----grid----')
    for row in grid:
        print(*row)
    print('----human----')
    print(*human)
    print('----arrive----')
    print(*arrive)


# ============================================================
# 세팅

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
block_grid = [[0]*N for _ in range(N)]

target = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
arrive = [False] * M
human = [None] * M
block_lst = []
turn = 1

# =============================================================
# 실행부

while True:
    # 1. 사람들 움직이기.
    human = move()
    if sum(arrive) == M:
        break
    
    # 3. blocking
    for row, col in block_lst:
        block_grid[row][col] = 1
    block_lst.clear()

    # 2. 배이스 캠프 배치.
    if turn <= M:
        base_row, base_col = find(turn-1)
        human[turn-1] = (base_row, base_col)
        block_lst.append((base_row, base_col))
        grid[base_row][base_col] = 0
    turn += 1

    # 3. blocking
    for row, col in block_lst:
        block_grid[row][col] = 1
    block_lst.clear()

# 정답 출력
print(turn)
