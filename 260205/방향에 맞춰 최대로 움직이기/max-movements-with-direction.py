n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.

def find_bigger(row, col):
    dr, dc = direction_dict[move_dir[row][col]]
    possible_list = []
    nr, nc = row + dr, col + dc
    while 0 <= nr < n and 0 <= nc < n:
        if num[row][col] < num[nr][nc]:
            possible_list.append((nr, nc))
        nr += dr
        nc += dc
    return possible_list

def backtrack(row, col, count):
    global max_cnt
    possible_list = find_bigger(row, col)

    if not possible_list:
        max_cnt = count if max_cnt < count else max_cnt
        return
    
    for next_row, next_col in possible_list:
        backtrack(next_row, next_col, count+1)

direction_dict = {
    1 : [-1, 0],
    2 : [-1, 1],
    3 : [0, 1],
    4 : [1, 1],
    5 : [1, 0],
    6 : [1, -1],
    7 : [0, -1],
    8 : [-1, -1]
}
max_cnt = 0
backtrack(r-1, c-1, 0)
print(max_cnt)