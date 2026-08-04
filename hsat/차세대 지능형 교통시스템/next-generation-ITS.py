# import sys; sys.stdin = open('input.txt', 'r')

from collections import deque

N, T = map(int, input().split())
signals = [[[int(x)-1 for x in input().split()] for _ in range(N)] for _ in range(N)]

# Please write your code here.

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
deltas = [[1, 0, -1], [1, 0], [0, -1]]

visited = [[[-1] * N for _ in range(N)] for _ in range(4)]

Q = deque([(0, 0, 1)])
visited[1][0][0] = 0
while Q:
    curr_row, curr_col, curr_dir = Q.popleft()
    t = visited[curr_dir][curr_row][curr_col]

    sig = signals[curr_row][curr_col][t % 4]

    if sig % 4 != curr_dir:
        continue

    for delta in deltas[sig//4]:
        next_dir = (curr_dir + delta) % 4
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
            continue
        if visited[next_dir][next_row][next_col] != -1:
            continue

        visited[next_dir][next_row][next_col] = t + 1
        Q.append((next_row, next_col, next_dir))

answer = 0
for row in range(N):
    for col in range(N):
        for k in range(4):
            if visited[k][row][col] != -1 and visited[k][row][col] <= T:
                answer += 1
                break
print(answer)