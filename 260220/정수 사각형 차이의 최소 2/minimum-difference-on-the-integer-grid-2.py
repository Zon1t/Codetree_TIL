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

from collections import deque

dr = [0, 1]
dc = [1, 0]

def in_range(row, col):
    return (0 <= row < n and 0 <= col < n)

def find_track(value):
    q = deque([(0, 0, grid[0][0], grid[0][0])])
    while q:
        row, col, track_min, track_max = q.popleft()
        if track_max - track_min > value:
            continue
        if (row, col) == (n-1, n-1):
            return True
        for i in range(2):
            nr, nc = row + dr[i], col + dc[i]
            if in_range(nr, nc):
                q.append((nr, nc, min(track_min, grid[nr][nc]), max(track_max, grid[nr][nc])))
    return False

start = 0
end = 99
while start < end:
    mid = (start+end)//2
    if find_track(mid):
        end = mid
    else:
        start = mid+1
print(start)