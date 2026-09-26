# [] / 13:41 시작 -10
# 얘도 클래스로 풀어보면 좋을 것 같다. 상속이랑 이런거 익숙했으면 더 쉽게 했을 것 같은데..
# 그냥 진행하자.

class Gorani:
    DR = [-1, 0, 1, 0, 1, 1, -1, -1]
    DC = [0, 1, 0, -1, 1, -1, 1, -1]
    INF = float('inf')

    def __init__(self, r, c):
        self.row = r
        self.col = c

    def get_pos(self):
        return self.row, self.col

    def update_pos(self, r, c):
        self.row = r
        self.col = c

    def find_target(self):
        curr_row, curr_col = self.get_pos()
        target = (self.INF, self.INF, self.INF)
        target_idx = -1

        for santa in santa_lst:
            if santa.is_out:
                continue

            target_row, target_col = santa.get_pos()
            curr_dist = (curr_row-target_row)**2 + (curr_col-target_col)**2
            curr_status = (curr_dist, -target_row, -target_col)
            if curr_status < target:
                target = curr_status
                target_idx = santa.idx

        return target_idx

    def find_dir(self, target_idx):
        curr_row, curr_col = self.get_pos()
        target_row, target_col = santa_lst[target_idx].get_pos()
        next_dir = -1

        curr_dist = (curr_row-target_row)**2 + (curr_col-target_col)**2
        curr_max = curr_dist
        for d in range(8):
            next_row, next_col = curr_row+self.DR[d], curr_col+self.DC[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue

            next_dist = (next_row-target_row)**2 + (next_col-target_col)**2
            if curr_max <= next_dist:
                continue

            curr_max = next_dist
            next_dir = d
        return next_dir

    def move(self):
        target_idx = self.find_target()
        target = santa_lst[target_idx]
        target_row, target_col = target.get_pos()
        curr_row, curr_col = self.get_pos()

        next_dir = self.find_dir(target_idx)
        move_row, move_col = curr_row+self.DR[next_dir], curr_col+self.DC[next_dir]
        self.update_pos(move_row, move_col)
        if move_row == target_row and move_col == target_col:
            santa_grid[target_row][target_col] = -1
            target.score += C
            target.stun = turn+2
            next_row, next_col = target_row+self.DR[next_dir]*C, target_col+self.DC[next_dir]*C
            target.interaction(next_row, next_col, next_dir)
        else:
            self.update_pos(move_row, move_col)


class Santa:
    DR = [-1, 0, 1, 0, 1, 1, -1, -1]
    DC = [0, 1, 0, -1, 1, -1, 1, -1]

    def __init__(self, i, r, c):
        self.idx = i
        self.row = r
        self.col = c
        self.is_out = False
        self.stun = 0
        self.score = 0

    def get_pos(self):
        return self.row, self.col

    def can_move(self):
        return self.stun <= turn and not self.is_out

    def update_pos(self, r, c):
        self.row = r
        self.col = c
        santa_grid[r][c] = self.idx

    def get_dir(self):
        curr_row, curr_col = self.get_pos()
        target_row, target_col = gorani.get_pos()

        curr_dist = (curr_row-target_row)**2 + (curr_col-target_col)**2
        curr_max = curr_dist
        next_dir = -1
        for d in range(4):
            next_row, next_col = curr_row+self.DR[d], curr_col+self.DC[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if santa_grid[next_row][next_col] != -1:
                continue

            next_dist = (next_row-target_row)**2 + (next_col-target_col)**2
            if curr_max <= next_dist:
                continue
            curr_max = next_dist
            next_dir = d
        return next_dir

    def move(self):
        curr_row, curr_col = self.get_pos()
        target_row, target_col = gorani.get_pos()
        next_dir = self.get_dir()

        if next_dir == -1:
            return

        santa_grid[curr_row][curr_col] = -1
        move_row, move_col = curr_row+self.DR[next_dir], curr_col+self.DC[next_dir]
        if move_row == target_row and move_col == target_col:
            self.score += D
            self.stun = turn+2
            next_row, next_col = move_row-self.DR[next_dir]*D, move_col-self.DC[next_dir]*D
            self.interaction(next_row, next_col, (next_dir+2) % 4)
        else:
            self.update_pos(move_row, move_col)

    def interaction(self, row, col, d):
        if row < 0 or row >= N or col < 0 or col >= N:
            self.is_out = True
            return

        that_santa = santa_grid[row][col]
        self.update_pos(row, col)

        if that_santa != -1:
            next_row, next_col = row+self.DR[d], col+self.DC[d]
            santa_lst[that_santa].interaction(next_row, next_col, d)


def get_answer():
    for santa in santa_lst:
        yield santa.score


def print_status():
    print('gorani')
    print(*gorani.get_pos())
    print('santa')
    for row in santa_grid:
        print(*row)


# =====================================================
# 세팅

scaling = lambda x: int(x)-1
N, M, K, C, D = map(int, input().split())
gorani_row, gorani_col = map(scaling, input().split())
gorani = Gorani(gorani_row, gorani_col)

santa_lst = [None] * K
santa_grid = [[-1]*N for _ in range(N)]
for _ in range(K):
    num, row, col = map(scaling, input().split())
    santa_lst[num] = Santa(num, row, col)
    santa_grid[row][col] = num

# ======================================================
# 실행부

for turn in range(1, M+1):
    # 1. 고라니 움직이기.
    gorani.move()

    # 2. 산타 움직이기.
    for santa in santa_lst:
        if santa.can_move():
            santa.move()

    # 3. 점수 업데이트
    keep_going = False
    for santa in santa_lst:
        if santa.is_out:
            continue

        santa.score += 1
        keep_going = True

    if not keep_going:
        break

# 정답 출력하기.
print(*get_answer())