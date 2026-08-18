# 좌표에 대한 부분은 맞춰서 제시해줌. 방향 북-동-남-서 델타 세팅 맞추기.
# 이미 방문 / 인도  ->  돌리기, 없으면 후진 후 반복. 후진조차 못하면 종료
# 첫, 마지막 행과 열은 인도임을 보장. 따로 범위 벗어나는지 체크는 할 필요 없음.
# 시키는 명령만 수행하면 되므로 while문 돌리면서 수행하면 될 것으로 보인다.
# 에지라할 수 있는 케이스가 존재하는가?

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
curr_row, curr_col, curr_dir = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
visited[curr_row][curr_col] = True

while True:

    # 인접한 네 방향 탐색. 순서는 현재 방향 기준 왼쪽으로 돌면서 체크.
    for delta in range(1, 5):
        # 왼쪽으로 도니까 빼주기.
        next_dir = (curr_dir - delta) % 4
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

        # 인도거나 이미 방문한 도로인 경우 왼쪽으로 돌기
        if grid[next_row][next_col] == 1 or visited[next_row][next_col]:
            continue

        # 방문할 수 있는 도로면 방향 fix 후 break.
        curr_dir = next_dir
        break
    # for ~ else문. 만약 인접한 네 영역 모두 인도거나 이미 방문했으면 후진 시도를 해야한다.
    else:
        # 후진 로직 구성
        next_row, next_col = curr_row - dr[curr_dir], curr_col - dc[curr_dir]

        # 만약 더 후진할 수 없다면 종료. 인도인지만 체크하면 된다.
        if grid[next_row][next_col] == 1:
            break

    # 방문처리 후 이동.
    visited[next_row][next_col] = True
    curr_row, curr_col = next_row, next_col

print(sum([sum(row) for row in visited]))