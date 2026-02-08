n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(1, n):
    grid[i][0] += grid[i-1][0]
    grid[0][i] += grid[0][i-1]
for row in range(1, n):
    for col in range(1, n):
        grid[row][col] += max(grid[row-1][col], grid[row][col-1])
print(grid[-1][])