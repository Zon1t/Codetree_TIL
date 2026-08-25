# 백트래킹 풀이

def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 돌아가는 방향에 대한 부분
# deltas[idx] : idx번호의 기물이 컨트롤 하는 상대방향
deltas = [None, [0], [-1, 1], [0, 1], [-1, 0, 1], [-1, 0, 1, 2]]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

ours, cnt, empty = [], 0, 0
fives = []
for row in range(N):
    for col in range(M):
        if 1 <= grid[row][col] <= 4:
            ours.append((row, col))
            cnt += 1
        elif grid[row][col] == 5:
            fives.append((row, col))
        elif grid[row][col] == 0:
            empty += 1

visited = [[0] * M for _ in range(N)]

# 5인 애들은 짜피 방향 세팅이 필요 없음.
for row, col in fives:
    for d in range(4):
        next_row, next_col = row, col
        while True:
            next_row += dr[d]
            next_col += dc[d]

            if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                break

            if grid[next_row][next_col] == 0:
                visited[next_row][next_col] += 1
                if visited[next_row][next_col] == 1:
                    empty -= 1

def backtrack(idx, empty):
    global answer

    if idx == cnt:
        if empty < answer:
            answer = empty
        return

    curr_row, curr_col = ours[idx]
    curr_num = grid[curr_row][curr_col]

    for d in range(2 if curr_num == 2 else 4):
        next_empty = empty
        for delta_dir in deltas[curr_num]:
            next_dir = (d + delta_dir) % 4
            next_row, next_col = curr_row, curr_col
            while True:
                next_row += dr[next_dir]
                next_col += dc[next_dir]

                if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                    break

                if grid[next_row][next_col] == 0:
                    visited[next_row][next_col] += 1
                    if visited[next_row][next_col] == 1:
                        next_empty -= 1

        backtrack(idx+1, next_empty)

        for delta_dir in deltas[curr_num]:
            next_dir = (d + delta_dir) % 4
            next_row, next_col = curr_row, curr_col
            while True:
                next_row += dr[next_dir]
                next_col += dc[next_dir]

                if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                    break

                if grid[next_row][next_col] == 0:
                    visited[next_row][next_col] -= 1


answer = empty
backtrack(0, empty)
print(answer)