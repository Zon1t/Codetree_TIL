# 큐 안 쓰는 버전

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def bfs(find_grid):
    return_lst = []
    visited = [[False] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if visited[row][col]:
                continue

            visited[row][col] = True

            lst = [(row, col)]
            pointer, cnt = 0, 1
            while pointer < cnt:
                for d in range(4):
                    next_row, next_col = lst[pointer][0] + dr[d], lst[pointer][1] + dc[d]

                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if find_grid[next_row][next_col] != find_grid[lst[pointer][0]][lst[pointer][1]]:
                        continue

                    visited[next_row][next_col] = True
                    lst.append((next_row, next_col))
                    cnt += 1

                pointer += 1

            if cnt < 3:
                continue
            else:
                return_lst += lst

    return return_lst, len(return_lst)


def small_bfs(lst):
    visited = [[False] * 5 for _ in range(5)]
    return_lst = []
    for row, col in lst:
        if visited[row][col]:
            continue

        visited[row][col] = True
        pointer, cnt = 0, 1

        Q = [(row, col)]
        while pointer < cnt:
            for d in range(4):
                next_row, next_col = Q[pointer][0] + dr[d], Q[pointer][1] + dc[d]
                if not in_range(next_row, next_col) or visited[next_row][next_col]:
                    continue
                if grid[next_row][next_col] != grid[Q[pointer][0]][Q[pointer][1]]:
                    continue

                visited[next_row][next_col] = True
                Q.append((next_row, next_col))
                cnt += 1
            pointer += 1

        if cnt < 3:
            continue
        else:
            return_lst += Q

    return return_lst



def rotate(sr, sc, cnt_):
    temp_grid = [row[sc:sc + 3] for row in grid[sr:sr + 3]]
    if cnt_ == 1:
        temp_grid = [row[::-1] for row in zip(*temp_grid)]
    elif cnt_ == 2:
        temp_grid = [row[::-1] for row in temp_grid[::-1]]
    else:
        temp_grid = [row[:] for row in zip(*temp_grid)][::-1]

    return_grid = [row[:] for row in grid]

    for delta_row in range(3):
        for delta_col in range(3):
            return_grid[sr + delta_row][sc + delta_col] = temp_grid[delta_row][delta_col]

    return return_grid


def priority():
    curr_max = (0, 0, 0, 0)
    max_lst, max_grid = None, None
    for row in range(3):
        for col in range(3):
            for cnt in range(1, 4):
                rotate_grid = rotate(row, col, cnt)
                pos_lst, money = bfs(rotate_grid)

                if curr_max < (money, -cnt, -col, -row):
                    curr_max = (money, -cnt, -col, -row)
                    max_grid = rotate_grid
                    max_lst = pos_lst
    
    return max_lst, max_grid, -curr_max[3], -curr_max[2] 


def get_money(lst):
    global fill_pointer
    for row, col in lst:
        grid[row][col] = fill_nums[fill_pointer]
        fill_pointer += 1
    return len(lst)


def custom_print():
    print(f'----grid----')
    for row in grid:
        print(*row)


# =============================================================
# 입력받기

K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]

fill_nums = list(map(int, input().split()))
fill_pointer = 0
ordering_rule = lambda x: (x[1], -x[0])

# ==============================================================
# 실행부

answer = []
for _ in range(K):
    # 1. 우선 순위에 의거한 회전 시키기.
    lst, grid, rotate_col, rotate_row = priority()
    # ** 종료 체크하기.
    if lst is None:
        break

    # 2. 유물 획득하기.
    lst.sort(key=ordering_rule)
    curr_money = get_money(lst)

    # 3. 연쇄작용 처리.
    while True:
        lst = small_bfs(lst)

        if lst:
            lst.sort(key=ordering_rule)
            curr_money += get_money(lst)
        else:
            break

    # 4. 정답 기록하기.
    answer.append(curr_money)

# 정답 출력
print(*answer)