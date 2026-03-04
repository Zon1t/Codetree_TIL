from itertools import combinations
from collections import deque

N, K, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
start_points = []
for _ in range(K):
    row, col = map(int, input().split())
    start_points.append((row-1, col-1))

stones = []
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            stones.append((row, col))

max_count = 0

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return (0 <= row < N and 0 <= col < N)

def count_area():
    global start_points
    count = 0
    visited = [[False]*N for _ in range(N)]
    for row, col in start_points:
        visited[row][col] = True
    q = deque(start_points[:])
    while q:
        row, col = q.popleft()
        count += 1
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]
            if not in_range(nr, nc):
                continue
            if visited[nr][nc] or grid[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    return count

def backtrack(cnt, start):
    global max_count, length
    if cnt == M:
        max_count = max(max_count, count_area())
        return
    for i in range(start, length):
        row, col = stones[i]
        grid[row][col] = 0
        backtrack(cnt+1, i+1)
        grid[row][col] = 1

length = len(stones)
backtrack(0, 0)
print(max_count)

# def in_range(row, col):
#     return (0 <= row < N and 0 <= col < N)

# for stone_comb in combinations(stones, M):
#     count = 0
#     visited = [[False]*N for _ in range(N)]
#     for row, col in start_points:
#         visited[row][col] = True
#     q = deque(start_points)
#     while q:
#         row, col = q.popleft()
#         count += 1
#         for i in range(4):
#             nr, nc = row+dr[i], col+dc[i]
#             if not in_range(nr, nc):
#                 continue
#             if visited[nr][nc]:
#                 continue
#             if grid[nr][nc] == 0 or (nr, nc) in stone_comb:
#                 visited[nr][nc] = True
#                 q.append((nr, nc))
#     max_count = max(max_count, count)

# print(max_count)