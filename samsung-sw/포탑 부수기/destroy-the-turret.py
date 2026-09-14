# 우선 순위에 따른 처리를 올바르게 하는 것이 메인인 문제인 것 같다. 즉 우선순위 연산을 위한
# "언제 마지막으로 공격했는가?" 등에 대해서 잘 따져보아야 하므로, 관련 변수들을 잘 세팅해야 할듯?
# find_attack, find_target, l_attack, b_attack, update 이 정도만 구현하면 될 듯?
# 조기 종료 : 부서지지 않은 포탑이 한 개가 된다면 그 즉시 종료.


from collections import deque

# 우선순위에 의거
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# plan_b 함수에서 사용
atk_dr = [0, 1, 1, 1, 0, -1, -1, -1]
atk_dc = [1, 1, 0, -1, -1, -1, 0, 1]

INF = float('inf')

def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


def find():
    attack, target = (INF, INF, -INF, -INF), (-INF, -INF, INF, INF)
    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue

            curr_info = (grid[row][col], turn-last_attack[row][col], -row-col, -col)
            if curr_info < attack:
                attack = curr_info
            if curr_info > target:
                target = curr_info

    return attack[3]-attack[2], -attack[3], target[3]-target[2], -target[3]


def plan_a():
    # 1. 경로 받아오기.
    dist_grid = [[-1] * M for _ in range(N)]
    dist_grid[target_row][target_col] = 0

    Q = deque([(target_row, target_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if (curr_row, curr_col) == (attack_row, attack_col):
            break

        for d in range(4):
            next_row, next_col = (curr_row + dr[d])%N, (curr_col + dc[d])%M

            if not grid[next_row][next_col]:
                continue
            if dist_grid[next_row][next_col] != -1:
                continue

            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col] + 1
            Q.append((next_row, next_col))

    # 도달 불가능하면 plan_b로 넘어가야 함.
    if dist_grid[attack_row][attack_col] == -1:
        return False

    # 경로 위에 있는 적들 공격.
    curr_row, curr_col, damage = attack_row, attack_col, grid[attack_row][attack_col]
    half_damage = damage // 2
    while True:
        # 공격 다 했으면 종료. 마지막 지점은 진짜 데미지를 입혀야 함.
        if (curr_row, curr_col) == (target_row, target_col):
            grid[curr_row][curr_col] = max(grid[curr_row][curr_col]-damage+half_damage, 0)
            break

        for d in range(4):
            next_row, next_col = (curr_row + dr[d])%N, (curr_col + dc[d])%M
            if dist_grid[next_row][next_col] == dist_grid[curr_row][curr_col]-1:
                curr_row, curr_col = next_row, next_col
                grid[curr_row][curr_col] = max(grid[curr_row][curr_col]-half_damage, 0)
                check_set.add((curr_row, curr_col))
                break

    return True


def plan_b():
    damage, half_damage = grid[attack_row][attack_col], grid[attack_row][attack_col] // 2

    # 타겟 공격
    grid[target_row][target_col] = max(grid[target_row][target_col]-damage, 0)
    check_set.add((target_row, target_col))

    # 인접한 범위 공격
    for d in range(8):
        next_row, next_col = (target_row + atk_dr[d])%N, (target_col + atk_dc[d])%M

        # 공격자는 공격 안받음.
        if (next_row, next_col) == (attack_row, attack_col):
            continue

        grid[next_row][next_col] = max(grid[next_row][next_col]-half_damage, 0)
        check_set.add((next_row, next_col))


def check():
    cnt = 0
    for row in range(N):
        for col in range(M):
            if grid[row][col]:
                cnt += 1
    return cnt == 1


def update():
    for row in range(N):
        for col in range(M):
            if grid[row][col] and (row, col) not in check_set:
                grid[row][col] += 1


def get_answer():
    return max([max(row) for row in grid])


def custom_print():
    print(f'----attack & target----')
    print('attack:', attack_row, attack_col)
    print('target:', target_row, target_col)
    print(f'----grid status----')
    for row in grid:
        print(*row)


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0] * M for _ in range(N)]
check_set = set()

for turn in range(1, K+1):
    # 1-1. 공격자 & 타겟 선정.
    attack_row, attack_col, target_row, target_col = find()
    # 1-2. 공격력 업데이트.
    grid[attack_row][attack_col] += N+M
    # 1-3. 공격에 유관된 포탑 추가.
    check_set.add((attack_row, attack_col))
    # 1-4. last_attack 업데이트
    last_attack[attack_row][attack_col] = turn

    # 2-1. 공격
    if not plan_a():
        plan_b()
    # 2-2. 조기종료 체크. 만약 부서지지 않은 포탑이 1개가 되면 그 즉시 종료.
    if check():
        break

    # 3-1. 포탑 정비
    update()
    # 3-2. 체크 set 비우기
    check_set.clear()


# 정답 출력
answer = get_answer()
print(answer)