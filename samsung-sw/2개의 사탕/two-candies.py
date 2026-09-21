# 20:06 시작
# bfs로 풀어보자. 좌표 최적화해서 2차원으로 풀어볼까? 그렇게 해보자.
# 우선 기울임 적용 로직만 있으면 수월하게 해결할 수 있을 것 같다.

from collections import deque


def apply_gravity(obj, direction):
    curr_obj = obj
    while True:
        curr_obj += delta_num[direction]
        if grid[curr_obj//M][curr_obj%M] == -1:
            return curr_obj - delta_num[direction]
        if curr_obj == EXIT:
            return curr_obj


N, M = map(int, input().split())
size = N*M
grid = [[0] * M for _ in range(N)]
red, blue, EXIT = -1, -1, -1
for i in range(N):
    for j, val in enumerate(input()):
        if val == '#':
            grid[i][j] = -1
        elif val == 'R':
            red = i*M+j
        elif val == 'B':
            blue = i*M+j
        elif val == 'O':
            EXIT = i*M+j

answer = -1
delta_num = [M, 1, -M, -1]

visited = [[-1] * size for _ in range(size)]
visited[red][blue] = 0

Q = deque([(red, blue)])
while Q:
    curr_red, curr_blue = Q.popleft()
    curr_cnt = visited[curr_red][curr_blue]

    if curr_cnt > 10:
        break

    if curr_red == EXIT and curr_blue != EXIT:
        answer = curr_cnt
        break

    for d in range(4):
        next_red, next_blue = apply_gravity(curr_red, d), apply_gravity(curr_blue, d)

        if next_blue == EXIT:
            continue

        if next_red == next_blue:
            if (curr_red < curr_blue and d < 2) or (curr_red > curr_blue and d > 1):
                next_red -= delta_num[d]
            else:
                next_blue -= delta_num[d]

        if visited[next_red][next_blue] != -1:
            continue

        visited[next_red][next_blue] = curr_cnt+1
        Q.append((next_red, next_blue))

# 정답 출력
print(answer)