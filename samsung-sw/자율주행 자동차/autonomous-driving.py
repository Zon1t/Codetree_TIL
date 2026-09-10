# 좌회전 해가며 다음 이동 방향 탐색. 정면 시작 아님!
# 만약 발견 못했다? 현재 방향 유지하고 후진
# 후진조차 못한다? 종료

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 확인할 방향
delta_dict = {0: [3, 2, 1, 0],
              1: [0, 3, 2, 1],
              2: [1, 0, 3, 2],
              3: [2, 1, 0, 3]}


N, M = map(int, input().split())
curr_row, curr_col, curr_dir = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

while True:
    visited[curr_row][curr_col] = 1
    # 1. 이동.
    for next_dir in delta_dict[curr_dir]:
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
        if grid[next_row][next_col] or visited[next_row][next_col]:
            continue
        curr_row, curr_col, curr_dir = next_row, next_col, next_dir
        break
    # 2. 이동을 못했을 경우.
    else:
        curr_row, curr_col = curr_row - dr[curr_dir], curr_col - dc[curr_dir]
        if grid[curr_row][curr_col]:
            break

# 정답 출력
print(sum([sum(row) for row in visited]))