# 시키는대로 잘하기. 주의할 점이라면 초기에는 좌 하단 2*2
# 이동시키키 -> 중요. 방향도 잘 맞춰야 할듯
# 함수로 분리하면 좋을 것 같다. move -> grow -> cut

# 주어진 정보에 맞게 델타 세팅.
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1 ,-1, -1, 0, 1]

def move(d, p):
    global yeongyang

    new_yeongyang = set()
    for row, col in yeongyang:
        next_row, next_col = (row + dr[d] * p) % N, (col + dc[d] * p) % N
        new_yeongyang.add((next_row, next_col))

    yeongyang = new_yeongyang


def grow():
    # 우선 1 증가시켜야 함. 동시에 대각 처리까지 하면 꼬일 수 있음.
    for row, col in yeongyang:
        grid[row][col] += 1

    for row, col in yeongyang:
        for d in (1, 3, 5, 7):
            next_row, next_col = row + dr[d], col + dc[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if grid[next_row][next_col]:
                grid[row][col] += 1


def cut():
    global yeongyang
    new_yeongyang = set()
    for row in range(N):
        for col in range(N):
            if grid[row][col] >= 2 and (row, col) not in yeongyang:
                grid[row][col] -= 2
                new_yeongyang.add((row, col))
    yeongyang = new_yeongyang


# 안헷갈리게 Y로 받자.
N, Y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 초기 영양제 세팅
yeongyang = set([(-1, 0), (-1, 1), (-2, 0), (-2, 1)])
for _ in range(Y):
    d, p = map(int, input().split())
    move((d-1)%8, p)
    grow()
    cut()

print(sum([sum(row) for row in grid]))