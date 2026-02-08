n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start_points = []

for _ in range(k):
    ri, ci = map(int, input().split())
    start_points.append((ri-1, ci-1))

# Please write your code here.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def select_rock_pos(start, temp_list):
    if len(temp_list) == m:
        rock_comb_list.append(temp_list[:])
        return
    for i in range(start, len(rock_pos)):
        temp_list.append(rock_pos[i])
        select_rock_pos(i+1, temp_list)
        temp_list.pop()

def count_possible_area(rock_comb, start_points):
    visited = [[False]*n for _ in range(n)]
    q = deque(start_points)
    for r, c in start_points:
        visited[r][c] = True
    s = 0

    while q:
        r, c = q.popleft()
        s += 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] == 0 or (nr, nc) in rock_comb:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return s

rock_pos = []
for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            rock_pos.append((row, col))

max_count = 0
rock_comb_list = []
select_rock_pos(0, [])
for rock_comb in rock_comb_list:
    count = count_possible_area(rock_comb, start_points)
    max_count = count if max_count < count else max_count
print(max_count)