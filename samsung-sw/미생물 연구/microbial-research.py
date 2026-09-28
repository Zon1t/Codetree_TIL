# 좌하단 -> 우상단. 그냥 평소 리스트 쓰던 방식으로 하면 될 것 같다. 격자 90도 돌렸다고 생각?
# 1. 미생물 투입
#    - 업데이트 되는 과정에서 각 좌표에 있는 미생물 집단의 번호, 갯수 확인
#    - 둘 이상으로 나누어짐의 여부는 bfs 연결 요소 확인으로
# 2. 배양 용기 이동
#    - 해당 과정에서 기준 미생물과, 상대 좌표를 써야할 것 같다.
#    - 기준 미생물은 (r작, c작)의 우선 순위를 가짐. 이래야 옮길 때 편할 것으로 추정된다.
#    - 옮길 때 어려운 점은 미생물이 순차적으로 들어올 때 들어갈 수 있는 공간인지 완탐?해야하는거?
# 3. 실험 결과 기록
#    - 전체에 대해서 bfs돌며 확인하기.
#    - 예술성 문제처럼 group 만드는 과정에서 info 따기.


from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def put(start_row, start_col, end_row, end_col, num):
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            grid[row][col] = num


def get_data():
    # 저장 양식 data[idx] = [delta_lst]
    data, remove_set = dict(), set()

    group_grid = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not grid[row][col] or group_grid[row][col]:
                continue

            if grid[row][col] in remove_set:
                continue

            if grid[row][col] in data:
                data.pop(grid[row][col])
                remove_set.add(grid[row][col])
                continue

            curr_group = group_grid[row][col] = grid[row][col]
            data[curr_group] = []

            Q = deque([(row, col)])
            while Q:
                curr_row, curr_col = Q.popleft()
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or group_grid[next_row][next_col]:
                        continue
                    if grid[curr_row][curr_col] != grid[next_row][next_col]:
                        continue
                    group_grid[next_row][next_col] = curr_group
                    Q.append((next_row, next_col))
                    data[curr_group].append((next_row-row, next_col-col))

    return data


def check(start_row, start_col, delta_lst, new_grid):
    for delta_row, delta_col in delta_lst:
        check_row, check_col = start_row + delta_row, start_col + delta_col
        if not in_range(check_row, check_col) or new_grid[check_row][check_col]:
            return False
    return True


def write(start_row, start_col, num, delta_lst, new_grid):
    new_grid[start_row][start_col] = num
    for delta_row, delta_col in delta_lst:
        write_row, write_col = start_row + delta_row, start_col + delta_col
        new_grid[write_row][write_col] = num


def move():
    data = get_data()
    cnt_data = dict()

    order = [(len(value), key) for key, value in data.items()]
    order.sort(key=lambda x: (-x[0], x[1]))

    new_grid = [[0]*N for _ in range(N)]
    for _, num in order:
        flag = False
        for row in range(N):
            for col in range(N):
                if not new_grid[row][col] and check(row, col, data[num], new_grid):
                    write(row, col, num, data[num], new_grid)
                    cnt_data[num] = len(data[num])+1
                    flag = True
                    break
            if flag:
                break
    return new_grid, cnt_data


def get_score():
    score = 0
    group_grid = [[0]*N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if group_grid[row][col] or not grid[row][col]:
                continue

            neighborhood_set = set()
            curr_group = grid[row][col]
            group_grid[row][col] = curr_group

            Q = deque([(row, col)])
            while Q:
                curr_row, curr_col = Q.popleft()
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or not grid[next_row][next_col]:
                        continue

                    if group_grid[next_row][next_col]:
                        if group_grid[next_row][next_col] != curr_group:
                            neighborhood_set.add(group_grid[next_row][next_col])
                        continue

                    if grid[next_row][next_col] == curr_group:
                        group_grid[next_row][next_col] = curr_group
                        Q.append((next_row, next_col))

            for num in neighborhood_set:
                score += cnt_data[num] * cnt_data[curr_group]
    return score


def print_grid():
    print(f'----{idx+1}----')
    for row in grid:
        print(*row)


# =====================================================================
# 세팅

N, Q = map(int, input().split())
grid = [[0]*N for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(Q)]

# ======================================================================
# 실행부

answer = []
for idx, (sr, sc, er, ec) in enumerate(commands):
    # 1. 미생물 놓기
    put(sr, sc, er, ec, idx+1)

    # 2. 배양 용기 이동. 여기서 데이터 뽑아내면 될듯?
    grid, cnt_data = move()

    # 3. 실험 결과 기록
    curr_answer = get_score()
    answer.append(str(curr_answer))

# 정답 출력
print('\n'.join(answer))