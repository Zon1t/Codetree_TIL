N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

from collections import deque

q = deque([(0, 0)])
is_find = 0
while q:
    row, col = q.pop()
    if (row, col) == (N-1, M-1):
        is_find = 1
        break
    if 0 <= row+1 < N and grid[row+1][col]:
        q.append((row+1, col))
    if 0 <= col+1 < M and grid[row][col+1]:
        q.append((row, col+1))
print(is_find)