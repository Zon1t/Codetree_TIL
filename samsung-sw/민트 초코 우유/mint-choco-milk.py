# 비트마스킹 써서 해결하면 될 것 같다.
# 1. 아침 시간 : 모든 사람의 신앙심이 1 증가
# 2. 점심 시간 : 1. 그룹 형성. 그룹 & 대표자에 대한 정보 기록 필요
#               2. 신앙심 1씩 대표자에게 넘기기
# 3. 저녁 시간 : 1. 신앙 전파. 이것도 우선순위에 의거하여, 대표자 신앙심, 행작, 열작
#               2. 해당 순서대로, 정해진 방향에 대해 전파 시작.

# 테케 검증 완료 - 9:58
# 대표자 먼저 찾으면 아침 과정 스킵 가능. 그래도 굳이 나대지 말자.

# 주어진 조건에 의거
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def morning():
    for row in range(N):
        for col in range(N):
            how_much[row][col] += 1


def lunch():
    visited = [[False] * N for _ in range(N)]
    rep_lst = []
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue
            visited[row][col] = True

            lst = [(row, col)]
            pointer, cnt, rep = 0, 1, (-how_much[row][col], row, col)
            while pointer < cnt:
                curr_row, curr_col = lst[pointer]
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if trust_grid[curr_row][curr_col] != trust_grid[next_row][next_col]:
                        continue

                    if (-how_much[next_row][next_col], next_row, next_col) < rep:
                        rep = (-how_much[next_row][next_col], next_row, next_col)
                    visited[next_row][next_col] = True
                    lst.append((next_row, next_col))
                    cnt += 1
                pointer += 1

            # 신앙심 모으기.
            rep_pos = rep[1:]
            for tr, tc in lst:
                how_much[tr][tc] += -1 if (tr, tc) != rep_pos else len(lst)-1

            # 저녁 시간을 수월하게 보내기 위한 세팅들..
            pick_cnt = 0
            for i in range(3):
                if trust_grid[row][col] & (1<<i):
                    pick_cnt += 1

            rep_lst.append(rep_pos+(how_much[rep_pos[0]][rep_pos[1]], pick_cnt))

    # pick_cnt 작은 순, 신앙심이 큰 순, 행 작은 순, 열 작은 순
    rep_lst.sort(key=lambda x: (x[3], -x[2], x[0], x[1]))
    return rep_lst


def dinner():
    change_set.clear()
    for row, col, B, _ in rep_lst:
        if (row, col) in change_set:
            continue

        how_much[row][col] = 1
        remain, my_fav = B-1, trust_grid[row][col]

        curr_dir = B%4
        next_row, next_col = row + dr[curr_dir], col + dc[curr_dir]
        while remain > 0 and in_range(next_row, next_col):
            if trust_grid[next_row][next_col] == my_fav:
                next_row += dr[curr_dir]
                next_col += dc[curr_dir]
                continue

            # 전파.
            change_set.add((next_row, next_col))
            if how_much[next_row][next_col] < remain:
                trust_grid[next_row][next_col] = my_fav
                how_much[next_row][next_col] += 1
                remain -= how_much[next_row][next_col]
            else:
                for i in range(3):
                    pick = 1<<i
                    if (my_fav&pick) and not (trust_grid[next_row][next_col]&pick):
                        trust_grid[next_row][next_col] |= pick
                how_much[next_row][next_col] += remain
                break

            next_row += dr[curr_dir]
            next_col += dc[curr_dir]


def get_answer():
    total_lst = [0] * 8
    for row in range(N):
        for col in range(N):
            total_lst[trust_grid[row][col]] += how_much[row][col]

    for idx in answer_idx:
        yield total_lst[idx]


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# ==================================================
# 세팅

N, T = map(int, input().split())

trust_grid = [[0] * N for _ in range(N)]
for i in range(N):
    for j, val in enumerate(input()):
        trust_grid[i][j] = 1 if val == 'T' else 2 if val == 'C' else 4

how_much = [list(map(int, input().split())) for _ in range(N)]
answer_idx = [7, 3, 5, 6, 4, 2, 1]
change_set = set()

# ==================================================
# 실행부

for _ in range(T):
    # 1. 아침 시간
    morning()

    # 2. 점심 시간
    rep_lst = lunch()

    # 3. 저녁 시간
    dinner()

    # 4. 정답 출력
    answer = get_answer()
    print(*answer)