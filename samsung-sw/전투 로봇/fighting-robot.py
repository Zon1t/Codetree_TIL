# 7:55 시작
# 대상 우선순위 (거리, 행, 열) << 잘 지켜서 bfs하면 문제 없이 통과할 것.
# 레벨업 처리 잘하기. 레벨에 따른 처리 적절하게 잘하기.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def find():
    visited = [[-1] * N for _ in range(N)]
    visited[robot_row][robot_col] = 0

    find = []
    Q = deque([(robot_row, robot_col)])
    while Q:
        for _ in range(len(Q)):
            curr_row, curr_col = Q.popleft()
            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] > level:
                    continue
                if visited[next_row][next_col] != -1:
                    continue

                if 0 < grid[next_row][next_col] < level:
                    find.append((next_row, next_col))

                visited[next_row][next_col] = visited[curr_row][curr_col] + 1
                Q.append((next_row, next_col))

        if find:
            find.sort()
            return_row, return_col = find[0]
            return return_row, return_col, visited[return_row][return_col]

    return -1, -1, -1


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


def print_status():
    print(f'----status----')
    print(robot_row, robot_col, answer)


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

robot_row, robot_col = -1, -1
for row in range(N):
    for col in range(N):
        if grid[row][col] == 9:
            robot_row, robot_col = row, col
            grid[row][col] = 0

level, cnt = 2, 0

answer = 0
while True:
    monster_row, monster_col, time = find()

    if time == -1:
        break

    answer += time
    cnt += 1
    if cnt == level:
        level += 1
        cnt = 0

    robot_row, robot_col = monster_row, monster_col
    grid[robot_row][robot_col] = 0


print(answer)