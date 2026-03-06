import sys; MAX_VALUE = sys.maxsize; input = sys.stdin.readline
import heapq

N, A, B = map(int, input().split())
total_num = N**2
grid = [input().strip() for _ in range(N)]

distances = [[MAX_VALUE] * (total_num) for _ in range(total_num)]
for i in range(total_num):
    distances[i][i] = 0
    i_row, i_col = i//N, i%N
    i_val = grid[i_row][i_col]
    for j in range(i+1, total_num):
        j_row, j_col = j//N, j%N
        j_val = grid[j_row][j_col]
        if i_row == j_row:
            if j_col - i_col == 1:
                if i_val == j_val:
                    distances[i][j] = A
                    distances[j][i] = A
                else:
                    distances[i][j] = B
                    distances[j][i] = B
        elif i_col == j_col:
            if j_row - i_row == 1:
                if i_val == j_val:
                    distances[i][j] = A
                    distances[j][i] = A
                else:
                    distances[i][j] = B
                    distances[j][i] = B

for k in range(total_num):
    for i in range(total_num):
        for j in range(total_num):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

answer = 0
for i in range(total_num):
    for j in range(i+1, total_num):
        if answer < distances[i][j]:
            answer = distances[i][j]
print(answer)