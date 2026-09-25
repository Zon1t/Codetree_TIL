# 15:22 시작
# [] /
# 사람이 거의 없음. 그냥 리스트로 관리하기.
# 탈출구 기준으로 잘 생각해서 문제를 해결하면 될 것 같다. 상대좌표를 이용한 회전 잘하기.


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def move():
    global answer
    for idx in range(M):
        if escape[idx]:
            continue

        curr_row, curr_col = human[idx]
        curr_dist = get_dist((curr_row, curr_col), EXIT)
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col]:
                continue

            next_dist = get_dist((next_row, next_col), EXIT)
            if next_dist < curr_dist:
                human[idx] = [next_row, next_col]
                answer += 1
                if [next_row, next_col] == EXIT:
                    escape[idx] = True
                break


def find():
    selected = (N, N, N)
    for idx in range(M):
        if escape[idx]:
            continue

        curr_row, curr_col = human[idx]
        curr_size = max(abs(curr_row-EXIT[0]), abs(curr_col-EXIT[1]))
        end_row, end_col = max(curr_row, EXIT[0]), max(curr_col, EXIT[1])
        start_row, start_col = max(0, end_row-curr_size), max(0, end_col-curr_size)

        selected = min(selected, (curr_size, start_row, start_col))
    return selected


def rotate(start_row, start_col, size):
    end_row, end_col = start_row + size, start_col + size
    temp_grid = [row[start_col:end_col] for row in grid[start_row:end_row]]

    for delta_row in range(size):
        for delta_col in range(size):
            grid[start_row+delta_row][start_col+delta_col] = temp_grid[-1-delta_col][delta_row] - (1 if temp_grid[-1-delta_col][delta_row] else 0)

    for idx in range(M):
        if escape[idx]:
            continue

        human_row, human_col = human[idx]
        if start_row <= human_row < end_row and start_col <= human_col < end_col:
            human[idx] = [start_row+human_col-start_col, end_col-1-human_row+start_row]

    EXIT[0], EXIT[1] = start_row+EXIT[1]-start_col, end_col-1-EXIT[0]+start_row


def print_grid():
    print('----grid----')
    temp_grid = [row[:] for row in grid]
    for idx in range(M):
        if escape[idx]:
            continue
        row, col = human[idx]
        temp_grid[row][col] = 'H'
    temp_grid[EXIT[0]][EXIT[1]] = 'E'
    for row in temp_grid:
        print(*row)



# =================================================================
# 세팅

scaling = lambda x: int(x)-1
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
human = [list(map(scaling, input().split())) for _ in range(M)]
escape = [False]*M
EXIT = list(map(scaling, input().split()))
answer = 0

# =================================================================
# 실행부

for _ in range(K):
    # 1. 사람 움직이기.
    move()

    # 조기종료 체크
    if sum(escape) == M:
        break

    # 2. 정사각형 찾기.
    size, start_row, start_col = find()

    # 3. 회전하기.
    rotate(start_row, start_col, size+1)

# 정답 출력하기.
print(answer)
print(EXIT[0]+1, EXIT[1]+1)