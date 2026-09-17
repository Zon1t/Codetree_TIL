# 3:53 시작
# 놓칠 수 있을 법한 조건들이 많이 있는 것 같다. 이를 염두해두고 잘 문제를 풀어보자.
# 나무 성장 / 번식 -> 모두 동시에 일어남.
# 제초제는 최대한 많이 줄일 수 있는 위치에 뿌린다.
# grow -> burnsick -> find -> fire
# 제초제 유지되는 시간 따로 관리하기. 박멸한 나무의 수 실시간으로 기록하기.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def grow():
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]

                if not in_range(next_row, next_col):
                    continue
                if grid[next_row][next_col] < 1:
                    continue

                grid[row][col] += 1
                grid[next_row][next_col] += 1


def burnsick():
    burnsick_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue

            grow_lst = []
            cnt = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] != 0:
                    continue
                if fired[next_row][next_col] >= turn:
                    continue

                grow_lst.append((next_row, next_col))
                cnt += 1

            if not cnt:
                continue

            grow_amount = grid[row][col] // cnt
            for gr, gc in grow_lst:
                burnsick_grid[gr][gc] += grow_amount

    for row in range(N):
        for col in range(N):
            grid[row][col] += burnsick_grid[row][col]


def find():
    standard = (0, 0, 0)
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue
            temp = grid[row][col]
            for delta_row, delta_col in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                for k in range(1, K+1):
                    next_row, next_col = row + delta_row*k, col + delta_col*k
                    if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                        break
                    temp += grid[next_row][next_col]
            if standard < (temp, -row, -col):
                standard = (temp, -row, -col)

    return -standard[1], -standard[2]


def fire(start_row, start_col):
    temp = grid[start_row][start_col]
    if temp < 1:
        return 0
    grid[start_row][start_col] = 0
    fired[start_row][start_col] = turn + C
    for delta_row, delta_col in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        for k in range(1, K + 1):
            next_row, next_col = start_row + delta_row * k, start_col + delta_col * k
            if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                break

            fired[next_row][next_col] = turn + C
            if grid[next_row][next_col] > 0:
                temp += grid[next_row][next_col]
                grid[next_row][next_col] = 0
            elif grid[next_row][next_col] == 0:
                break
    return temp


def print_grid():
    print(f'----namu_grid----')
    for row in grid:
        print(*row)
    print(f'----kill_grid----')
    for row in fired:
        print(*row)
    print(f'{turn}_answer:{answer}')

# =========================================================
# 입력
N, M, K, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
fired = [[0] * N for _ in range(N)]

# =========================================================
# 실행
answer = 0
for turn in range(1, M+1):
    # 1. 나무 성장
    grow()

    # 2. 나무 번식
    burnsick()

    # 3. 위치 찾기
    kill_row, kill_col = find()

    # 4. 살포하기
    answer += fire(kill_row, kill_col)

print(answer)