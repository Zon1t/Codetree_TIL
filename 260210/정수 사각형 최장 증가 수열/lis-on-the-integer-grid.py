n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 각 row, col 에 대해서 모두 dfs쓰기 -> 시간초과가 나지 않을까?
# 각 row, col 에 대해서 자신보다 작은 요소가 존재하면 +1
# 적당한 조건 하에 업데이트 지속
# 우선 업데이트를 한다. -> 업데이트가 된 애들을 기준으로 우선탐색 돌리기..?

# is_update = True

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# answer_matric = [[1]*n for _ in range(n)]

# while is_update:
#     is_update = False
#     for row in range(n):
#         for col in range(n):
#             for i in range(4):
#                 nr, nc = row + dr[i] , col + dc[i]
#                 if 0 <= nr < n and 0 <= nc < n:
#                     if grid[row][col] > grid[nr][nc] and answer_matric[row][col] <= answer_matric[nr][nc]:
#                         answer_matric[row][col] = answer_matric[nr][nc] + 1
#                         is_update = True
# print(max([max(row) for row in answer_matric]))

# ----------------------------------------------------------------------

# from collections import deque

# def in_range(row, col):
#     return (0 <= row < n and 0 <= col < n)

# start_set = set()

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# answer_matric = [[1]*n for _ in range(n)]

# for row in range(n):
#     for col in range(n):
#         for i in range(4):
#             nr, nc = row + dr[i] , col + dc[i]
#             if in_range(nr, nc):
#                 if grid[row][col] > grid[nr][nc] and answer_matric[row][col] <= answer_matric[nr][nc]:
#                     answer_matric[row][col] = answer_matric[nr][nc] + 1
#                     start_set.add((row, col))

# q = deque(list(start_set))
# while q:
#     r, c = q.popleft()
#     for i in range(4):
#         nr, nc = r+dr[i], c+dc[i]
#         if in_range(nr, nc) and grid[nr][nc] > grid[r][c] and answer_matric[r][c] >= answer_matric[nr][nc]:
#             answer_matric[nr][nc] = answer_matric[r][c] + 1
#             q.append((nr, nc))

# print(max([max(row) for row in answer_matric]))

# -------------------------------------------------------------------------------

# dp로 풀기*??

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return (0 <= row < n and 0 <= col < n)

def update(row, col, start):
    q = deque([(row, col, start)])
    while q:
        r, c, d = q.popleft()
        answer[r][c] = d
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if in_range(nr, nc) and grid[r][c] < grid[nr][nc]:
                if answer[nr][nc] == 0:
                    answer[nr][nc] = d+1
                    q.append((nr, nc, d+1))
                else:
                    if answer[r][c] >= answer[nr][nc]:
                        update(nr, nc, d+1)

answer = [[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if answer[row][col] == 0:
            update(row, col, 1)
print(max([max(row) for row in answer]))