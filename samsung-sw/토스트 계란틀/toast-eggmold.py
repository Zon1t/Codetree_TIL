# 전형적인 bfs 사용하는 시뮬레이션 문제인 것 같다.
# 매 회차마다 방문 배열 세팅해두고, 순회하며 미방문인 곳을 시뮬레이션 돌리면 될 것 같다.
# 현재 위치에 대한 계란 양을 기준으로 뻗어나가는 것이 중요할 것으로 보인다.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    global changed

    # 계란물의 평균을 계산하기 위함.
    total = arr[sr][sc]
    cnt = 1

    # 평균을 적용하기 위함.
    will_changed = set()
    will_changed.add((sr, sc))

    Q = deque([(sr, sc)])
    while Q:
        curr_row, curr_col = Q.popleft()

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 만약 범위에서 벗어나면 스킵
            if not in_range(next_row, next_col):
                continue
            # 만약 이미 방문했으면 스킵
            if visited[next_row][next_col]:
                continue

            # 범위 안에 들어온다면 같이 합칠 계란으로 포함시키기.
            if L <= abs(arr[next_row][next_col] - arr[curr_row][curr_col]) <= R:
                visited[next_row][next_col] = True
                Q.append((next_row, next_col))

                total += arr[next_row][next_col]
                cnt += 1

                will_changed.add((next_row, next_col))

    # 만약 다른 계란과 합쳐지게 된다면
    if cnt > 1:
        average = total // cnt          # 소숫점은 버리므로..
        for row, col in will_changed:
            arr[row][col] = average

        changed = True


def in_range(row, col):
    return (0 <= row < N and 0 <= col < N)


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chage_cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]

    changed = False
    for row in range(N):
        for col in range(N):
            if not visited[row][col]:
                visited[row][col] = True
                bfs(row, col)

    if not changed:
        break

    # 바뀌었으면 += 1
    chage_cnt += 1

print(chage_cnt)