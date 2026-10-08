# 09:01 시작

# 1. 미생물 투입
#       - 90도 돌려서 생각하면 문제 풀이하기 편할듯
#       - grid 위에 덮어쓰면 잡아먹기 처리 가능
#       - 영역 갈라지는 부분은 2번 과정과 함께 진행하면 될 듯.

# 2. 배양 용기 이동
#       - group 지어가며 상대 좌표 기록하기.
#       - 개수 기록 및 갈리지는거 체크.
#       - 행작 - 열작 우선순위 잘 지키기.
#       - 옮기는 것이 불가능한 경우 버리기.

# 3. 실험 결과 기록
#       - 개수는 잘 저장되어 있을 것이고..
#       - 인접 체크를 그냥 한 번 더 순회? 아니면 2번 단계 옮기면서 체크?
#       - 그냥 옮기면서 체크하는게 좋지 않나 싶다.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def check(pos, row, col, grid):
    for delta_row, delta_col in pos:
        check_row, check_col = row + delta_row, col + delta_col
        if not in_range(check_row, check_col) or grid[check_row][check_col]:
            return False
    return True


def move():
    visited = [[False] * N for _ in range(N)]
    removed_set = set()
    pos_info = dict()

    for row in range(N):
        for col in range(N):
            if not grid[row][col] or visited[row][col]:
                continue

            curr_idx = grid[row][col]
            if curr_idx in removed_set:
                continue

            if curr_idx in pos_info:
                pos_info.pop(curr_idx)
                removed_set.add(curr_idx)
                continue

            pos = []

            lst = [(row, col)]
            visited[row][col] = True
            pointer, cnt = 0, 1
            while pointer < cnt:
                curr_row, curr_col = lst[pointer]
                pointer += 1

                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if grid[next_row][next_col] != curr_idx:
                        continue

                    visited[next_row][next_col] = True
                    lst.append((next_row, next_col))
                    pos.append((next_row-row, next_col-col))
                    cnt += 1

            pos_info[curr_idx] = (cnt, curr_idx, pos)
    ordered_lst = list(pos_info.values())
    ordered_lst.sort(key=lambda x: (-x[0], x[1]))

    new_grid = [[0] * N for _ in range(N)]
    for _, curr_idx, pos in ordered_lst:
        done = False
        for row in range(N):
            for col in range(N):
                if new_grid[row][col]:
                    continue
                if check(pos, row, col, new_grid):
                    new_grid[row][col] = curr_idx
                    for delta_row, delta_col in pos:
                        new_grid[row+delta_row][col+delta_col] = curr_idx
                    done = True
                    break
            if done:
                break
    return new_grid, pos_info


def write():
    temp = 0
    check_pair = set()
    for row in range(N):
        for col in range(N):
            if not grid[row][col]:
                continue
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or not grid[next_row][next_col]:
                    continue
                if grid[row][col] == grid[next_row][next_col]:
                    continue

                min_idx, max_idx = min(grid[row][col], grid[next_row][next_col]), max(grid[row][col], grid[next_row][next_col])
                if (min_idx, max_idx) in check_pair:
                    continue

                temp += info[min_idx][0] * info[max_idx][0]
                check_pair.add((min_idx, max_idx))
    return temp


# ================================================================
# 세팅

N, Q = map(int, input().split())
grid = [[0] * N for _ in range(N)]
commands = [map(int, input().split()) for _ in range(Q)]
answer = []

# ================================================================
# 실행부

for idx, (start_row, start_col, end_row, end_col) in enumerate(commands):
    # 1. 미생물 투입.
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            grid[row][col] = idx+1

    # 2. 배양 용기 이동
    grid, info = move()

    # 3. 실험 결과 기록
    answer.append(str(write()))

# 정답 출력
print('\n'.join(answer))