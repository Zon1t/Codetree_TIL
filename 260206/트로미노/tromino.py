n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_num = 0

for row in range(n-1):
    for col in range(m-1):
        temp = 0
        temp += grid[row][col] + grid[row+1][col] + grid[row+1][col+1]
        max_num = max(max_num, temp)

for row in range(n):
    for col in range(m-2):
        temp = 0
        temp += grid[row][col] + grid[row][col+1] + grid[row][col+2]
        max_num = max(max_num, temp)
print(max_num)