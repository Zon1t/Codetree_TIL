# 굉장히 귀찮은 문제이지만, 그냥 시키는대로 천천히 하면 된다. 어려운 로직은 없어 보인다.
# m_move() -> see() -> w_move() -> attack() 이런 느낌으로..
# 최단 거리는 맨해튼 거리로 연산하면 된다. << 이거 쉽지않네
# 유의할 점? 시야각을 잘 처리해야 할 것 같은데.. bfs까진 맞고. 용사 만나는 위치 기준으로 덧씌우기?
# 단순히 생각하면 안 될 것 같다. 일단 구현 ㄱㄱ


from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 이거 폐기, 그냥 완탐하면 되는데 무슨 부귀영화를 누리겠다고;
# # 직선 따로 대각 따로? 대각은 이후 직선도 퍼지게끔? 이것도 좋아보인다.
# deltas = [[[(-1, -1), (-1, 0), (None, None)], [(None, None), (-1, 0), (None, None)], [(None, None), (-1, 0), (-1, 1)]],
#           [[(1, -1), (1, 0), (None, None)],   [(None, None), (1, 0), (None, None)],  [(None, None), (1, 0), (1, 1)]],
#           [[(-1, -1), (0, -1), (None, None)], [(None, None), (0, -1), (None, None)], [(None, None), (0, -1), (1, -1)]],
#           [[(-1, 1), (0, 1), (None, None)],   [(None, None), (0, 1), (None, None)],  [(None, None), (0, 1), (1, 1)]]]

init_delta = [[(-1, -1), (-1, 0), (-1, 1)],
              [(1, -1), (1, 0), (1, 1)],
              [(-1, -1), (0, -1), (1, -1)],
              [(-1, 1), (0, 1), (1, 1)]]
deltas = [[[(-1, -1), (-1, 0)], [(-1, 0)], [(-1, 0), (-1, 1)]],
          [[(1, -1), (1, 0)],   [(1, 0)],  [(1, 0), (1, 1)]],
          [[(-1, -1), (0, -1)], [(0, -1)], [(0, -1), (1, -1)]],
          [[(-1, 1), (0, 1)],   [(0, 1)],  [(0, 1), (1, 1)]]]



def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def make_dist_grid():
    start_row, start_col = er, ec
    dist_grid = [[-1] * N for _ in range(N)]
    dist_grid[start_row][start_col] = 0

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_row == mr and curr_col == mc:
            break

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or dist_grid[next_row][next_col] != -1:
                continue
            if grid[next_row][next_col] == 1:
                continue
            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return dist_grid


def m_move():
    for d in range(4):
        next_row, next_col = mr+dr[d], mc+dc[d]
        if not in_range(next_row, next_col):
            continue
        if dist_grid[next_row][next_col] == dist_grid[mr][mc]-1:
            return next_row, next_col


def update_grid(row, col, status, direction, check_grid):
    Q = deque([(row, col)])
    new_grid = [[0] * N for _ in range(N)]
    while Q:
        curr_row, curr_col = Q.popleft()
        for delta_row, delta_col in deltas[direction][status]:
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            if not in_range(next_row, next_col) or new_grid[next_row][next_col]:
                continue
            new_grid[next_row][next_col] = 1
            Q.append((next_row, next_col))

    for row in range(N):
        for col in range(N):
            if new_grid[row][col]:
                check_grid[row][col] = 1


# 돌로 된 전사의 수 반환
def see():
    watch_grid = [[[0] * N for _ in range(N)] for _ in range(4)]
    max_cnt, max_direction = 0, 0
    for d in range(4):
        curr_cnt = 0
        check_grid = [[0] * N for _ in range(N)]

        Q = deque([(mr, mc)])
        while Q:
            curr_row, curr_col = Q.popleft()
            for delta_row, delta_col in init_delta[d]:
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if not in_range(next_row, next_col) or watch_grid[d][next_row][next_col]:
                    continue
                if check_grid[next_row][next_col]:
                    continue

                watch_grid[d][next_row][next_col] = 1
                Q.append((next_row, next_col))

                if w_grid[next_row][next_col]:
                    curr_cnt += w_grid[next_row][next_col]
                    if dr[d]:
                        status = 0 if next_col < mc else 1 if next_col == mc else 2
                    else:
                        status = 0 if next_row < mr else 1 if next_row == mr else 2
                    update_grid(next_row, next_col, status, d, check_grid)

        if curr_cnt > max_cnt:
            max_cnt, max_direction = curr_cnt, d

    return max_cnt, watch_grid[max_direction]


# 이동 거리의 합. + 공격한 전사의 수 반환
def w_move():
    new_w_grid = [[0] * N for _ in range(N)]
    attack_cnt, move_cnt = 0, 0
    for row in range(N):
        for col in range(N):
            if not w_grid[row][col]:
                continue

            if watch_grid[row][col]:
                new_w_grid[row][col] += w_grid[row][col]
                continue

            curr_dist = get_dist((row, col), (mr, mc))
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue

                next_dist = get_dist((next_row, next_col), (mr, mc))
                if watch_grid[next_row][next_col] or next_dist >= curr_dist:
                    continue

                move_cnt += w_grid[row][col]
                if next_dist == 0:
                    attack_cnt += w_grid[row][col]
                else:
                    for d_ in range(2, 6):
                        nnr, nnc = next_row + dr[d_%4], next_col + dc[d_%4]
                        if not in_range(nnr, nnc):
                            continue

                        nnd = get_dist((nnr, nnc), (mr, mc))
                        if watch_grid[nnr][nnc] or nnd >= next_dist:
                            continue

                        move_cnt += w_grid[row][col]
                        if nnd == 0:
                            attack_cnt += w_grid[row][col]
                        else:
                            new_w_grid[nnr][nnc] += w_grid[row][col]

                        break

                    else:
                        new_w_grid[next_row][next_col] += w_grid[row][col]

                break

            else:
                new_w_grid[row][col] += w_grid[row][col]

    return attack_cnt, move_cnt, new_w_grid


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# ==============================================
# 세팅

N, M = map(int, input().split())
mr, mc, er, ec = map(int, input().split())

w_grid = [[0] * N for _ in range(N)]
w_info = list(map(int, input().split()))
for i in range(M):
    ar, ac = w_info[i<<1], w_info[i<<1|1]
    w_grid[ar][ac] += 1

grid = [list(map(int, input().split())) for _ in range(N)]
dist_grid = make_dist_grid()

# ==============================================
# 실행부

if dist_grid[mr][mc] == -1:
    print(-1)
else:
    while mr != er or mc != ec:
        # 1. 메두사 움직이기.
        mr, mc = m_move()
        w_grid[mr][mc] = 0
        if mr == er and mc == ec:
            print(0)
            break

        # 2. 시선처리
        rock_cnt, watch_grid = see()

        # 3. 전사들 움직임.
        attack_cnt, move_cnt, w_grid = w_move()

        # 4. 정답 출력
        print(move_cnt, rock_cnt, attack_cnt)