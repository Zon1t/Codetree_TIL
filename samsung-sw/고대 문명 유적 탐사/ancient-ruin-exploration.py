# 다른 점? 탐사 결과마다 출력을 찍어야 한다는거.
# 이게 완탐이 되나 싶었는데 K도 10이고 5*5면 할만한 것 같기도 하다.. 복사 해가면서 돌려야 하나?
# 우선순위를 잘 따지자. (획득 가치, 각작, 열작, 행작), 가치를 따질 때에는 최소 3조각 이상.
# 연쇄 작용이 이제 메인 테마인가 계속 나오는 것 같다. 부족한 조각은 없으니 잘 채워보자.

from collections import deque


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def bfs(find_grid, set_return=False):
    if set_return:
        return_set.clear()

    return_value = 0
    visited = [[False] * 5 for _ in range(5)]
    for row in range(5):
        for col in range(5):
            if visited[row][col]:
                continue

            temp = 0
            temp_set = set()
            visited[row][col] = True

            Q = deque([(row, col)])
            while Q:
                curr_row, curr_col = Q.popleft()
                temp += 1

                if set_return:
                    temp_set.add((curr_row, curr_col))

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
            else:
                if set_return:
                    return_set.update(temp_set)
                return_value += temp

    return return_value


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
    for row in range(3):
        for col in range(3):
            for cnt in range(1, 4):
                rotate_grid = rotate(row, col, cnt)
                money = bfs(rotate_grid)

                if curr_max < (money, -cnt, -col, -row):
                    curr_max = (money, -cnt, -col, -row)

    return (-curr_max[1], -curr_max[2], -curr_max[3]) if curr_max[0] != 0 else (-1, -1, -1)


def get_money():
    for row, col in return_set:
        grid[row][col] = 0
    return len(return_set)


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
return_set = set()
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
        bfs(grid, True)

        earn = 0
        if return_set:
            total_earn += get_money()
            fill()
        else:
            break

    # 4. 정답 기록하기.
    answer.append(total_earn)

print(*answer)