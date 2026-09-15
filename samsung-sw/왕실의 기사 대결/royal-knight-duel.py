class Knight:
    DELTA_R = [-1, 0, 1, 0]
    DELTA_C = [0, 1, 0, -1]

    def __init__(self, i, r, c, h, w, k):
        self.idx = i
        self.row = r
        self.col = c
        self.height = h
        self.width = w
        self.hp = k
        self.origin_hp = k

    # 위치 업데이트
    def update_pos(self, row, col):
        self.row = row
        self.col = col

    # 정답 연산을 위해 정의
    def get_diff(self):
        return self.origin_hp - self.hp if self.hp > 0 else 0

    # hp 받아오기.
    def get_hp(self):
        return self.hp

    # check 세팅을 얻기 위함.
    def get_setting(self, d):
        start_row = self.row-1 if d == 0 else self.row+self.height if d == 2 else self.row
        start_col = self.col-1 if d == 3 else self.col+self.width if d == 1 else self.col
        return start_row, start_col

    # 이동 가능한지 체크하기.
    def check(self, d):
        # 초기 세팅 가져오기.
        curr_row, curr_col = self.get_setting(d)

        # 순회하며 집합 채워나가기.
        return_set, check_set, flag = {self.idx}, set(), d%2+1
        for cnt in range(self.width if flag==1 else self.height):
            next_row, next_col = curr_row + self.DELTA_R[flag] * cnt, curr_col + self.DELTA_C[flag] * cnt
            if grid[next_row][next_col] == 2:
                return False, None
            if knight_grid[next_row][next_col]:
                check_set.add(knight_grid[next_row][next_col])

        # 이동 가능한 애들 담기.
        for next_idx in check_set:
            keep_going, move_set = knights[next_idx].check(d)
            if not keep_going:
                return False, None
            return_set |= move_set

        return True, return_set

    # 지우기.
    def erase(self):
        for delta_row in range(self.height):
            for delta_col in range(self.width):
                knight_grid[self.row + delta_row][self.col + delta_col] = 0

    # 움직이기.
    def move(self, d):
        curr_row, curr_col = self.row + self.DELTA_R[d], self.col + self.DELTA_C[d]
        self.update_pos(curr_row, curr_col)

        # 격자 업데이트 + 데미지 적용
        for delta_row in range(self.height):
            for delta_col in range(self.width):
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                knight_grid[next_row][next_col] = self.idx

                # 데미지 처리
                if self.idx != attack_idx and grid[next_row][next_col] == 1:
                    self.hp -= 1

        # 죽으면 처리
        if self.hp <= 0:
            self.erase()


# 정답 연산하기.
def get_answer():
    answer = 0
    for idx in range(1, M+1):
        answer += knights[idx].get_diff()
    return answer

# custom 함수 정의
def custom_print():
    print(f'----knight_grid----')
    for row in knight_grid:
        print(*row)

# 입력 받기
N, M, Q = map(int, input().split())
grid = [[2]*(N+2)] + \
    [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + \
    [[2]*(N+2)]

# 세팅
knight_grid = [[0] * (N+2) for _ in range(N+2)]
knights = [None]
for idx in range(1, M+1):
    r, c, h, w, k = map(int, input().split())
    for row in range(r, r+h):
        for col in range(c, c+w):
            knight_grid[row][col] = idx
    knights.append(Knight(idx, r, c, h, w, k))

# 실행부
for _ in range(Q):
    attack_idx, direction = map(int, input().split())

    # 이미 죽은 기사면 continue
    if knights[attack_idx].get_hp() <= 0:
        continue

    # 움직일 수 있다면 이동시키기.
    can_move, move_set = knights[attack_idx].check(direction)
    if can_move:
        for knight_idx in move_set:
            knights[knight_idx].erase()
        for knight_idx in move_set:             
            knights[knight_idx].move(direction)

# 정답 출력
answer = get_answer()
print(answer)
