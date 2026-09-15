# 초기 위치 & 높이와 너비를 적절하게 저장해야 할 듯? 다중 객체 <-> 격자와의 상호작용에 대한 문제이다.
# 단순히 봤을 땐 그렇게 안어려워 보이는데? 자료형 적절하게 선언하고, 하면 금방 풀릴 듯
# 밀치는 로직 << 얘는 좀 중요해 보이긴 한다. 벽 있는지 연쇄적으로 판별.. 재귀?하면 되나
# move -> check -> push 정도의 절차로 문제를 해결하면 될 듯? 격자 업데이트도 해야 한다.
# 기사 클래스로 쓸까? 아직 그 정도 잘쓰진 않으니 깝치지 말자.


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(idx, direction):
    if not is_alive[idx]:
        return

    can_move, move_set = check(idx, direction)
    if not can_move:
        return False

    curr_row, curr_col, height, width, health = knights[idx]

    # 정보 업데이트.
    erase(move_set|{idx})
    write(move_set, direction)

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

    check_lst = []
    return_set = set()
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

    for knight_idx in check_lst:
        can_move, check_set = check(knight_idx, direction)
        if not can_move:
            return False, None
        return_set |= check_set
    return True, return_set|set(check_lst)


def erase(move_set):
    for knight_idx in move_set:
        curr_row, curr_col, height, width, _ = knights[knight_idx]
        for delta_row in range(height):
            for delta_col in range(width):
                knights_grid[curr_row+delta_row][curr_col+delta_col] = 0


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


def print_grid():
    print(f'----knights_grid----')
    for row in knights_grid:
        print(*row)


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


N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
knights_grid = [[0]*N for _ in range(N)]

knights = [None]
hp = [0] * (M+1)
is_alive = [True] * (M+1)
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

for _ in range(Q):
    idx, d = map(int, input().split())
    move(idx, d)

answer = get_answer()
print(answer)