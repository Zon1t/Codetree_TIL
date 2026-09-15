''' 왕실의 기사 대결 / 20260915 / 체감 난이도 : 골드 1~2
소요 시간 : 77분 / 시도 : 1회 / 실행 시간 : 63ms / 메모리 : 17MB

타임 라인 : 구상(18분) - 구현(45분) - 검증(14분)


[구상]
    - 격자에 기사 그려가면서 문제를 풀면 그렇게 어렵진 않을 것 같다는 생각을 했다. 밀치는 로직이
    좀 까다롭나 생각이 들었었는데, 재귀적으로 판별하면 괜찮을 것 같다고 판단했다.
    - 당장 생각나는 함수 정도를 정의하고, 자료 구조를 고민해보았다. 클래스를 쓸까에 대해서도 고민
    해보았는데, 익숙하지 않아서 그런가 끌리진 않았다.

[구현]
    - 재귀로 문제 풀겠다고 해놓고 구상을 짧게 가져간 벌을 받아버렸다. 처음 단순하게 생각했던 함수,
    전체적인 진행 양상 등 그대로 가져간 구석이 없을 정도로 수정을 많이 해버렸다. 구현 과정에서 적
    절히 생각하면서 할 수 있을 줄 알았는데, 나를 너무 과대평가했다.
    - 가장 크게 변화한 아이디어 : 원래는 already_move 리스트를 만들어 check 이후 다시 확인해
    가며 움직이고자 하였으나, 그냥 check 과정에서 set을 받아와 애초에 이미 움직이고 자시고 하는
    문제가 없게끔 만들어 주었다.
    - 해당 과정에서 바뀌는 부분도 많고, 또 격자를 업데이트 해주어야 하는 부분도 있었기에 꽤나 많
    은 부분을 고치느라 구현 시간이 오래 걸렸다.

[검증]
    - 주어진 테케를 조금 변형해 검증을 진행해보았다. 로직만 봤을 땐 괜찮을 것 같다 생각했는데 혹
    시 몰라 재귀 로직이 올바르게 동작하는지 체크해보았다.
    - 하드코딩한 부분이 있어 혹시 오타나 복붙 과정에서 문제가 있는지 한 번 더 확인해보고, 로직을
    한 번 더 훑어보고 제출하게 되었다.


검증 단계에서 사용한 테케

1. 연쇄 작용 + 이동 불가능
4 4 3
0 0 1 2
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 3 2 1 5
1 2
2 1
3 3

2. 연쇄 작용 + 이동 가능
4 4 3
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 3 2 1 5
1 2
2 1
3 3
'''

# 초기 위치 & 높이와 너비를 적절하게 저장해야 할 듯? 다중 객체 <-> 격자와의 상호작용에 대한 문제이다.
# 단순히 봤을 땐 그렇게 안어려워 보이는데? 자료형 적절하게 선언하고, 하면 금방 풀릴 듯
# 밀치는 로직 << 얘는 좀 중요해 보이긴 한다. 벽 있는지 연쇄적으로 판별.. 재귀?하면 되나
# move -> check -> push 정도의 절차로 문제를 해결하면 될 듯? 격자 업데이트도 해야 한다.
# 기사 클래스로 쓸까? 아직 그 정도 잘쓰진 않으니 깝치지 말자.


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 명령 수행하기.
def move(idx, direction):
    if not is_alive[idx]:
        return

    # 이동 가능 여부와 같이 이동할 기사들의 index 받아오기.
    can_move, move_set = check(idx, direction)
    if not can_move:
        return

    # 정보 업데이트.
    erase(move_set|{idx})
    write(move_set, direction)

    # 현재 공격자 정보 받아오기.
    curr_row, curr_col, height, width, health = knights[idx]

    # 공격자도 업데이트 해주기.
    curr_row, curr_col = curr_row + dr[direction], curr_col + dc[direction]
    for delta_row in range(height):
        for delta_col in range(width):
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            knights_grid[next_row][next_col] = idx
    knights[idx] = (curr_row, curr_col, height, width, health)


