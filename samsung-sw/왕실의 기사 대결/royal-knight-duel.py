# 12:51 [] /
# 연쇄 처리만 잘하면 크게 문제 될 구석이 없다.
# 이동 이전에 체크 처리 -> 이동 처리 -> 데미지 적용 이렇게 구성하면 될 것으로 보인다.

class Knight:
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    def __init__(self, i, r, c, h, w, k):
        self.idx = i
        self.row = r
        self.col = c
        self.height = h
        self.width = w
        self.origin_hp = k
        self.hp = k

    def get_diff(self):
        return self.origin_hp-self.hp if self.hp else 0

    def get_data(self):
        return self.row, self.col, self.height, self.width

    def get_setting(self, d):
        if d == 0: return self.row-1, self.col
        if d == 1: return self.row, self.col+self.width
        if d == 2: return self.row+self.height, self.col
        if d == 3: return self.row, self.col-1

    def update_grid(self, is_idx):
        start_row, start_col, height, width = self.get_data()
        fill_value = self.idx if is_idx else -1
        for row in range(start_row, start_row+height):
            for col in range(start_col, start_col+width):
                knights_grid[row][col] = fill_value

    def move(self, d, get_damage):
        self.row += self.DR[d]
        self.col += self.DC[d]

        if get_damage:
            start_row, start_col, height, width = self.get_data()
            damage = 0
            for row in range(start_row, start_row+height):
                for col in range(start_col, start_col+width):
                    if grid[row][col] == 1:
                        damage += 1
            self.hp = max(0, self.hp-damage)
            if self.hp:
                self.update_grid(True)
        else:
            self.update_grid(True)

    def check(self, d):
        start_row, start_col = self.get_setting(d)
        dr, dc = (1, 0) if d % 2 else (0, 1)

        return_set, check_set = set(), set()
        for k in range(self.height if d % 2 else self.width):
            next_row, next_col = start_row + dr*k, start_col + dc*k
            if grid[next_row][next_col] == 2:
                return None
            if knights_grid[next_row][next_col] != -1:
                check_set.add(knights_grid[next_row][next_col])

        for check_idx in check_set:
            temp = knights[check_idx].check(d)
            if temp is None:
                return None
            return_set |= temp

        return_set.add(self.idx)
        return return_set


def get_answer():
    temp = 0
    for idx in range(M):
        temp += knights[idx].get_diff()
    return temp


def print_grid():
    print('----grid----')
    for row in knights_grid:
        print(*row)


# ===============================================================
# 세팅

N, M, Q = map(int, input().split())
grid = [[2] * (N+2)] + \
       [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + \
       [[2] * (N+2)]

knights = []
knights_grid = [[-1]*(N+2) for _ in range(N+2)]
for idx in range(M):
    r, c, h, w, k = map(int, input().split())
    knights.append(Knight(idx, r, c, h, w, k))
    knights[idx].update_grid(True)

# =================================================================
# 실행부

for _ in range(Q):
    # 명령 수행하기.
    i, d = map(int, input().split())
    if not knights[i-1].hp:
        continue

    move_set = knights[i-1].check(d)
    if move_set is None:
        continue

    # 움직일 수 있으면 움직이기.
    for move_idx in move_set:
        knights[move_idx].update_grid(False)
    for move_idx in move_set:
        knights[move_idx].move(d, (move_idx != i-1))

# 정답 출력하기.
answer = get_answer()
print(answer)