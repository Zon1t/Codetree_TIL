n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def find_next(R, C, val):
    visited = [[False] * n for _ in range(n)]
    visited[R][C] = True
    temp_list = []
    q = deque([(R, C)])
    while q:
        R, C = q.popleft()
        for i in range(4):
            nr, nc = R + dr[i], C + dc[i]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] < val and not visited[nr][nc]:
                q.append((nr, nc))
                temp_list.append([grid[nr][nc], nr, nc])
                visited[nr][nc] = True
    print(temp_list)
    if temp_list:
        temp_list.sort(reverse = True)
        max_value = temp_list[0][0]
        max_idx = temp_list[0][1:]
        for temp_val, temp_r, temp_c in temp_list:
            if temp_val == max_value:
                max_idx = min(max_idx, [temp_r, temp_c])
            else:
                break
        return (max_idx[0], max_idx[1], max_value)

    else:
        return (R, C, val)


sample_answer = (r-1, c-1, grid[r-1][c-1])
for _ in range(k):
    sample_answer = find_next(sample_answer)
print(sample_answer[0], sample_answer[1])