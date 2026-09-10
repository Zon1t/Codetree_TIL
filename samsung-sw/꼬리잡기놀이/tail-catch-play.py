''' 꼬리잡기놀이 / 20260910 / 체감 난이도 : 골드2~3
소요 시간 : 69분 / 시도 : 2회 (1회차 : 틀림) / 실행 시간 : 73ms / 메모리 : 17MB

타임 라인 : 구상(19분) - 구현(39분) - 검증(4분) - 수정(7분)


[구상]
    - 솔직히 감을 잡기 어려운 문제였다고 생각된다. 머리 이후 사람들을 어떻게 관리해야 하는가에
    대해서 적잖게 고민을 해봤는데, 전체를 옮겼을 때 시/공간적으로 빡셀 수도 있겠다는 생각이 들
    었다. 이런 부류는 빡세거나 헷갈릴 소요가 있지만 포인터로 머리사람을 가리키게 하여, 문제를
    푸는 편이 좋을 것이라 생각이 들었고, 이를 바탕으로 해결하고자 했다.
    - 포인터를 사용하고자 하니 다양한 사전 준비 작업들이 필요했다. 경로도 따야하고, 해당 경로는
    어느 팀의 경로인지, 해당 팀 경로에서 몇 번째 위치인지 등 필요하다고 생각하여 적절한 변수들
    을 선언하고 틀을 만들어 보았다.

[구현]
    - 구상 단계에서 생각했던 변수들 이외에 많은 변수들을 추가해주었다. 사람 수 / 경로 길이 /
    등등.. 경로를 따는 로직을 만든 이후 해당 로직에 계속 추가해주었다. 이러한 부분은 구현 단
    계에서 더 잘보인다고 생각하여 괜찮다고 생각한다.
    - 이번에는 조금 빠르게 판단하여, 하드코딩할 부분은 그냥 시원하게 하드코딩 하고 넘어갔다. 공
    던지기 로직과 해당 위치에 사람이 있는지 체크하는 로직이 이에 해당한다.
    - 구현하다가 막히진 않았던 것 같은데, 기본 구현량이 많기도 하고 검증도 하다보니 시간을 많이
    잡아먹은 것 같다.

[검증]
    - grid와 초기 정보 세팅은 구현 단계에서 여러번 확인했기에, pointer변화(뒤집힐 때에도),
    점수 추가 로직 등 정도를 추가로 확인하고 제출해보았다.

[수정]
    - 이번엔 문제도 잘 읽었는데, 또 뭘 놓친거지 싶었다. 문제를 다시 읽어도 괜찮았고 내 코드를 읽
    다보니 곧바로 문제점이 보였다. 그림을 보면서 순회 순서를 잡았었는데, 이걸 반대로 잡은 것...
    수정하니 바로 정답이였다. 특히 이런 로직들은 옛날에 연습해본 바 있기도 하고, 매번 자신감 있게
    짜는 것 같은데 틀리는 경우가 적지 않은 것 같다. 심지어 이런건 따로 temp.py나 떼어 와서 확인
    하면 금방 알 수 있는건데.. 반성해야겠다.

* 피드백
    이젠 그냥 맨날 바보짓 못해도 하나씩은 하는 것 같다. 세부 로직들도 검증 잘 하고 넘어가자.
'''

# 관리 관리 팀 사람들에 대한 위치 관리를 어떻게 진행할 것인가?? 직관적으로는 포인터 사용 문제 같기는
# 하다. 이를 바탕으로 문제 풀이를 진행해보자.
# 라운드가 1000까지 있고.. 순서 관리? 에지라고 할 부분이 있을까? round는 -1해서 생각하는게 편할듯
# 틀 짜보면서 더 생각해보자.


# 범위 체크
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 정확히는 팀을 만드는 함수. 문제 풀이에 필요한 grid, 데이터를 업데이트 해준다.
def make_grid(start_row, start_col):
    team_grid[start_row][start_col] = team_num
    order_grid[start_row][start_col] = 0

    # 어느 방향으로 진행할지 갈피만 잡아주자. 최소 3명 이상이니 ㄱㅊ
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

    cnt = 2         # 사람 수도 세어줘야 함.
    while True:
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 경로 벗어남 or 경로 아님 or 이미 탐색한 격자 -> continue
            if not in_range(next_row, next_col):
                continue
            if grid[next_row][next_col] == 0 or team_grid[next_row][next_col]:
                continue

            # 경로를 찾은 것임.
            team_grid[next_row][next_col] = team_num
            order_grid[next_row][next_col] = order_grid[curr_row][curr_col] + 1
            curr_row, curr_col = next_row, next_col

            # 사람이면 사람 수 카운트
            if grid[curr_row][curr_col] != 4:
                cnt += 1
            break

        # break가 안되었다면 해당 팀 경로는 모두 찾은 것. while문을 멈춰주자.
        else:
            break

    # 사람 수, 경로 길이는 추가해주자.
    human_cnts.append(cnt)
    path_length.append(order_grid[curr_row][curr_col]+1)

# 머리 사람 이동하기.
def move():
    for team_idx in range(1, M+1):
        pointers[team_idx] = (pointers[team_idx] + (-1 if team_status[team_idx] else 1)) % path_length[team_idx]

# 공 던져
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

# 거기 사람 있어요?
def is_there_human(row, col):
    global answer
    curr_team, curr_order = team_grid[row][col], order_grid[row][col]

    # 정방향 이동의 경우
    if team_status[curr_team]:
        order_diff = (curr_order - pointers[curr_team]) % path_length[curr_team]
        if order_diff < human_cnts[curr_team]:
            answer += (order_diff+1) ** 2
            pointers[curr_team] = (pointers[curr_team] + human_cnts[curr_team] - 1) % path_length[curr_team]
            team_status[curr_team] = False
            return True

    # 역방향 이동의 경우
    else:
        order_diff = (pointers[curr_team] - curr_order) % path_length[curr_team]
        if order_diff < human_cnts[curr_team]:
            answer += (order_diff+1) ** 2
            pointers[curr_team] = (pointers[curr_team] - human_cnts[curr_team] + 1) % path_length[curr_team]
            team_status[curr_team] = True
            return True

    # 여기까지 오면 사람이 없는거
    return False

# 초기 세팅값을 찍어보기 위함.
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

# 변화되는 요소를 관찰하기 위함.
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

path_length = [None]                        # 경로의 길이를 담아둠.
human_cnts = [None]                         # 팀별 사람 수를 담아둠.
team_status = [True]*(M+1)                  # 초기 방향인지 아닌지 여부를 담아둠.
pointers = [0]*(M+1)                        # 머리 사람의 위치를 담아둠.

# 데이터 업데이트 해주기. 머리사람 기준!
team_num = 0
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            team_num += 1
            make_grid(row, col)

# 실행부
answer = 0
for round in range(K):
    # 1. 머리사람 이동
    move()

    # 2. 공 던지기. 4N 라운드마다 다시 초기화
    throw((round//N)%4, round%N)

# 정답 출력
print(answer)