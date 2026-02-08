n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(1, n):
    grid[0][-1-i] += grid[0][-i]
    grid[i][-1] += grid[i-1][-1]

for row in range(1, n):
    for col in range(n-2, -1, -1):
        grid[row][col] += min(grid[row-1][col], grid[row][col+1])

print(grid[-1][0])