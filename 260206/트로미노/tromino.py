n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_num = 0

drc_dict = {
    0 : [(0, 0), (1, 0), (1, 1)],
    1 : [(1, 0), (1, 1), (0, 1)],
    2 : [(0, 0), (0, 1), (1, 1)],
    3 : [(0, 0), (1, 0), (0, 1)],
    4 : [(0, 0), (0, 1), (0, 2)],
    5 : [(0, 0), (1, 0), (2, 0)]
}

def calc_area(drc_list, row, col):
    temp = 0
    for dr, dc in drc_list:
        nr, nc = row + dr, col + dc
        if 0 <= nr < n and 0 <= nc < m:
            temp += grid[nr][nc]
        else:
            return 0
    return temp

for row in range(n):
    for col in range(m):
        for i in range(6):
            temp = calc_area(drc_dict[i], row, col)
            max_num = max(max_num, temp)

print(max_num)