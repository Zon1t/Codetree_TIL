n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# def find_track(r, c, now_min, now_max):
#     answer_list = [[[] for _ in range(n)] for _ in range(n)]
#     answer_list[0][0].append((now_min, now_max))

#     # 초기 세팅
#     for i in range(c+1, n):
#         answer_list[r][i].append((min(answer_list[r][i-1][0][0], grid[r][i]), max(answer_list[r][i-1][0][1], grid[r][i])))
#     for i in range(r+1, n):
#         answer_list[i][c].append((min(answer_list[i-1][c][0][0], grid[i][c]), max(answer_list[i-1][c][0][1], grid[i][c])))
    
#     for row in range(r+1, n):
#         for col in range(c+1, n):
#             if len(answer_list[row-1][col]) == 2:
#                 result_min1, result_max1 = find_track(row-1, col, answer_list[row-1][col][0][0], answer_list[row-1][col][0][1])
#                 result_min2, result_max2 = find_track(row-1, col, answer_list[row-1][col][1][0], answer_list[row-1][col][1][1])
#                 if result_max2 - result_min2 < result_max1 - result_min1:
#                     answer_list[row-1][col].pop(0)
#                 else:
#                     answer_list[row-1][col].pop()
#             temp_min1 = min(answer_list[row-1][col][0][0], grid[row][col])
#             temp_max1 = max(answer_list[row-1][col][0][1], grid[row][col])
#             if len(answer_list[row][col-1]) == 2:
#                 result_min1, result_max1 = find_track(row, col-1, answer_list[row][col-1][0][0], answer_list[row][col-1][0][1])
#                 result_min2, result_max2 = find_track(row, col-1, answer_list[row][col-1][1][0], answer_list[row][col-1][1][1])
#                 if result_max2 - result_min2 < result_max1 - result_min1:
#                     answer_list[row][col-1].pop(0)
#                 else:
#                     answer_list[row][col-1].pop()
#             temp_min2 = min(answer_list[row][col-1][0][0], grid[row][col])
#             temp_max2 = max(answer_list[row][col-1][0][1], grid[row][col])

#             if temp_max1 - temp_min1 <= temp_max2 - temp_min2:
#                 answer_list[row][col].append((temp_min1, temp_max1))
#             if temp_max1 - temp_min1 >= temp_max2 - temp_min2:
#                 answer_list[row][col].append((temp_min2, temp_max2))

#     return answer_list[-1][-1][0]

# answer_min, answer_max = find_track(0, 0, grid[0][0], grid[0][0])
# print(answer_max - answer_min)

unique_list = list(set([grid[row][col] for row in range(n) for col in range(n)]))
unique_list.sort()

def in_range(row, col, minimum, maximum):
    return (minimum <= grid[row][col] <= maximum)

def is_possible(minimum, maximum):
    if not in_range(0, 0, minimum, maximum):
        return False
    if not in_range(-1, -1, minimum, maximum):
        return False

    dp = [[False] * n for _ in range(n)]
    dp[0][0] = True

    for i in range(1, n):
        if dp[0][i-1] and in_range(0, i, minimum, maximum):
            dp[0][i] = True
        else:
            break
    for i in range(1, n):
        if dp[i-1][0] and in_range(i, 0, minimum, maximum):
            dp[i][0] = True
        else:
            break
    for row in range(1, n):
        for col in range(1, n):
            if (dp[row-1][col] or dp[row][col-1]) and in_range(row, col, minimum, maximum):
                dp[row][col] = True
    return dp[-1][-1]

left = right = 0
ans = 100
num_count = len(unique_list)
while left < num_count and right < num_count:
    if is_possible(unique_list[left], unique_list[right]):
        ans = min(ans, unique_list[right]-unique_list[left])
        left += 1
        if left > right:
            right = left
    else:
        right += 1
print(ans)