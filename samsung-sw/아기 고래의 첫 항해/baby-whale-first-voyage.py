# 아기 고래가 갈 수 있는 모든 바다를 방문하는 것이 목적.

# 1. 인접 탐험. 인접한 칸에 대해서 방문하지 않은 바다가 있는 경우 해당 바다 탐색.
#       - 우선 순위. 직진 - 좌회전 - 우회전 - 180도
#       - 이동한 방향으로 바라보는 방향이 갱신됨에 유의하자!
#       - 해당 과정을 인접한 칸에 방문 가능한 바다가 없을 때까지 반복

# 2. 가장 가까운 바다로 이동. 인접 탐험이 불가한 경우 진행한다.
#       - 최소 이동 횟수를 기준으로 삼는다.
#       - 가장 가까운 칸이 여러개면 행작 - 열작 우선순위
#       - 이 때에도 좌 하 우 상 우선순위에 의거하여 이동. 마지막 바라보는 방향이 중요하다.
#       - 이거 마지막 칸만 확인하면 되는 것 같은.. 그런 묘수 있을 것 같긴 한데 그냥 가자.

# 1단계부터 다시 반복. 시키는대로 잘해보자.


from collections import deque

#    좌  하  우  상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
dir_dict = {1: 3, 2: 1, 3: 0, 4: 2}
for_debug = ['←', '↓', '→', '↑']

# 직진, 좌회전, 우회전, 180도
delta_lst = [0, 1, -1, 2]


def adj_move():
    global whale_row, whale_col, curr_dir
    for delta_dir in delta_lst:
        next_dir = (curr_dir + delta_dir) % 4
        next_row, next_col = whale_row + dr[next_dir], whale_col + dc[next_dir]

        if grid[next_row][next_col] or visited[next_row][next_col]:
            continue

        whale_row, whale_col, curr_dir = next_row, next_col, next_dir
        visited[whale_row][whale_col] = True
        answer.append((whale_row, whale_col))
        return True

    return False


def find_next():
    dist_grid = [[-1] * (N+2) for _ in range(N+2)]
    dist_grid[whale_row][whale_col] = 0

    find = (N+2, N+2)
    Q = deque([(whale_row, whale_col)])
    while Q:
        for _ in range(len(Q)):
            curr_row, curr_col = Q.popleft()

            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]

                if grid[next_row][next_col] or dist_grid[next_row][next_col] != -1:
                    continue

                dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
                Q.append((next_row, next_col))

                if not visited[next_row][next_col]:
                    find = min(find, (next_row, next_col))

        if find[0] != N+2:
            return find

    return None, None


def close_move():
    global whale_row, whale_col, curr_dir

    # 목표 지점 찾기.
    end_row, end_col = find_next()
    if end_row is None:
        return False

    # 찾았으면 역방향 걸기.
    dist_grid = [[-1] * (N+2) for _ in range(N+2)]
    dist_grid[end_row][end_col] = 0

    Q = deque([(end_row, end_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if (curr_row, curr_col) == (whale_row, whale_col):
            break

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if grid[next_row][next_col] or dist_grid[next_row][next_col] != -1:
                continue
            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    # 목적지로 이동하기.
    while True:
        if (whale_row, whale_col) == (end_row, end_col):
            break

        for d in range(4):
            next_row, next_col = whale_row + dr[d], whale_col + dc[d]
            if grid[next_row][next_col]:
                continue
            if dist_grid[next_row][next_col] != dist_grid[whale_row][whale_col]-1:
                continue

            whale_row, whale_col, curr_dir = next_row, next_col, d
            break

    # 정보 업데이트.
    visited[whale_row][whale_col] = True
    answer.append((whale_row, whale_col))
    return True


def print_grid():
    print(f'----grid----')
    temp_grid = [row[:] for row in grid]
    temp_grid[whale_row][whale_col] = for_debug[curr_dir]
    for row in temp_grid:
        print(*row)
    print()


# ==============================================================
# 세팅

N, whale_row, whale_col, curr_dir = map(int, input().split())
curr_dir = dir_dict[curr_dir]

# 좌표 기록의 편의를 위함.
grid = [[1] * (N+2)] + \
       [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + \
       [[1] * (N+2)]

visited = [[False] * (N+2) for _ in range(N+2)]
visited[whale_row][whale_col] = True

answer = [(whale_row, whale_col)]

# ===============================================================
# 실행부

while True:
    # 1. 인접 탐험.
    while adj_move():
        continue

    # 2. 가장 가까운 바다 이동.
    if not close_move():
        break

# 정답 출력
print('\n'.join([' '.join(map(str, pos)) for pos in answer]))