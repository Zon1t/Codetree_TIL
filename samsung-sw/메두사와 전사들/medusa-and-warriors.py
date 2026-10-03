# [] /
# 시작 09:33
# 1. 메두사의 이동. dist_grid 만들어서 재탕하면 될 듯
#       - 상 하 좌 우 우선순위 잘 따르기.
#       - 전사가 있으면 사라짐 처리.

# 2. 메두사의 시선. 시선 grid를 받아와야 한다. 전사 이동에 쓰임
#       - 가려지는 애들은 appendleft 활용해서 bfs 하면 될 것 같다.
#       - 퍼뜨리면서 석화된 전사의 수 역시 구해야 한다.
#       - 역시 상 하 좌 우의 우선순위에 의거해서 바라보는 방향을 결정한다.

# 3. 전사들의 이동 & 공격. 공격한 전사의 수, 전사들의 이동 거리를 반환해야 한다.
#       - 두 칸 이동할 수 있고, 경우에 따라선 이동 불가능한 경우 역시 존재한다.
#       - 상 하 좌 우 -> 좌 우 상 하 우선순위 잘 따르기.
#       - 시야각 체크 잘하기.

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
delta_lst = [[(-1, -1), (-1, 0), (-1, 1)],
             [(1, -1),   (1, 0),  (1, 1)],
             [(-1, -1), (0, -1), (1, -1)],
             [(-1, 1),   (0, 1),  (1, 1)]]
select_lst = [(0, 1, 2), (0, 1), (1,), (1, 2)]


def get_dist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist_grid():
    visit_grid = [[-1] * N for _ in range(N)]
    visit_grid[end_row][end_col] = 0

    Q = deque([(end_row, end_col)])
    while Q:
        curr_row, curr_col = Q.popleft()
        if curr_row == m_row and curr_col == m_col:
            break
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col]:
                continue
            if visit_grid[next_row][next_col] != -1:
                continue
            visit_grid[next_row][next_col] = visit_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return visit_grid


def m_move():
    for d in range(4):
        next_row, next_col = m_row + dr[d], m_col + dc[d]
        if not in_range(next_row, next_col):
            continue
        if dist_grid[next_row][next_col] == dist_grid[m_row][m_col]-1:
            return next_row, next_col


def watch():
    watch_grid = [[[False] * N for _ in range(N)] for _ in range(4)]
    max_stone, max_dir = 0, 0

    for d in range(4):
        visited = [[False] * N for _ in range(N)]
        visited[m_row][m_col] = True
        curr_stone = 0

        Q = deque([(m_row, m_col, 0)])
        while Q:
            curr_row, curr_col, curr_state = Q.popleft()

            for order in select_lst[curr_state]:
                delta_row, delta_col = delta_lst[d][order]
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if not in_range(next_row, next_col) or visited[next_row][next_col]:
                    continue

                visited[next_row][next_col] = True
                if curr_state:
                    Q.appendleft((next_row, next_col, curr_state))
                else:
                    watch_grid[d][next_row][next_col] = True
                    if (next_row, next_col) in w_dict:
                        curr_stone += w_dict[(next_row, next_col)]
                        if dr[d]:
                            next_state = 1 if next_col < m_col else 2 if next_col == m_col else 3
                        else:
                            next_state = 1 if next_row < m_row else 2 if next_row == m_row else 3
                        Q.appendleft((next_row, next_col, next_state))
                    else:
                        Q.append((next_row, next_col, curr_state))

        if max_stone < curr_stone:
            max_stone = curr_stone
            max_dir = d

    return watch_grid[max_dir], max_stone


def w_move():
    new_dict = dict()
    total_move, total_attack = 0, 0
    for (row, col), num in w_dict.items():
        if watch_grid[row][col]:
            new_dict[(row, col)] = new_dict.get((row, col), 0) + num
            continue

        curr_row, curr_col = row, col
        curr_dist = get_dist((curr_row , curr_col), (m_row, m_col))

        # 1차 이동 시도.
        keep_going = False
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or watch_grid[next_row][next_col]:
                continue

            next_dist = get_dist((next_row, next_col), (m_row, m_col))
            if curr_dist <= next_dist:
                continue

            total_move += num
            if next_row == m_row and next_col == m_col:
                total_attack += num
            else:
                keep_going = True
                curr_row, curr_col = next_row, next_col
            break
        else:
            new_dict[(curr_row, curr_col)] = new_dict.get((curr_row, curr_col), 0) + num

        if not keep_going:
            continue

        curr_dist = get_dist((curr_row, curr_col), (m_row, m_col))
        for d in range(-2, 2):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or watch_grid[next_row][next_col]:
                continue

            next_dist = get_dist((next_row, next_col), (m_row, m_col))
            if curr_dist <= next_dist:
                continue

            total_move += num
            if next_row == m_row and next_col == m_col:
                total_attack += num
            else:
                curr_row, curr_col = next_row, next_col
                new_dict[(curr_row, curr_col)] = new_dict.get((curr_row, curr_col), 0) + num
            break
        else:
            new_dict[(curr_row, curr_col)] = new_dict.get((curr_row, curr_col), 0) + num

    return new_dict, total_move, total_attack


def get_state():
    temp = [[0] * N for _ in range(N)]
    for (row, col), num in w_dict.items():
        temp[row][col] = num

    print(f'----w_grid----')
    for row in temp:
        print(*row)
    print()
    print(f'm_pos:', m_row, m_col)
    print(f'----watch_grid----')
    for row in watch_grid:
        print(*row)


# ======================================================================
# 세팅

N, M = map(int, input().split())
m_row, m_col, end_row, end_col = map(int, input().split())
w_pos = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
dist_grid = get_dist_grid()

w_dict = dict()
for i in range(M):
    w_row, w_col = w_pos[i<<1], w_pos[i<<1|1]
    w_dict[(w_row, w_col)] = w_dict.get((w_row, w_col), 0) + 1

# =======================================================================
# 실행부

if dist_grid[m_row][m_col] == -1:
    print(-1)
else:
    while True:
        # 1. 메두사 이동
        m_row, m_col = m_move()

        # 1-1. 도착 확인
        if m_row == end_row and m_col == end_col:
            print(0)
            break

        # 1-2. 전사 공격
        if (m_row, m_col) in w_dict:
            w_dict.pop((m_row, m_col))

        # 2. 시선 처리
        watch_grid, stone = watch()

        # 3. 전사 이동
        w_dict, dist, attack = w_move()

        # 4. 정답 출력
        print(dist, stone, attack)