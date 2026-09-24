# 09:55 시작 [] / 59t 12t
# bfs 연결요소 찾기 + 중력 문제
# 1. 폭탄 묶음 찾기
# 2. 터뜨리기.
# 3. 중력 적용
# 4. 회전
# 5. 중력 적용


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def find():
    target_lst, rep = None, (0, 0, 0, 0)
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1 or visited[row][col]:
                continue

            visited[row][col] = True
            curr_color = grid[row][col]
            pos_prio = (-row, col)

            red_set = set()
            lst = [(row, col)]
            pointer, cnt = 0, 1
            while pointer < cnt:
                curr_row, curr_col = lst[pointer]
                pointer += 1

                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]

                    if not in_range(next_row, next_col) or grid[next_row][next_col] < 0:
                        continue
                    if visited[next_row][next_col]:
                        continue

                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col) in red_set:
                            continue

                        red_set.add((next_row, next_col))
                        lst.append((next_row, next_col))
                        cnt += 1
                    else:
                        if grid[next_row][next_col] != curr_color:
                            continue

                        visited[next_row][next_col] = True
                        lst.append((next_row, next_col))
                        cnt += 1
                        pos_prio = min(pos_prio, (-next_row, next_col))

            if cnt < 2:
                continue

            if (-cnt, len(red_set), pos_prio[0], pos_prio[1]) < rep:
                rep = (-cnt, len(red_set), pos_prio[0], pos_prio[1])
                target_lst = lst

    return target_lst


def apply_gravity():
    for col in range(N):
        pointer = N-1
        for row in range(N-1, -1, -1):
            if grid[row][col] == -1:
                pointer = row-1
            else:
                if grid[row][col] != -2:
                    if pointer != row:
                        grid[row][col], grid[pointer][col] = grid[pointer][col], grid[row][col]
                    pointer -= 1


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


# --------------------------------------------------------------
# 세팅

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 0

# ==============================================================
# 실행부

while True:
    # 1. 폭탄 묶음 찾기.
    kill_lst = find()
    if kill_lst is None:
        break

    # 2. 폭탄 터뜨리고 점수 업데이트
    for row, col in kill_lst:
        grid[row][col] = -2
    answer += len(kill_lst) ** 2

    # 3. 중력 적용하기
    apply_gravity()

    # 4. 회전
    grid = [list(row) for row in zip(*grid)][::-1]

    # 5. 중력 적용하기
    apply_gravity()

# 정답 출력하기
print(answer)