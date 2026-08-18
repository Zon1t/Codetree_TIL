# 실험 코드

# 방화벽은 영역에 포함되지 않음.
# 빈칸의 수도 3이상, n, m도 그닥 크지 않아서 완탐하면 될 것 같다.
# 정확히 3개를 설치한다고 하니, 그보다 적게 설치하는 경우에 대해서는 생각 X
# 64C3 -> 약 36000, 8*8 size bfs 진행해도 시간초과? 안 날듯;
# 난다 해도 달리 방법이 없어 보이긴 한다


# select -> bfs -> count -> update 순으로 진행해보자.
# 에지 케이스가 있을까? 없는듯?

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs():
    # 초기 세팅
    visited = [[False] * M for _ in range(N)]
    Q = deque()
    for row, col in fire_lst:
        visited[row][col] = True
        Q.append((row, col))

    # 불이 나올 때마다 -= 1 해줄 것이므로 초기 불 개수만큼 추가. 더불어 3개는 설치했으니 -3 해주기
    now = empty

    while Q:
        curr_row, curr_col = Q.popleft()
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 범위에서 벗어나면 패스
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            # 이미 불이 번졌거나 방화벽이 있으면 패스
            if visited[next_row][next_col] or grid[next_row][next_col] == 1:
                continue

            # 방문처리 및 큐에 추가
            visited[next_row][next_col] = True
            now -= 1
            Q.append((next_row, next_col))

    # 안전 영역의 수를 반환
    return now


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

fire_lst, can_put = [], []
empty = -3
for row in range(N):
    for col in range(M):
        if grid[row][col] == 2:
            fire_lst.append((row, col))
        elif grid[row][col] == 0:
            can_put.append((row, col))
            empty += 1

cnt = len(can_put)
fire_cnt = len(fire_lst)

answer = 0
# select
for i in range(cnt-2):
    # 방화벽 설치와 제거를 잘해야 한다.
    grid[can_put[i][0]][can_put[i][1]] = 1

    for j in range(i+1, cnt-1):
        grid[can_put[j][0]][can_put[j][1]] = 1

        for k in range(j+1, cnt):
            grid[can_put[k][0]][can_put[k][1]] = 1

            # bfs
            temp = bfs()
            # update
            if temp > answer:
                answer = temp

            grid[can_put[k][0]][can_put[k][1]] = 0

        grid[can_put[j][0]][can_put[j][1]] = 0

    grid[can_put[i][0]][can_put[i][1]] = 0

print(answer)