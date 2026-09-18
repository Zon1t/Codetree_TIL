# 내 머리가 이상한건지 오른쪽 회전 예제를 들 때, 왜 왼쪽으로 못가는지 이해가 안됨.
# 이해한 바에 의하면 회전한 이후 어쨋든 내려가긴 해야 하는 것 같다. 근데 그게 안되면 다음 우선순위..
# 이동 로직 자체가 최대한 남쪽으로 내려가는 의도라고 생각하자. 내가 봤을 땐 가운데를 기준으로 떨구기?
# 보다는 아래칸 기준으로 인접한 3방향을 확인하는 게 더 편할 것 같긴 하다? 진행해보자.
# 오늘 속이 너무 안좋다. 점수 연산할 때 2 빼주는 것 잊지 말기.
# 아다리가 너무 잘맞아서 정령들이 계속 탈출 가능한 경우가 있을까? 정령 != 골렘 << 헷갈리지 말자.
# 바보다. 그룹 구분도 안하고 있었다.


from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

bottom_check_lst = [(0, -1), (0, 1), (1, 0)]
left_check_lst = [(-2, -1), (-1, -2), (0, -2), (0, -1), (1, -1)]
right_check_lst = [(-2, 1), (-1, 2), (0, 2), (0, 1), (1, 1)]


def in_range(row, col):
    return 0 <= row < N+3 and 0 <= col < M


def drop(col, direction):
    curr_row, curr_col, curr_direction = 2, col, direction
    while True:
        if check_bottom(curr_row, curr_col):
            curr_row += 1
        elif check_left(curr_row, curr_col):
            curr_row, curr_col, curr_direction = curr_row+1, curr_col-1, (curr_direction-1)%4
        elif check_right(curr_row, curr_col):
            curr_row, curr_col, curr_direction = curr_row+1, curr_col+1, (curr_direction+1)%4
        else:
            break

    # 격자 밖을 벗어나는 경우
    if curr_row <= 4:
        clear()
        return 0

    # 정령 중심지로 이동
    curr_row -= 1
    grid[curr_row][curr_col] = 1
    group_grid[curr_row][curr_col] = turn
    for d in range(4):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if d == curr_direction:
            grid[next_row][next_col] = 2
        else:
            grid[next_row][next_col] = 1
        group_grid[next_row][next_col] = turn

    max_row = move(curr_row, curr_col)
    return max_row-2


def check_bottom(curr_row, curr_col):
    for delta_row, delta_col in bottom_check_lst:
        next_row, next_col = curr_row + delta_row, curr_col + delta_col
        if not in_range(next_row, next_col) or grid[next_row][next_col]:
            return False
    return True


def check_left(curr_row, curr_col):
    for delta_row, delta_col in left_check_lst:
        next_row, next_col = curr_row + delta_row, curr_col + delta_col
        if not in_range(next_row, next_col) or grid[next_row][next_col]:
            return False
    return True


def check_right(curr_row, curr_col):
    for delta_row, delta_col in right_check_lst:
        next_row, next_col = curr_row + delta_row, curr_col + delta_col
        if not in_range(next_row, next_col) or grid[next_row][next_col]:
            return False
    return True


def move(start_row, start_col):
    visited = [[0] * M for _ in range(N+3)]
    visited[start_row][start_col] = 1

    curr_max = start_row
    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col] == 0:
                continue
            if visited[next_row][next_col] or (grid[curr_row][curr_col] == 1 and \
                    group_grid[curr_row][curr_col] != group_grid[next_row][next_col]):
                continue

            curr_max = max(curr_max, next_row)
            visited[next_row][next_col] = True
            Q.append((next_row, next_col))

    return curr_max


def clear():
    global grid, group_grid
    grid = [[0] * M for _ in range(N+3)]
    group_grid = [[0] * M for _ in range(N+3)]


def print_grid():
    print(f'----curr_grid----')
    for row in grid:
        print(*row)

# ==================================================
# 입력

N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N+3)]
group_grid = [[0] * M for _ in range(N+3)]

# ==================================================
# 실행부

answer = 0
for turn in range(1, K+1):
    c, d = map(int, input().split())
    answer += drop(c-1, d)

print(answer)