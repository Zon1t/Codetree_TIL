# 관리 관리 팀 사람들에 대한 위치 관리를 어떻게 진행할 것인가?? 직관적으로는 포인터 사용 문제 같기는
# 하다. 이를 바탕으로 문제 풀이를 진행해보자.
# 라운드가 1000까지 있고.. 순서 관리? 에지라고 할 부분이 있을까? round는 -1해서 생각하는게 편할듯
# 틀 짜보면서 더 생각해보자.


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def make_grid(start_row, start_col):
    team_grid[start_row][start_col] = team_num
    order_grid[start_row][start_col] = 0

    # 어느 방향으로 진행할지 갈피만 잡아주자.
    curr_row, curr_col = -1, -1
    for d in range(4):
        next_row, next_col = start_row + dr[d], start_col + dc[d]

        if not in_range(next_row, next_col):
            continue

        if grid[next_row][next_col] == 2:
            team_grid[next_row][next_col] = team_num
            order_grid[next_row][next_col] = 1
            curr_row, curr_col = next_row, next_col
            break

    cnt = 2
    while True:
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col):
                continue
            if grid[next_row][next_col] == 0 or team_grid[next_row][next_col]:
                continue

            # 경로를 찾은 것임.
            team_grid[next_row][next_col] = team_num
            order_grid[next_row][next_col] = order_grid[curr_row][curr_col] + 1
            curr_row, curr_col = next_row, next_col

            if grid[curr_row][curr_col] != 4:
                cnt += 1
            break

        # break가 안되었다면 해당 팀 경로는 모두 찾은 것. while문을 멈춰주자.
        else:
            break

    # 사람 수, 경로 길이는 추가해주자.
    human_cnts.append(cnt)
    path_length.append(order_grid[curr_row][curr_col]+1)


def move():
    for team_idx in range(1, M+1):
        pointers[team_idx] = (pointers[team_idx] + (-1 if team_status[team_idx] else 1)) % path_length[team_idx]


def throw(standard, pos):
    # 기세로 하드코딩이나 하자.
    if standard == 0:
        for idx in range(N):
            if team_grid[pos][idx] and is_there_human(pos, idx):
                return
    elif standard == 1:
        for idx in range(N-1, -1, -1):
            if team_grid[idx][pos] and is_there_human(idx, pos):
                return
    elif standard == 2:
        for idx in range(N-1, -1, -1):
            if team_grid[-1-pos][idx] and is_there_human(-1-pos, idx):
                return
    else:
        for idx in range(N):
            if team_grid[idx][-1-pos] and is_there_human(idx, -1-pos):
                return


def is_there_human(row, col):
    global answer
    curr_team, curr_order = team_grid[row][col], order_grid[row][col]
    if team_status[curr_team]:
        order_diff = (curr_order - pointers[curr_team]) % path_length[curr_team]
        if order_diff < human_cnts[curr_team]:
            answer += (order_diff+1) ** 2
            pointers[curr_team] = (pointers[curr_team] + human_cnts[curr_team] - 1) % path_length[curr_team]
            team_status[curr_team] = False
            return True
    else:
        order_diff = (pointers[curr_team] - curr_order) % path_length[curr_team]
        if order_diff < human_cnts[curr_team]:
            answer += (order_diff+1) ** 2
            pointers[curr_team] = (pointers[curr_team] - human_cnts[curr_team] + 1) % path_length[curr_team]
            team_status[curr_team] = True
            return True

    return False


def print_grid():
    print(f'----team_grid----')
    for row in team_grid:
        print(*row)

    print(f'----order_grid----')
    for row in order_grid:
        print(*row)

    print(f'----path_length----')
    print(*path_length)

    print(f'----human_cnts----')
    print(*human_cnts)


def custom_print():
    print(f'----curr_pointers----')
    print(*pointers)
    print(f'----team_status----')
    print(*team_status)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

team_grid = [[0]*N for _ in range(N)]       # 경로에 있어 어느 팀이 지나는 경로인지 체크
order_grid = [[-1] * N for _ in range(N)]   # 초기 머리사람 위치 기준 경로에 순서 부여

path_length = [None]            # 경로의 길이를 담아둠.
human_cnts = [None]             # 팀별 사람 수를 담아둠.
team_status = [True]*(M+1)      # 초기 방향인지 아닌지 여부를 담아둠.
pointers = [0]*(M+1)            # 머리 사람의 위치를 담아둠.

team_num = 0
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            team_num += 1
            make_grid(row, col)

answer = 0
for round in range(K):
    # 1. 머리사람 이동
    move()

    # 2. 공 던지기
    throw((round//N)%4, round%N)

# 정답 출력
print(answer)