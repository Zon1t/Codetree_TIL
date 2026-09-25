# [] / 14:14 시작
# 플레이어에 대한 정보를 클래스, 총에 대한 정보는 격자로 다루면 되겠다.
# 대상 위치에 다른 플레이어가 있는지도 알아야해서 플레이어 격자도 만들어야겠다.

class Player:
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    def __init__(self, i, r, c, d, s):
        self.idx = i
        self.row = r
        self.col = c
        self.direction = d
        self.stat = s
        self.gun = 0
        self.alive = True
        self.score = 0

    def get_pos(self):
        return self.row, self.col

    def get_power(self):
        return self.gun + self.stat, self.stat

    def update_pos(self, r, c):
        self.row = r
        self.col = c

    def move(self):
        curr_row, curr_col = self.get_pos()
        next_row, next_col = curr_row + self.DR[self.direction], curr_col + self.DC[self.direction]
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
            self.direction = (self.direction + 2) % 4
            next_row, next_col = curr_row + self.DR[self.direction], curr_col + self.DC[self.direction]

        return next_row, next_col

    def drop_gun(self):
        if self.gun:
            gun_grid[self.row][self.col].append(self.gun)
            gun_grid[self.row][self.col].sort()
            self.gun = 0

    def imloser(self):
        self.drop_gun()

        for delta_dir in range(4):
            next_dir = (self.direction + delta_dir)%4
            next_row, next_col = self.row + self.DR[next_dir], self.col + self.DC[next_dir]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if player_grid[next_row][next_col] != -1:
                continue

            self.update_pos(next_row, next_col)
            self.direction = next_dir
            break

        self.get_gun()
        return self.get_pos()

    def imwinner(self, point):
        self.drop_gun()
        self.get_gun()
        self.score += point
        return self.get_pos()

    def get_gun(self):
        if gun_grid[self.row][self.col]:
            self.gun = gun_grid[self.row][self.col].pop()


def fight(player1, player2):
    power1, power2 = players[player1].get_power(), players[player2].get_power()
    diff = abs(power1[0]-power2[0])
    if power1 > power2:
        return players[player1], players[player2], diff
    else:
        return players[player2], players[player1], diff


def get_answer():
    for i in range(M):
        yield players[i].score


# =========================================================
# 세팅

N, M, K = map(int, input().split())
gun_grid = [list(map(lambda x: [int(x)], input().split())) for _ in range(N)]

player_grid = [[-1]*N for _ in range(N)]
players = []
for idx in range(M):
    r, c, d, s = map(int, input().split())
    players.append(Player(idx, r-1, c-1, d, s))
    player_grid[r-1][c-1] = idx

# =========================================================
# 실행부

for _ in range(K):
    # 1. 플레이어 움직이기.
    for pi in range(M):
        curr_row, curr_col = players[pi].get_pos()
        player_grid[curr_row][curr_col] = -1

        next_row, next_col = players[pi].move()
        players[pi].update_pos(next_row, next_col)

        if player_grid[next_row][next_col] == -1:
            players[pi].drop_gun()
            players[pi].get_gun()
            player_grid[next_row][next_col] = pi
        else:
            winner, loser, point = fight(pi, player_grid[next_row][next_col])

            lose_row, lose_col = loser.imloser()
            player_grid[lose_row][lose_col] = loser.idx

            winner_row, winner_col = winner.imwinner(point)
            player_grid[winner_row][winner_col] = winner.idx

# 정답 출력하기.
answer = get_answer()
print(*answer)