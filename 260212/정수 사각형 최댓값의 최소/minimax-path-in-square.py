n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer_matrix = [[0]*n for _ in range(n)]
answer_matrix[0][0] = grid[0][0]

for i in range(1, n):
    answer_matrix[0][i] = max(answer_matrix[0][i-1], grid[0][i])
    answer_matrix[i][0] = max(answer_matrix[i-1][0], grid[i][0])

for row in range(1, n):
    for col in range(1, n):
        answer_matrix[row][col] = max(min(answer_matrix[row-1][col], answer_matrix[row][col-1]), grid[row][col])
print(answer_matrix[-1][-1])