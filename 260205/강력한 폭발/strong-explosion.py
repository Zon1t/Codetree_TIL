N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

drc_dict = {
    0 : [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    1 : [(-1, 0), (0, 1), (1, 0), (0, -1)],
    2 : [(-1, -1), (-1, 1), (1, 1), (1, -1)]
}

one_position = [(r, c) for c in range(N) for r in range(N) if grid[r][c]]
length = len(one_position)
max_count = 0

def backtrack(idx):
    global max_count
    if idx == length:
        count = 0
        for row in range(N):
            for col in range(N):
                if grid[row][col]:
                    count += 1
        max_count = max_count if count < max_count else count
        return
    
    row, col = one_position[idx]
    for i in range(3):
        temp_list = []
        for dr, dc in drc_dict[i]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N:
                grid[nr][nc] += 1
                temp_list.append((nr, nc))
        backtrack(idx+1)
        for r, c in temp_list:
            grid[r][c] -= 1

backtrack(0)
print(max_count)