# 10:50시작    /[
# 열 순차 탐색. 빨리 발견한 곰팡이를 채취한다. 물론 못 할 수도 있음
# 곰팡이 이동 로직 잘 설계하기. 주기 : 2N - 2. 속력까지 고려하기
# 같은 칸에 있으면 잡아먹기. 크기는 모두 다름.
# 채취한 곰팡이의 총합을 구하는 문제. 채취할 떄마다 업뎃. 다음 칸 곰팡이는 미리 담아두는 방식 채용


class Gompang:

    DELTA_R = [-1, 1, 0, 0]
    DELTA_C = [0, 0, 1, -1]

    def __init__(self, i, r, c, s, d, b):
        self.idx = i
        self.row = r
        self.col = c
        self.speed = s
        self.direction = d
        self.size = b
        self.alive = True

    def update(self, r, c):
        target_idx = grid[r][c]

        if target_idx == -1 or pang_lst[target_idx].size < self.size:
            self.row = r
            self.col = c
            if target_idx != -1:
                pang_lst[target_idx].alive = False
            grid[r][c] = self.idx
            return r, c
        else:
            self.alive = False
            return None, None

    def move(self):
        next_row = (self.row + self.DELTA_R[self.direction] * self.speed) % sero
        next_col = (self.col + self.DELTA_C[self.direction] * self.speed) % garo

        if next_row >= N:
            next_row = sero - next_row
            self.direction ^= 1
        if next_col >= M:
            next_col = garo - next_col
            self.direction ^= 1

        return self.update(next_row, next_col)


def print_grid(grid):
    print(f'----pang_grid----')
    for row in grid:
        print(*row)


# =====================================================
# 세팅

N, M, K = map(int, input().split())
pang_gird = [[-1] * M for _ in range(N)]
next_target = None
garo, sero = 2*M-2, 2*N-2
pang_lst = []
for idx in range(K):
    r, c, s, d, b = map(int, input().split())
    pang_gird[r-1][c-1] = idx
    pang_lst.append(Gompang(idx, r-1, c-1, s, d-1, b))
    if c == 1 and (next_target is None or (r-1, idx) < next_target):
        next_target = (r-1, idx)

answer = 0

# =====================================================
# 실행부

for col in range(M):
    if next_target is not None:
        _, target_idx = next_target
        answer += pang_lst[target_idx].size
        pang_lst[target_idx].alive = False
        next_target = None

    grid = [[-1] * M for _ in range(N)]
    for pang in pang_lst:
        if not pang.alive:
            continue

        pr, pc = pang.move()
        if pr is None:
            continue

        if pc == col+1 and (next_target is None or pr <= next_target[0]):
            next_target = (pr, pang.idx)

    pang_gird = grid

# 정답 출력
print(answer)
