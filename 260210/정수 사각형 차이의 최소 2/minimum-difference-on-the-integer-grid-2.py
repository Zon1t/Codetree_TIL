n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer_list = [[[0]*2 for _ in range(n)] for _ in range(n)]
answer_list[0][0][0] = grid[0][0]
answer_list[0][0][1] = grid[0][0]

for i in range(1, n):
    answer_list[0][i][0] = min(answer_list[0][i-1][0], grid[0][i])
    answer_list[0][i][1] = max(answer_list[0][i-1][1], grid[0][i])
    answer_list[i][0][0] = min(answer_list[i-1][0][0], grid[i][0])
    answer_list[i][0][1] = max(answer_list[i-1][0][1], grid[i][0])

for row in range(1, n):
    for col in range(1, n):
        temp_min1 = min(answer_list[row-1][col][0], grid[row][col])
        temp_max1 = max(answer_list[row-1][col][1], grid[row][col])
        temp_min2 = min(answer_list[row][col-1][0], grid[row][col])
        temp_max2 = max(answer_list[row][col-1][1], grid[row][col])
        if temp_max1 - temp_min1 < temp_max2 - temp_min2:
            answer_list[row][col][0] = temp_min1
            answer_list[row][col][1] = temp_max1
        else:
            answer_list[row][col][0] = temp_min2
            answer_list[row][col][1] = temp_max2

print(answer_list[-1][-1][1]-answer_list[-1][-1][0])