dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def dfs(curr_row, curr_col, diff, memo):
    # 이미 연산된 바 있으면 skip
    if memo[curr_row][curr_col] != -1:
        return memo[curr_row][curr_col]

    cnt = 1
    for d in range(4):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col):
            continue

        if grid[curr_row][curr_col] < grid[next_row][next_col] <= grid[curr_row][curr_col]+diff:
            can_go = dfs(next_row, next_col, diff, memo)
            if cnt < can_go+1:
                cnt = can_go+1

    memo[curr_row][curr_col] = cnt
    return memo[curr_row][curr_col]

def check(diff):
    memo = [[-1] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if memo[row][col] != -1:
                continue

            temp = dfs(row, col, diff, memo)
            if temp >= K:
                return True
    return False


N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

start, end = 1, int(1e8)
while start < end:
    mid = (start + end) >> 1
    if check(mid):
        end = mid
    else:
        start = mid + 1

print(start if start != int(1e8) else -1)