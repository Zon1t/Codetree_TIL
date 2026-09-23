# 16:03 시작
# 문제 풀이 방식을 조금 바꿀 필요가 있어 보인다. 미리 사람들 출발지에서 도착지 거리 다 체크해놓고
# 진행해보면 어떨까? 일종의 조기종료 조건이 될 수도 있겠다.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def calc_dist(idx):
    start_row, start_col, end_row, end_col = pas_info[idx]
    dist_grid = [[-1] * N for _ in range(N)]
    dist_grid[start_row][start_col] = 0

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_row == end_row and curr_col == end_col:
            break

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col]:
                continue
            if dist_grid[next_row][next_col] != -1:
                continue
            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return dist_grid[end_row][end_col]


def find_closest():
    if pas_grid[car_row][car_col] != -1 and not arrive[pas_grid[car_row][car_col]]:
        return car_row, car_col, pas_grid[car_row][car_col], 0

    dist_grid = [[-1] * N for _ in range(N)]
    dist_grid[car_row][car_col] = 0
    curr_dist = 0

    lst = []
    Q = deque([(car_row, car_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_dist != dist_grid[curr_row][curr_col]:
            if lst:
                lst.sort()
                return_row, return_col = lst[0]
                return return_row, return_col, pas_grid[return_row][return_col], dist_grid[return_row][return_col]
            else:
                curr_dist += 1

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col]:
                continue
            if dist_grid[next_row][next_col] != -1:
                continue

            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

            if pas_grid[next_row][next_col] != -1 and not arrive[pas_grid[next_row][next_col]]:
                lst.append((next_row, next_col))

    return -1, -1, -1, -1


# ==========================================================
# 세팅

scaling = lambda x: int(x)-1

N, M, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
car_row, car_col = map(scaling, input().split())

pas_info = [tuple(map(scaling, input().split())) for _ in range(M)]
pas_grid = [[-1] * N for _ in range(N)]
for idx, (row, col, *_) in enumerate(pas_info):
    pas_grid[row][col] = idx

dist_info = [calc_dist(idx) for idx in range(M)]
arrive = [False] * M
answer = -1

# ===========================================================
# 실행부

if -1 not in dist_info:
    for _ in range(M):
        # 1. 가까운 고객 찾기.
        car_row, car_col, idx, cost = find_closest()
        C -= cost
        if C < 1 or car_row == -1:
            break

        arrive[idx] = True

        # 2. 고객 이동시키기.
        car_row, car_col = pas_info[idx][2:]
        if C >= dist_info[idx]:
            C += dist_info[idx]
        else:
            break
    else:
        answer = C

# 정답 출력
print(answer)

