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

def update(row, col):
    if answer[row][col]:
        return answer[row][col]
    temp = 1
    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        if in_range(nr, nc) and grid[row][col] < grid[nr][nc]:
            temp = max(temp, update(nr, nc) + 1)
    answer[row][col] = temp
    return temp

answer = [[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        update(row, col)
print(max([max(row) for row in answer]))