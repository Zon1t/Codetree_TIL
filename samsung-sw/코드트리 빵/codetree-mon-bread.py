# 생각할 부분이 많은 문제인 듯. 천천히 읽고 들어가자.
# 격자에 있는 사람들이 모두 이동한 뒤에 이동할 수 없어짐 <- 이거 굉장히 중요한 조건이다.
# 매턴 bfs 돌려가면서 위치 찾고 넣어주고 등등.. 수행하는 거 잘하면 생각보다는? 괜찮을 것 같다.
# 움직이는 방법론에 대해서 고민을 좀 해봐야 하는데.. 개인 격자 만들어주기? 이거 생각보다 괜찮겠다.
# 사람은 많아야 30명이니 시간도 괜찮을지도.. 더 고능한 방법 없나? 일단 해보자.
# 배이스캠프 == 편의점 이건 있을 수 있나?


from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def find_basecamp(idx):
    target_row, target_col = conb[idx]
    visited = individual_grid[idx]          # 해당 가변 객체를 수정할 것.
    visited[target_row][target_col] = 0

    find = []
    curr_dist = -1

    Q = deque([(target_row, target_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_dist != visited[curr_row][curr_col]:
            if find:
                find.sort()
                return find[0][0], find[0][1]
            curr_dist = visited[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or lock_grid[next_row][next_col]:
                continue
            if visited[next_row][next_col] != -1:
                continue

            if grid[next_row][next_col]:
                find.append((next_row, next_col))
            visited[next_row][next_col] = visited[curr_row][curr_col] + 1
            Q.append((next_row, next_col))

    # 여기까지 올 일은 없긴 하다.
    return -1, -1


def update_grid():
    for idx in range(1, min(curr_time, M) + 1):
        if arrival[idx]:
            continue

        target_row, target_col = conb[idx]
        visited = individual_grid[idx] = [[-1] * N for _ in range(N)]
        visited[target_row][target_col] = 0

        Q = deque([(target_row, target_col)])
        while Q:
            curr_row, curr_col = Q.popleft()

            if (curr_row, curr_col) == human[idx]:
                break

            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or (lock_grid[next_row][next_col] and (next_row, next_col) != human[idx]):
                    continue
                if visited[next_row][next_col] != -1:
                    continue
                visited[next_row][next_col] = visited[curr_row][curr_col] + 1
                Q.append((next_row, next_col))


# 최단거리란 항상 현재를 기준으로 하는가? 아니면 미래를 예측해서 하는가? 전자겠지?
def move():
    global need_update
    if need_update:
        update_grid()
        need_update = False

    arrival_lst = []
    for idx in range(1, min(curr_time, M)+1):
        # 이미 도착했으면 움직일 필요 없음
        if arrival[idx]:
            continue

        curr_row, curr_col = human[idx]
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col):
                continue

            if individual_grid[idx][next_row][next_col] == individual_grid[idx][curr_row][curr_col] - 1:

                if individual_grid[idx][next_row][next_col] == 0:
                    arrival_lst.append((idx, next_row, next_col))
                human[idx] = (next_row, next_col)
                break

    # 필요 값 반환
    return arrival_lst


def custom_print():
    print(f'----arrival----')
    print(*arrival[1:])
    print(f'----human----')
    print(*human[1:])
    print(f'----indiv_grid----')
    for idx in range(1, M+1):
        print(f'----{idx}----')
        for row in individual_grid[idx]:
            print(*row)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
individual_grid = [[[-1] * N for _ in range(N)] for _ in range(M+1)]
lock_grid = [[0] * N for _ in range(N)]
arrival = [False] * (M+1)

conb = [None] + [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
human = [None]

curr_time, visit_cnt, need_update = 0, 0, False
while True:
    # 0. 이미 다 편의점에 갔으면 종료
    if visit_cnt == M:
        break

    # 1. 격자에 사람들이 있다면 move
    cant_go = move()

    # 2. 못가는 칸들 표시.
    for idx, row, col in cant_go:
        lock_grid[row][col] = 1
        visit_cnt += 1
        need_update = True
        arrival[idx] = True

    # 3. 베이스 캠프 배치가 가능하면 배치
    if curr_time < M:
        base_row, base_col = find_basecamp(curr_time+1)
        lock_grid[base_row][base_col] = 1
        human.append((base_row, base_col))
        need_update = True

    curr_time += 1

# 정답 출력
print(curr_time)