# 자신의 레벨보다 큼 - 지나 가지도 못함.
# 같음 - 지나 갈 수는 있음
# 작음 - 잡으러 감.
# 세 가지 경우에 대해서 잘 나누어 bfs를 진행하면 되겠다. bfs를 되게 많이 수행해야 할 듯?

# 1. 격자를 탐색해 가장 가까운 잡을 수 있는 몬스터를 append한다. - 없으면 시뮬레이션 종료
# 2. 몬스터 중 우선 순위에 맞게 잡으러 이동한다.
# 3. 위 과정을 반복한다.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 범위 내부에 있는지 반환하는 함수
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# bfs로 가장 가까운 잡을 수 있는 몬스터를 반환하는 함수.
def find_monster(sr, sc):
    Q = deque([(sr, sc)])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    now_time = 0
    monsters = []
    while Q:
        curr_row, curr_col = Q.popleft()

        # 종료 여부 판단.
        if now_time != visited[curr_row][curr_col]:
            # 만약 몬스터를 발견한 상태라면 정렬 후 반환
            if monsters:
                monsters.sort()
                return monsters[0][0], monsters[0][1], now_time
            # 그게 아니라면 시간대 업데이트
            now_time = visited[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or visited[next_row][next_col]:
                continue
            if grid[next_row][next_col] > level:
                continue

            # 발견시 monsters에 append
            if 0 < grid[next_row][next_col] < level:
                monsters.append((next_row,next_col))

            Q.append((next_row, next_col))
            visited[next_row][next_col] = visited[curr_row][curr_col] + 1

    # 못 찾는 경우
    return -1, -1, -1


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(N):
        if grid[row][col] == 9:
            curr_row, curr_col = row, col
            grid[curr_row][curr_col] = 0

level, kill_score, time = 2, 0, 0
while True:
    row, col, delta = find_monster(curr_row, curr_col)

    # 만약 다음 잡을 수 있는 몬스터가 없다면 종료
    if row == -1:
        print(time)
        break

    # 정보 업데이트
    curr_row, curr_col, time, kill_score = row, col, time+delta, kill_score+1
    grid[curr_row][curr_col] = 0
    if kill_score == level:
        level, kill_score = level+1, 0