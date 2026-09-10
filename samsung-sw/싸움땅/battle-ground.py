# 클래스로 풀어보자. 근데 이렇게 하는거 맞음?
class Player:
    def __init__(self, i, r, c, d, s, g=0):
        self.idx = i
        self.row = r
        self.col = c
        self.direction = d
        self.status = s
        self.gun = g

    # def __str__(self):
    #     return f'data:{self.get_data()}, power:{self.get_power()}'

    def get_data(self):
        return self.row, self.col, self.direction

    def get_power(self):
        return self.status + self.gun

    def update_data(self, r, c, d, update_grid=True):
        self.row = r
        self.col = c
        self.direction = d
        if update_grid:
            player_grid[r][c] = self.idx

    # 이동 로직
    def move(self):
        curr_row, curr_col, curr_dir = self.get_data()
        next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
        if not in_range(next_row, next_col):
            curr_dir = (curr_dir + 2) % 4
            next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
        player_grid[curr_row][curr_col] = -1

        # 1. 사람이 없으면 총줍기 + 격자 업데이트
        if player_grid[next_row][next_col] == -1:
            self.update_data(next_row, next_col, curr_dir)
            self.my_gun()

        # 2. 사람이 있으면?
        else:
            # 맞짱뜰 사람 잡아오기
            another_player = players[player_grid[next_row][next_col]]
            self.update_data(next_row, next_col, curr_dir, False)   # 격자 업뎃은 X

            # 뜨자
            my_power, your_power = self.get_power(), another_player.get_power()
            if my_power > your_power or (my_power == your_power and self.status > another_player.status):
                winner, loser = self, another_player
            else:
                winner, loser = another_player, self

            # 주어진 로직 수행.
            scores[winner.idx] += abs(my_power-your_power)
            loser.urloser()
            winner.update_data(*winner.get_data())
            winner.my_gun()

    # 패자가 할 일..
    def urloser(self):
        curr_row, curr_col, curr_dir = self.get_data()

        # 총 떨구고
        if self.gun:
            guns[curr_row][curr_col].append(self.gun)
            self.gun = 0

        # 도망가
        for delta_d in range(4):
            next_dir = (curr_dir + delta_d) % 4
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

            # 격자 밖 or 플레이어 있으면..
            if not in_range(next_row, next_col) or player_grid[next_row][next_col] != -1:
                continue

            # 위치가 결정됨.
            self.update_data(next_row, next_col, next_dir)
            self.my_gun()
            break

    # 총 줍자
    def my_gun(self):
        curr_row, curr_col, _ = self.get_data()

        # 총이 놓여져 있다면..
        if guns[curr_row][curr_col]:
            my_gun, max_gun = self.gun, max(guns[curr_row][curr_col])

            # 클 때만 가져가면 된다.
            if my_gun < max_gun:
                max_idx = guns[curr_row][curr_col].index(max_gun)

                # 총을 소지했으면 교체.
                if my_gun:
                    guns[curr_row][curr_col][max_idx] = my_gun
                # 아니면 들고감.
                else:
                    guns[curr_row][curr_col].pop(max_idx)

                self.gun = max_gun

# 주어진 순서에 맞게 델타 세팅
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


N, M, K = map(int, input().split())

# 총 정보 받기
guns = [[[] for _ in range(N)] for _ in range(N)]
for row in range(N):
    for col, val in enumerate(map(int, input().split())):
        if not val:
            continue
        guns[row][col].append(val)

# 플레이어 정보 받기
player_grid = [[-1] * N for _ in range(N)]
players = []
for idx in range(M):
    r, c, d, s = map(int, input().split())
    player_grid[r-1][c-1] = idx
    players.append(Player(idx, r-1, c-1, d, s))

# 실행부
scores = [0] * M
for _ in range(K):
    for idx in range(M):
        players[idx].move()

# 정답 출력
print(*scores)