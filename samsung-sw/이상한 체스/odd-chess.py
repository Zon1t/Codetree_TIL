# 시작 11:30 종료
# 기물에 따른 적절한 델타 세팅. 가짓 수 줄일 수 있는건 줄여볼까?
# 5일 때는 미리 연산해두기. 2는 절반만.
# 순회해서 백트래킹으로 해보자.

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
deltas = [None, [(0,), (1,), (2,), (3,)], [(0, 2), (1, 3)], [(0, 1), (1, 2), (2, 3), (3, 0)],\
          [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < M


def check():
    temp = 0
    for row in range(N):
        for col in range(M):
            if not grid[row][col] and not visited[row][col]:
                temp += 1
    return temp


def backtrack(idx):
    global answer
    if idx == total_mal:
        temp = check()
        if temp < answer:
            answer = temp
        return

    curr_row, curr_col = mal[idx]
    mal_type = grid[curr_row][curr_col]
    for comb_dir in deltas[mal_type]:
        for d in comb_dir:
            next_row, next_col = curr_row, curr_col
            while True:
                next_row, next_col = next_row + dr[d], next_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                    break
                visited[next_row][next_col] += 1

        backtrack(idx+1)

        for d in comb_dir:
            next_row, next_col = curr_row, curr_col
            while True:
                next_row, next_col = next_row + dr[d], next_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                    break
                visited[next_row][next_col] -= 1

# ========================================
# 입력받기
# ========================================

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

lst_5, mal = [], []
for row in range(N):
    for col in range(M):
        if grid[row][col] == 5:
            lst_5.append((row, col))
        elif 1 <= grid[row][col] <= 4:
            mal.append((row, col))
total_mal = len(mal)

# 5는 미리 처리
visited = [[0] * M for _ in range(N)]
for row, col in lst_5:
    for d in range(4):
        next_row, next_col = row, col
        while True:
            next_row, next_col = next_row + dr[d], next_col + dc[d]
            if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                break
            visited[next_row][next_col] += 1

# ===============================
# 실행부
# ===============================

answer = N*M
backtrack(0)
print(answer)