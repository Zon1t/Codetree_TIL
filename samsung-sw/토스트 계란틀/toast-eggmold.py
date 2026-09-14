# 시작 5:17
# 단지 번호 붙이기 유형 문제. 적절한 조건에 따른 그루핑 + 잘 처리하자.
# 달리 생각할 부분은 없을 듯

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def bfs(sr, sc):
    visited[sr][sc] = True
    total, cnt = egg_grid[sr][sc], 1
    lst, pointer = [(sr, sc)], 0

    while pointer < cnt:
        curr_row, curr_col = lst[pointer]
        pointer += 1

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or visited[next_row][next_col]:
                continue

            if L <= abs(egg_grid[curr_row][curr_col]-egg_grid[next_row][next_col]) <= R:
                visited[next_row][next_col] = True
                lst.append((next_row, next_col))

                total += egg_grid[next_row][next_col]
                cnt += 1

    if cnt == 1:
        return False

    average = total // cnt
    for gr, gc in lst:
        egg_grid[gr][gc] = average
    return True


def print_grid():
    print(f'----{turn}----')
    for row in egg_grid:
        print(*row)
    print()


N, L, R = map(int, input().split())
egg_grid = [list(map(int, input().split())) for _ in range(N)]

turn = 0
while True:
    is_changed = False
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue

            if bfs(row, col):
                is_changed = True

    if not is_changed:
        break

    turn += 1

print(turn)