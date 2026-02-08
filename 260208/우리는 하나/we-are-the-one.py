n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

combination_cities = []
def select_cities(start, temp_list):
    if len(temp_list) == k:
        combination_cities.append(temp_list[:])
        return
    for i in range(start, n**2):
        temp_list.append((i//n, i%n))
        select_cities(i+1, temp_list)
        temp_list.pop()

select_cities(0, [])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

max_count = 0
for cities_list in combination_cities:
    visited = [[False]*n for _ in range(n)]
    count = 0
    for r, c in cities_list:
        visited[r][c] = True
    q = deque(cities_list)
    while q:
        r, c = q.popleft()
        count += 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if u <= abs(grid[r][c] - grid[nr][nc]) <= d:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    max_count = count if max_count < count else max_count
print(max_count)