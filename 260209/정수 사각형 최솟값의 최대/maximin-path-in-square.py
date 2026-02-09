n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(1, n):
    grid[0][i] = min(grid[0][i], grid[0][i-1])
    grid[i][0] = min(grid[i][0], grid[i-1][0])
for row in range(1, n):
    for col in range(1, n):
        grid[row][col] = min(max(grid[row-1][col], grid[row][col-1]), grid[row][col])
print(grid[-1][-1])