n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

import sys
sys.setrecursionlimit(10000)

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