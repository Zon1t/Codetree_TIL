# 인접한 방향의 칸 수를 잘 세어야겠다. 더불어 확산되는 양을 적절하게 잘 줄일 필요가 있을 것이다.
# 주의할 점! 확산이 끝난 뒤에 다음 칸에 반영이 된다. 이는 새로운 배열을 만들고 다 연산한 이후 추가하자.
# 구현해야 할 함수. simulate, rotate

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def simulate():
    temp_grid = [[0] * M for _ in range(N)]

    # 확산
    for row in range(N):
        for col in range(M):
            # 돌풍이 있는 곳은 확산이 안 일어남.
            if (row == sr and col == 0) or (row == sr+1 and col == 0):
                continue

            temp = grid[row][col] // 5
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]

                if not in_range(next_row, next_col):
                    continue
                if grid[next_row][next_col] == -1:
                    continue

                grid[row][col] -= temp
                temp_grid[next_row][next_col] += temp

    # 반영
    for row in range(N):
        for col in range(M):
            grid[row][col] += temp_grid[row][col]


def rotate():
    # 윗 직사각형 왼쪽 변
    for row in range(sr-1, 0, -1):
        grid[row][0] = grid[row-1][0]
    # 윗 직사각형 윗쪽 변
    for col in range(M-1):
        grid[0][col] = grid[0][col+1]
    # 윗 직사각형 오른쪽 변
    for row in range(sr):
        grid[row][-1] = grid[row+1][-1]
    # 윗 직사각형 아랫쪽 변
    for col in range(M-1, 1, -1):
        grid[sr][col] = grid[sr][col-1]
    grid[sr][1] = 0

    # 아랫 직사각형 왼쪽 변
    for row in range(sr+2, N-1):
        grid[row][0] = grid[row+1][0]
    # 아랫 직사각형 아랫쪽 변
    for col in range(M-1):
        grid[-1][col] = grid[-1][col+1]
    # 아랫 직사각형 오른쪽 변
    for row in range(N-1, sr+1, -1):
        grid[row][-1] = grid[row-1][-1]
    # 아랫 직사각형 윗쪽 변
    for col in range(M-1, 1, -1):
        grid[sr+1][col] = grid[sr+1][col-1]
    grid[sr+1][1] = 0


def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


N, M, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

sr = -1
for row in range(N):
    if grid[row][0] == -1:
        sr = row
        break

for _ in range(t):
    simulate()
    rotate()

print(sum([sum(row) for row in grid]) + 2)