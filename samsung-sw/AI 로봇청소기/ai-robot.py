# []/
# 10:15

# 격자 1-based 기억하기 **

# 1. 청소기의 이동
#       - 순서대로 이동함에 유의
#       - 이동 거리가 가장 가까운 오염된 격자로 이동하기.
#       - 물건이 있거나 청소기가 있는 경우 지나갈 수 없음.
#       - 여러 개일 경우 행작 - 열작

# 2. 청소
#       - 순서대로 청소함에 유의
#       - 'ㅗ' 모양으로 청소 진행.
#       - 바라보는 방향의 경우 가장 청소를 많이 할 수 있는 방향으로
#       - 그러한 방향이 여러 개인 경우 우-하-좌-상 우선순위를 가짐
#       - 한 칸마다 ""최대 20""만큼 청소 가능함에 유의

# 3. 먼지 축적
#       - '먼지가 있는' 칸에 5씩 더해주기

# 4. 먼지 확산
#       - 주변 4방향 격자의 합을 10으로 나눈 값만큼 확산
#       - 확산은 동시에 일어남에 유의

# 5. 각 라운드마다 총 먼지의 합 출력하면 됨.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(cleaner_idx):
    start_row, start_col = cleaner[cleaner_idx]
    if grid[start_row][start_col] > 0:
        return

    visited = [[False] * N for _ in range(N)]
    visited[start_row][start_col] = True

    target = (N, N)

    Q = deque([(start_row, start_col)])
    while Q:
        for _ in range(len(Q)):
            curr_row, curr_col = Q.popleft()
            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                    continue
                if visited[next_row][next_col] or cleaner_grid[next_row][next_col]:
                    continue

                visited[next_row][next_col] = True
                Q.append((next_row, next_col))

                if grid[next_row][next_col]:
                    target = min(target, (next_row, next_col))

        if target[0] != N:
            break

    if target[0] == N:
        return

    cleaner[cleaner_idx] = target
    target_row, target_col = target
    cleaner_grid[start_row][start_col] = 0
    cleaner_grid[target_row][target_col] = cleaner_idx


def clean(cleaner_idx):
    curr_row, curr_col = cleaner[cleaner_idx]
    max_num, max_d = 0, 0
    for d in range(4):
        temp = 0
        for clean_d in range(4):
            if d == (clean_d + 2) % 4:
                continue
            next_row, next_col = curr_row + dr[clean_d], curr_col + dc[clean_d]
            if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                continue
            temp += min(20, grid[next_row][next_col])

        if max_num < temp:
            max_num, max_d = temp, d

    grid[curr_row][curr_col] -= min(20, grid[curr_row][curr_col])
    for d in range(4):
        if d == (max_d + 2) % 4:
            continue
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
            continue
        grid[next_row][next_col] -= min(20, grid[next_row][next_col])


def accumulate():
    for row in range(N):
        for col in range(N):
            if grid[row][col] > 0:
                grid[row][col] += 5


def spread():
    update_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col]:
                continue

            temp = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                    continue
                temp += grid[next_row][next_col]
            update_grid[row][col] += temp // 10

    for row in range(N):
        for col in range(N):
            grid[row][col] += update_grid[row][col]


def get_sum():
    return sum([grid[row][col] for row in range(N) for col in range(N) if grid[row][col] > 0])


# =====================================================================
# 세팅

N, K, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cleaner_grid = [[0] * N for _ in range(N)]
cleaner = [None] * (K+1)
for idx in range(1, K+1):
    ai_row, ai_col = map(lambda x: int(x)-1, input().split())
    cleaner[idx] = (ai_row, ai_col)
    cleaner_grid[ai_row][ai_col] = idx

answer = []

# =====================================================================
# 실행부

for _ in range(T):
    # 1. 청소기 무빙
    for idx in range(1, K+1):
        move(idx)

    # 2. 청소하기
    for idx in range(1, K+1):
        clean(idx)

    # 3. 먼지 축적
    accumulate()

    # 4. 먼지 확산
    spread()

    # 5. 출력
    curr_sum = get_sum()
    answer.append(str(curr_sum))

    # 조기 종료 체크
    if not curr_sum:
        break

print('\n'.join(answer))