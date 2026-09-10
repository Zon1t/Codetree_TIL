# 시작 5:16
# 불이 있는 위치 X, 방화벽은 정확히 3개 설치했음. itertools로 풀어볼까?

from collections import deque
from itertools import combinations

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


def bfs():
    for row, col in t:
        grid[row][col] = 1

    visited = [[False] * M for _ in range(N)]
    Q, cnt = deque(), empty_cnt-3
    for row, col in fire_lst:
        visited[row][col] = True
        Q.append((row, col))

    while Q:
        curr_row, curr_col = Q.popleft()

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if visited[next_row][next_col] or grid[next_row][next_col] != 0:
                continue
            visited[next_row][next_col] = True
            Q.append((next_row, next_col))
            cnt -= 1

    for row, col in t:
        grid[row][col] = 0

    return cnt


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

empty_lst, fire_lst = [], []
empty_cnt = 0
for row in range(N):
    for col in range(M):
        if grid[row][col] == 0:
            empty_lst.append((row, col))
            empty_cnt += 1
        if grid[row][col] == 2:
            fire_lst.append((row, col))

answer = 0
for t in combinations(empty_lst, 3):
    temp = bfs()
    if answer < temp:
        answer = temp

print(answer)