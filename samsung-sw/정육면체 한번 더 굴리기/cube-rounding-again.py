# 주사위 보이는대로 위, 앞, 왼, 뒤, 오, 아래 순서 idx fix하기.
# -1 idx에 있는 숫자를 기준으로 위치를 이동시켜가며 점수 연산.
# 점수를 연산하는 것에 있어, 중복 연산이 많아질 수 있을 것. 미리 연산 후 grid를 업데이트하자.
# *격자 튕기는 로직 잘 구현하기

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def bfs(sr, sc):

    Q.append((sr, sc))
    update_set.clear()

    cnt = 0
    while Q:
        cr, cc = Q.popleft()

        update_set.add((cr, cc))
        cnt += 1

        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if not in_range(nr, nc) or score_grid[nr][nc] or grid[nr][nc] != grid[cr][cc]:
                continue
            score_grid[nr][nc] = 1
            Q.append((nr, nc))

    update_value = grid[sr][sc] * cnt
    for row, col in update_set:
        score_grid[row][col] = update_value

def chage():
    if curr_dir == 0:
        curr_status[0], curr_status[2], curr_status[4], curr_status[5] = \
            curr_status[2], curr_status[5], curr_status[0], curr_status[4]
    elif curr_dir == 1:
        curr_status[0], curr_status[1], curr_status[3], curr_status[5] = \
            curr_status[3], curr_status[0], curr_status[5], curr_status[1]
    elif curr_dir == 2:
        curr_status[0], curr_status[2], curr_status[4], curr_status[5] = \
            curr_status[4], curr_status[0], curr_status[5], curr_status[2]
    else:
        curr_status[0], curr_status[1], curr_status[3], curr_status[5] = \
            curr_status[1], curr_status[5], curr_status[0], curr_status[3]

def find_dir():
    global curr_dir

    if curr_status[-1] > grid[curr_row][curr_col]:
        curr_dir = (curr_dir + 1) % 4
    elif curr_status[-1] < grid[curr_row][curr_col]:
        curr_dir = (curr_dir - 1) % 4

    next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    if not in_range(next_row, next_col):
        curr_dir = (curr_dir + 2) % 4


N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 전역변수 선언
curr_status = [1, 2, 4, 5, 3, 6]    # 다 맞게 했는데 얘를 잘못 적냐
curr_row, curr_col = 0, 0
curr_dir = 0

# grid 업데이트
Q = deque()
update_set = set()
score_grid = [[0] * N for _ in range(N)]
for row in range(N):
    for col in range(N):

        if score_grid[row][col]:
            continue

        score_grid[row][col] = 1
        bfs(row, col)

answer = 0
for _ in range(K):
    # 1. 좌표 업데이트 + 점수 반영
    curr_row, curr_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    answer += score_grid[curr_row][curr_col]

    # 2. 주사위 상태 변화시켜 주기
    chage()

    # 3. 다음 방향 모색
    find_dir()

print(answer)