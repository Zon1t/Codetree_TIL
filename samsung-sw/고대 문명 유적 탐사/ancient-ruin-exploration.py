# 큐 안 쓰는 게 더 낫나?

from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def bfs(find_grid):
    Q = deque()
    return_value = 0
    visited = [[False] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if visited[row][col]:
                continue

            temp = 0
            visited[row][col] = True

            Q.append((row, col))
            while Q:
                curr_row, curr_col = Q.popleft()
                temp += 1

                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]

                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if find_grid[next_row][next_col] != find_grid[curr_row][curr_col]:
                        continue

                    visited[next_row][next_col] = True
                    Q.append((next_row, next_col))

            if temp < 3:
                continue
            return_value += temp

    return return_value


def swap(*lst, reverse=False):
    if reverse: return (lst[-1],)+lst[:-1]
    else: return lst[1:]+(lst[0],)


def rotate(sr, sc, cnt_):
    return_grid = [row[:] for row in grid]

    if cnt_ == 2:
        return_grid[sr][sc], return_grid[sr+2][sc+2] = swap(return_grid[sr][sc], return_grid[sr+2][sc+2])
        return_grid[sr][sc+1], return_grid[sr+2][sc+1] = swap(return_grid[sr][sc+1], return_grid[sr+2][sc+1])
        return_grid[sr][sc+2], return_grid[sr+2][sc] = swap(return_grid[sr][sc+2], return_grid[sr+2][sc])
        return_grid[sr+1][sc+2], return_grid[sr+1][sc] = swap(return_grid[sr+1][sc+2], return_grid[sr+1][sc])
    else:
        return_grid[sr][sc], return_grid[sr+2][sc], return_grid[sr+2][sc+2], return_grid[sr][sc+2] = \
            swap(return_grid[sr][sc], return_grid[sr+2][sc], return_grid[sr+2][sc+2], return_grid[sr][sc+2], reverse=cnt_==3)
        return_grid[sr][sc+1], return_grid[sr+1][sc], return_grid[sr+2][sc+1], return_grid[sr+1][sc+2] = \
            swap(return_grid[sr][sc+1], return_grid[sr+1][sc], return_grid[sr+2][sc+1], return_grid[sr+1][sc+2], reverse=cnt_==3)

    return return_grid


def priority():
    curr_max = (0, 0, 0, 0)
    for row in range(3):
        for col in range(3):
            for cnt in range(1, 4):
                rotate_grid = rotate(row, col, cnt)
                money = bfs(rotate_grid)

                if curr_max < (money, -cnt, -col, -row):
                    curr_max = (money, -cnt, -col, -row)

    return (-curr_max[1], -curr_max[2], -curr_max[3]) if curr_max[0] != 0 else (-1, -1, -1)


def get_money():
    total_money = 0
    visited = [[False] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if visited[row][col]:
                continue

            visited[row][col] = True
            cnt, pointer = 1, 0

            check_lst = [(row, col)]
            while pointer < cnt:
                curr_row, curr_col = check_lst[pointer]
                pointer += 1

                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if grid[next_row][next_col] != grid[curr_row][curr_col]:
                        continue
                    visited[next_row][next_col] = True
                    check_lst.append((next_row, next_col))
                    cnt += 1

            if cnt < 3:
                continue

            total_money += cnt
            for row, col in check_lst:
                grid[row][col] = 0

    return total_money


def fill():
    global fill_pointer
    for col in range(5):
        for row in range(4, -1, -1):
            if grid[row][col]:
                continue

            grid[row][col] = fill_nums[fill_pointer]
            fill_pointer += 1


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

# ==============================================================
# 실행부

answer = []
for _ in range(K):
    # 1. 회전할 부분 찾기.
    cnt, rotate_col, rotate_row = priority()
    # ** 종료 체크하기.
    if cnt == -1:
        break

    # 2. 회전시키기.
    grid = rotate(rotate_row, rotate_col, cnt)

    # 3. 유물 획득하기.
    total_earn = 0
    while True:
        money = get_money()

        if not money:
            break

        total_earn += money
        fill()

    # 4. 정답 기록하기.
    answer.append(total_earn)

print(*answer)