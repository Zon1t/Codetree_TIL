''' 포탑 부수기 / 20260914 / 체감 난이도 : 골드 1~2
소요 시간 : 64분 / 시도 : 1회 / 실행 시간 : 181ms / 메모리 : 22MB

타임 라인 : 구상(17분) - 구현(36분) - 검증(11분)

[구상]
    - 기능을 수행하기 위한 로직 자체는 크게 어려운 것이 없다고 판단했다. 우선 순위에 의거한
    대상 찾기 & 경로 탐색 등 개별적인 기능들은 다 이전에 구현해봤던 것들이였기 때문이다.
    - 전역으로 세팅해야 할 변수들이 많지 않기도 했고, 기능 구현하면서 맞춰가면 되는 것들이
    대부분이라 구현을 하는 과정에서 고쳐나가자는 생각을 했다. 구현량이 많았음에도 구상을 많
    이 하진 않은 것 같다.
    - 내가 만들어야 할 함수들만 세팅하고, 틀 만들고, 문제 읽으며 주의 사항 세팅하고 구현
    단계로 넘어갔다.

[구현]
    - find_attack & find_target 함수는 우선순위가 정반대임을 고려하여 그냥 하나의 함수
    로 만드는 것이 좋다 생각하여 수정했다.
    - 구현 과정에서 수정한 부분이 엄청 많았다. 큰 부분에선 다음과 같다.
        1) 범위 밖 벗어나는 부분 다시 세팅. 사실 in_range를 선언할 필요가 없었다.
        2) 포탑 부서짐 처리. 음수가 될 수 있었는데, 그냥 max 0 때려서 처리했다. 나중에
         처리해야 하나 고민했었는데, 그럴 소요가 없었기 때문이다.
        3) 공격자는 데미지를 안 받는데 기능 구현 후 단위 검증 과정에서 추가했다.
        4) last_attack grid를 업데이트 하지 않고 있었다.
        5) 조기 종료 세팅을 추가해주었다.
    - 구현하면서 체크해가면 되겠다 생각했는데, 생각보다 고려 사항이 너무 많았다. 이런건 생각
    날 때마다 주석/종이에 남길 필요가 있겠다.    *

[검증]
    - 예제 기준 라운드 수만 올려서 변화 양상을 관찰해보았다. 우선순위에 의거한 공격자/피공격
    자는 올바르게 찾는지, 조기 종료 조건이 잘 작동하는가 등 체크해보고 제출해보았다.
'''

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


def find():
    # 공격자 / 피공격자 초기 세팅.
    attack, target = (INF, INF, -INF, -INF), (-INF, -INF, INF, INF)
    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue
            
            # 우선 순위에 의거한 변수 세팅
            curr_info = (grid[row][col], turn-last_attack[row][col], -row-col, -col)
            
            # 변수 업데이트
            if curr_info < attack:
                attack = curr_info
            if curr_info > target:
                target = curr_info
    
    # 좌표 반환.
    return attack[3]-attack[2], -attack[3], target[3]-target[2], -target[3]

# 레이저 공격
def plan_a():
    # 1. 경로 찾기를 위한 distance map 만들기
    dist_grid = [[-1] * M for _ in range(N)]
    dist_grid[target_row][target_col] = 0

    Q = deque([(target_row, target_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        # 공격자 발견하면 종료
        if (curr_row, curr_col) == (attack_row, attack_col):
            break

        # 아니면 인접한 영역 탐색.
        for d in range(4):
            next_row, next_col = (curr_row + dr[d])%N, (curr_col + dc[d])%M

            # 포탑이 없거나 이미 방문한 칸이면 넘김.
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
        
        # 경로 따라가면서 경로상 적들 데미지 입히기.
        for d in range(4):
            next_row, next_col = (curr_row + dr[d])%N, (curr_col + dc[d])%M
            if dist_grid[next_row][next_col] == dist_grid[curr_row][curr_col]-1:
                curr_row, curr_col = next_row, next_col
                grid[curr_row][curr_col] = max(grid[curr_row][curr_col]-half_damage, 0)
                check_set.add((curr_row, curr_col))
                break

    # plan_a 정상적으로 수행 
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

# 조기 종료 조건 : 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지.
def check():
    cnt = 0
    for row in range(N):
        for col in range(M):
            if grid[row][col]:
                cnt += 1
    return cnt == 1

# 부서지지 않고, 공격에 관여하지 않았다면 += 1 처리
def update():
    for row in range(N):
        for col in range(M):
            if grid[row][col] and (row, col) not in check_set:
                grid[row][col] += 1

# 가장 강한 포탑의 공격력 출력
def get_answer():
    return max([max(row) for row in grid])

# 열심히 찍자.
def custom_print():
    print(f'----attack & target----')
    print('attack:', attack_row, attack_col)
    print('target:', target_row, target_col)
    print(f'----grid status----')
    for row in grid:
        print(*row)

# 입력 & 초기 세팅
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[0] * M for _ in range(N)]
check_set = set()

# 실행부
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