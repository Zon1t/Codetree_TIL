# 4:43 시작
# 1. 특수 영양제 이동시키기.
# 2. 특수 영양제 투입.
# 3. 인접한 곳으로부터 높이 성장
# 4. 영양제를 투여한 곳 제외, 높이가 2 이상이라면 잘라내고 특수 영양제 올려두기.


dr = [None, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [None, 1, 1, 0, -1, -1, -1, 0, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(direction, cnt):
    return [((pos[0]+dr[direction]*cnt)%N, (pos[1]+dc[direction]*cnt)%N) for pos in yeongyang]


def grow():
    for row, col in yeongyang:
        grid[row][col] += 1

    for row, col in yeongyang:
        for d in (2, 4, 6, 8):
            next_row, next_col = row + dr[d], col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if grid[next_row][next_col]:
                grid[row][col] += 1


def cut():
    new_yeongyang = []
    for row in range(N):
        for col in range(N):
            if grid[row][col] >= 2 and (row, col) not in yeongyang:
                grid[row][col] -= 2
                new_yeongyang.append((row, col))
    return new_yeongyang


def custom_print():
    print(f'----grid----')
    for row in grid:
        print(*row)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

yeongyang = [(-2, 0), (-2, 1),
             (-1, 0), (-1, 1)]
for direction, cnt in commands:
    # 1. 움직이기.
    yeongyang = move(direction, cnt)

    # 2. 성장시키기.
    grow()

    # 3. 자르기.
    yeongyang = cut()

# 정답 출력
print(sum([sum(row) for row in grid]))