n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_nount = 0
for row in range(n-2):
    for col in range(n-2):
        temp = 0
        for i in range(3):
            for j in range(3):
                temp += grid[row+i][col+j]
        max_nount = temp if max_nount < temp else max_nount
print(max_nount)