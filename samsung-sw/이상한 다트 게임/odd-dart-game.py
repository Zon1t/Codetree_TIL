# 시작 09:35
# 지워지는 수에 대해서는 0으로 처리하기. 배수 판 회전 주의.
# 인접하다의 개념은 우리가 익히 알고 있는 그 인접하다의 개념이다.
# rotate -> erase -> standard


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row):
    return 0 <= row < N


def rotate(x, d, k):
    for idx in range(x-1, N, x):
        grid[idx] = (grid[idx][k:]+grid[idx][:k] if d else grid[idx][-k:]+grid[idx][:-k])


def erase():
    flag = False
    visited = [[False] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if visited[row][col] or not grid[row][col]:
                continue

            visited[row][col] = True
            lst = [(row, col)]
            pointer, cnt = 0, 1
            while pointer < cnt:
                for d in range(4):
                    next_row, next_col = lst[pointer][0] + dr[d], (lst[pointer][1] + dc[d])%M
                    if not in_range(next_row) or visited[next_row][next_col]:
                        continue
                    if grid[lst[pointer][0]][lst[pointer][1]] != grid[next_row][next_col]:
                        continue
                    visited[next_row][next_col] = True
                    lst.append((next_row, next_col))
                    cnt += 1
                pointer += 1

            if cnt < 2:
                continue

            flag = True
            for er, ec in lst:
                grid[er][ec] = 0
    return flag


def scaling():
    total, cnt = 0, 0
    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue
            total += grid[row][col]
            cnt += 1
    average = total // cnt

    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue

            if grid[row][col] > average:
                grid[row][col] -= 1
            elif grid[row][col] < average:
                grid[row][col] += 1


def print_grid():
    print(f'----grid----')
    for row in grid:
        print(*row)


# ==========================================
# 세팅

N, M, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# ==========================================
# 실행부

for _ in range(q):
    x, d, k = map(int, input().split())
    
    # 1. 돌리기
    rotate(x, d, k%M)
    
    # 2. 지우기
    if not erase():
        scaling()

# 정답 출력
print(sum([sum(row) for row in grid]))