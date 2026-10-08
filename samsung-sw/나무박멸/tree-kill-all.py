# 10:00 시작
# 1. 나무 성장.
#       - 인접한 칸의 나무 수만큼 성장
#       - 동시에 일어나는 현상인데 굳이 동시 처리는 할 필요 없을 듯

# 2. 나무 번식
#       - 번식 가능한 칸 조사.
#       - 몫만큼 번식. 동시에 일어남.

# 3. 제초제 뿌리기.
#       - 박멸되는 나무가 가장 많은 칸 - 행 작 - 열 작
#       - 대각으로 퍼지는 도중에 빈 칸, 벽이 있는 경우 해당 칸 까지만 제초제를 뿌림.
#       - 제초제는 c년만큼 유지

dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def grow():
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                    continue
                grid[row][col] += 1
                grid[next_row][next_col] += 1


def burnsick():
    burnsick_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue

            curr_num = grid[row][col]
            cnt = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col]:
                    continue
                if turn <= death_grid[next_row][next_col]:
                    continue
                cnt += 1

            if not cnt:
                continue

            D = curr_num // cnt
            if not D:
                continue

            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col]:
                    continue
                if turn <= death_grid[next_row][next_col]:
                    continue
                burnsick_grid[next_row][next_col] += D

    for row in range(N):
        for col in range(N):
            grid[row][col] += burnsick_grid[row][col]


def find():
    target = (0, -N, -N)

    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue

            curr_cnt = grid[row][col]
            for d in range(4, 8):
                for k in range(1, K+1):
                    next_row, next_col = row + dr[d] * k, col + dc[d] * k
                    if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                        break
                    curr_cnt += grid[next_row][next_col]
            target = max(target, (curr_cnt, -row, -col))

    return -target[1], -target[2]


def kill():
    global answer

    target_row, target_col = find()
    if target_row == N:
        return False

    answer += grid[target_row][target_col]
    grid[target_row][target_col] = 0
    death_grid[target_row][target_col] = turn + C

    for d in range(4, 8):
        for k in range(1, K+1):
            next_row, next_col = target_row + dr[d] * k, target_col + dc[d] * k
            if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                break

            death_grid[next_row][next_col] = turn + C
            if grid[next_row][next_col] == 0:
                break
            else:
                answer += grid[next_row][next_col]
                grid[next_row][next_col] = 0

    return True


# ====================================================================
# 세팅

N, T, K, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
death_grid = [[-1] * N for _ in range(N)]
answer = 0

# ====================================================================
# 실행부

for turn in range(T):
    # 1. 나무 성장
    grow()

    # 2. 나무 번식
    burnsick()

    # 3. 죽이기
    if not kill():
        break

# 정답 출력
print(answer)