# 이동 가능 여부, check_set까지 반환
def check(idx, direction):
    curr_row, curr_col, height, width, _ = knights[idx]
    
    check_lst = []          # 더 확인해야 할 knight_idx를 담아두기 for 연쇄 작용
    return_set = set()      # 밀 수 있는 knight_idx를 반환하기 위함.
    
    # 기세로 하드코딩이나 하자.
    if direction == 0:
        next_row = curr_row - 1
        if next_row < 0:
            return False, None

        for delta_col in range(width):
            next_col = curr_col + delta_col
            if grid[next_row][next_col] == 2:
                return False, None
            if knights_grid[next_row][next_col]:
                check_lst.append(knights_grid[next_row][next_col])

    elif direction == 1:
        next_col = curr_col + width
        if next_col >= N:
            return False, None

        for delta_row in range(height):
            next_row = curr_row + delta_row
            if grid[next_row][next_col] == 2:
                return False, None
            if knights_grid[next_row][next_col]:
                check_lst.append(knights_grid[next_row][next_col])

    elif direction == 2:
        next_row = curr_row + height
        if next_row >= N:
            return False, None

        for delta_col in range(width):
            next_col = curr_col + delta_col
            if grid[next_row][next_col] == 2:
                return False, None
            if knights_grid[next_row][next_col]:
                check_lst.append(knights_grid[next_row][next_col])

    else:
        next_col = curr_col - 1
        if next_col < 0:
            return False, None

        for delta_row in range(height):
            next_row = curr_row + delta_row
            if grid[next_row][next_col] == 2:
                return False, None
            if knights_grid[next_row][next_col]:
                check_lst.append(knights_grid[next_row][next_col])

    # 추가로 확인이 필요하면 확인하기!
    for knight_idx in check_lst:
        can_move, check_set = check(knight_idx, direction)
        if not can_move:
            return False, None
        return_set |= check_set
    
    # 적절한 값 반환
    return True, return_set|set(check_lst)


# 격자에서 지우기
def erase(move_set):
    for knight_idx in move_set:
        curr_row, curr_col, height, width, _ = knights[knight_idx]
        for delta_row in range(height):
            for delta_col in range(width):
                knights_grid[curr_row+delta_row][curr_col+delta_col] = 0


# 격자에 다시 적으며 health 업데이트
def write(move_set, direction):
    for knight_idx in move_set:
        curr_row, curr_col, height, width, health = knights[knight_idx]
        curr_row, curr_col = curr_row + dr[direction], curr_col + dc[direction]
        for delta_row in range(height):
            for delta_col in range(width):
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if grid[next_row][next_col] == 1:
                    health -= 1

        # 죽었으면 처리 후 스킵
        if health <= 0:
            is_alive[knight_idx] = False
            continue

        # 살았으면 업데이트
        for delta_row in range(height):
            for delta_col in range(width):
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                knights_grid[next_row][next_col] = knight_idx
        knights[knight_idx] = (curr_row, curr_col, height, width, health)


# 주요 확인 대상1
def print_grid():
    print(f'----knights_grid----')
    for row in knights_grid:
        print(*row)


# 주요 확인 대상2
def print_status():
    print(f'----status----')
    for i in range(1, M+1):
        print(f'idx: {i}')
        print(*knights[i])
        print(is_alive[i])


def get_answer():
    temp = 0
    for knight_idx in range(1, M+1):
        if not is_alive[knight_idx]:
            continue
        temp += hp[knight_idx] - knights[knight_idx][4]
    return temp


# 입력 받기 및 세팅
N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

knights_grid = [[0]*N for _ in range(N)]    # 밀치는지 여부 등 확인하려면 격자 그리자.
knights = [None]                            # 기사의 위치, 크기, 체력 정보를 저장
hp = [0] * (M+1)                            # 정답 연산에 필요한 초기 hp값 저장
is_alive = [True] * (M+1)                   # 살아 있는 애들에 대해서 로직 수행하기 위함.
for idx in range(1, M+1):
    r, c, h, w, k = map(int, input().split())
    knights.append((r-1, c-1, h, w, k))
    hp[idx] = k

    # 죽은 애를 입력으로 줄 수 있나?
    if not k:
        is_alive[idx] = False
        continue

    # 격자에 그려주기.
    for delta_row in range(h):
        for delta_col in range(w):
            knights_grid[r-1+delta_row][c-1+delta_col] = idx

# 실행부
for _ in range(Q):
    idx, d = map(int, input().split())
    move(idx, d)

# 정답 연산 후 출력
answer = get_answer()
print(answer)