# 굉장히 귀찮은 문제이다. 1. 구성에 의거 get_dist 함수를 따로 선언하자.
# 2. 우선 순위에 의거해서 산타를 찾자. 이때 중요한 점은 거리가 우리가 생각하는 거리가 아니라는 것.
# -> 즉 단순 bfs로 찾아야 하는 부분이 절대 아니라는 것이다.
# + 8방향 처리 잘해주기.
# 3. 1~P번 순서대로 move 처리. 이동 로직을 적절하게 구성해 이동할 수 있고 없고를 정확하게 판단하자.
# 4. 2, 3번 과정에서의 충돌 처리를 잘하자. 점수 업뎃 + 밀려난 위치 잘 판단하기.
# 5. 상호작용도 함수 맞게끔 세팅
# 6. 기절은 따로 변수 만들어서 관리
# 7. 조기 종료 처리 적절하게 잘하면 문제 없을 듯??
# 거리 연산 등 그냥 순회하면서 찾아보자. 그러면 될 듯?
# 클래스 쓰고 싶다..


dr = [-1, 0, 1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, 1, -1]

INF = float('inf')


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2


def gorani_move():
    global gorani_row, gorani_col

    target = (INF, INF, INF)
    for idx in range(P):
        if santa_out[idx]:
            continue

        curr_dist = get_dist((gorani_row, gorani_col), santa_lst[idx])
        santa_row, santa_col = santa_lst[idx]
        curr_status = (curr_dist, -santa_row, -santa_col)

        if curr_status < target:
            target = curr_status

    min_dist, next_dir = INF, -1
    for d in range(8):
        next_row, next_col = gorani_row + dr[d], gorani_col + dc[d]

        if not in_range(next_row, next_col):
            continue

        next_dist = get_dist((next_row, next_col), (-target[1], -target[2]))
        if next_dist < min_dist:
            min_dist, next_dir = next_dist, d

    gorani_row, gorani_col = gorani_row + dr[next_dir], gorani_col + dc[next_dir]
    if santa_grid[gorani_row][gorani_col] != -1:
        gorani_accident(santa_grid[gorani_row][gorani_col], next_dir)


def gorani_accident(santa_idx, d):
    santa_row, santa_col = santa_lst[santa_idx]
    santa_grid[santa_row][santa_col] = -1
    scores[santa_idx] += C
    sturn[santa_idx] = turn+2

    next_row, next_col = santa_row + dr[d]*C, santa_col + dc[d]*C
    if not in_range(next_row, next_col):
        santa_out[santa_idx] = True
    else:
        if santa_grid[next_row][next_col] == -1:
            santa_grid[next_row][next_col] = santa_idx
            santa_lst[santa_idx] = (next_row, next_col)
        else:
            interaction(santa_idx, next_row, next_col, d)


def santa_move(idx):
    curr_row, curr_col = santa_lst[idx]
    santa_grid[curr_row][curr_col] = -1

    min_dist, next_dir = get_dist((gorani_row, gorani_col), (curr_row, curr_col)), -1
    for d in range(4):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col) or santa_grid[next_row][next_col] != -1:
            continue
        next_dist = get_dist((gorani_row, gorani_col), (next_row, next_col))
        if next_dist < min_dist:
            min_dist, next_dir = next_dist, d

    if next_dir == -1:
        santa_grid[curr_row][curr_col] = idx
        return

    curr_row, curr_col = curr_row+dr[next_dir], curr_col+dc[next_dir]
    if curr_row == gorani_row and curr_col == gorani_col:
        santa_accident(idx, next_dir)
    else:
        santa_grid[curr_row][curr_col] = idx
        santa_lst[idx] = (curr_row, curr_col)

# 인덱스 처리도 해주기.
def santa_accident(santa_idx, d):
    santa_row, santa_col = santa_lst[santa_idx]
    santa_grid[santa_row][santa_col] = -1
    scores[santa_idx] += D
    sturn[santa_idx] = turn+2

    next_row, next_col = santa_row - dr[d]*(D-1), santa_col - dc[d]*(D-1)
    if not in_range(next_row, next_col):
        santa_out[santa_idx] = True
    else:
        if santa_grid[next_row][next_col] == -1:
            santa_grid[next_row][next_col] = santa_idx
            santa_lst[santa_idx] = (next_row, next_col)
        else:
            interaction(santa_idx, next_row, next_col, (d+2)%4)


def interaction(attack_idx, row, col, direction):
    pushed_santa = santa_grid[row][col]
    santa_grid[row][col] = attack_idx
    santa_lst[attack_idx] = (row, col)

    next_row, next_col = row + dr[direction], col + dc[direction]
    if not in_range(next_row, next_col):
        santa_out[pushed_santa] = True
    else:
        if santa_grid[next_row][next_col] == -1:
            santa_grid[next_row][next_col] = pushed_santa
            santa_lst[pushed_santa] = (next_row, next_col)
        else:
            interaction(pushed_santa, next_row, next_col, direction)


def custom_print():
    print(f'----grid----')
    for row in range(N):
        for col in range(N):
            if row == gorani_row and col == gorani_col:
                print('G', end=' ')
            else:
                print(santa_grid[row][col], end=' ')
        print()
    print(f'----turn:{turn}----')
    print(*scores)


scaling = lambda x: int(x)-1

# ========================================================
# 입력받기
N, M, P, C, D = map(int, input().split())
gorani_row, gorani_col = map(scaling, input().split())

santa_lst = [(-1, -1)] * P
santa_grid = [[-1] * N for _ in range(N)]
for _ in range(P):
    num, santa_row, santa_col = map(scaling, input().split())
    santa_grid[santa_row][santa_col] = num
    santa_lst[num] = (santa_row, santa_col)

santa_out = [False] * P
scores = [0] * P
sturn = [0] * P

# ========================================================
# 실행부
for turn in range(1, M+1):
    # 1. 루돌프 움직이기.
    gorani_move()

    # 2. 산타 움직이기.
    for idx in range(P):
        # 경기장에서 벗어난 산타 or 기절했으면 넘기기.
        if santa_out[idx] or turn < sturn[idx]:
            continue

        santa_move(idx)

    keep_going = False
    # 3. 턴 종료
    for idx in range(P):
        if santa_out[idx]:
            continue
        scores[idx] += 1
        keep_going = True

    # 조기 종료 체크
    if not keep_going:
        break

# 정답 출력하기
print(*scores)