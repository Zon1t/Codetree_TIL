''' 마법의 숲 탐색 / 20260918 / 체감 난이도 : 골드 3
소요 시간 : 62분 / 시도 : 1회 / 실행 시간 : 341ms / 메모리 : 24MB

타임 라인 : 구상(26분) - 화캉스(12분) - 구현(18분) - 검증(6분)


[구상]
    - 회전 로직을 온전히 이해하는 것에 시간을 거의 다 쓴 것 같다. 내가 한국말을 못하는건가 생각하다.
    오늘 속도 안좋고 해서 글도 잘 안 읽히고 주석이나 초기 틀을 잡는데 오타가 너무 많았다.
    - 초록색 칸이라고 명시해준 것을 나중에 알아차렸다.. 다행히 이해한 바와 동일해서 수정은 안했지만
    문제 똑바로 잘 읽어야 겠다고 생각했다.
    - 틀 다 만들어 놓고 속이 너무 안 좋아서 잠시 나갔다가 왔다.

[구현]
    - 체크리스트 등 다 세팅해두었고, 구상을 오래 가져갔어서 머리에 정리가 잘 되어있다고 생각했다. 겹
    치는 부분도 많아서, 근래 푼 문제 중에선 구현량이 가장 적었던 문제같다.
    - 출구 개념을 온전히 이해하고 bfs를 구현한 줄 알았는데, 알고보니 group도 만들어 주어야 골렘 사
    이의 이동 로직 구현에 수월함을 알아차렸다. 이런건 미리 알 만도 한데.. 테케 디버깅에서 이걸 알게
    된 게 아쉬운 부분같다.

[검증]
    - 문제, 코드를 정독하며 비교해보고 곧바로 제출했다.


* 다행히 쉬운 문제에서 아팠던게 다행인 것 같다. 컨디션 관리 잘해서 연습할 때에도 지장 없게 해야겠다.
'''

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

# 그냥 중심 좌표로 해도 됐을듯?
bottom_check_lst = [(0, -1), (0, 1), (1, 0)]
left_check_lst = [(-2, -1), (-1, -2), (0, -2), (0, -1), (1, -1)]
right_check_lst = [(-2, 1), (-1, 2), (0, 2), (0, 1), (1, 1)]


def in_range(row, col):
    return 0 <= row < N+3 and 0 <= col < M


def drop(col, direction):
    curr_row, curr_col, curr_direction = 2, col, direction
    while True:
        if check(curr_row, curr_col, bottom_check_lst):
            curr_row += 1
        elif check(curr_row, curr_col, left_check_lst):
            curr_row, curr_col, curr_direction = curr_row+1, curr_col-1, (curr_direction-1)%4
        elif check(curr_row, curr_col, right_check_lst):
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
    return max_row-2    # 결과 보정


def check(curr_row, curr_col, check_lst):
    for delta_row, delta_col in check_lst:
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
    for row in range(N+3):
        for col in range(M):
            grid[row][col] = group_grid[row][col] = 0


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