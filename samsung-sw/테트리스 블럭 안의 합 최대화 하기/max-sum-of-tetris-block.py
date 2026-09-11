# 시작 5:05
# 아는 것이 저주.. 풀이 방법이 너무 기억에 남는다. 저번에 완탐했었는데
# 이번엔 백트래킹으로 ㄱㄱ

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


def backtrack(cnt, acc, lst):
    global answer
    if cnt == 4:
        if answer < acc:
            answer = acc
        return

    for curr_row, curr_col in lst:
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or visit[next_row][next_col]:
                continue

            visit[next_row][next_col] = 1
            backtrack(cnt+1, acc+grid[next_row][next_col], lst+[(next_row, next_col)])
            visit[next_row][next_col] = 0


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

answer = 0
for row in range(N):
    for col in range(M):
        visit[row][col] = 1
        backtrack(1, grid[row][col], [(row, col)])

print(answer)