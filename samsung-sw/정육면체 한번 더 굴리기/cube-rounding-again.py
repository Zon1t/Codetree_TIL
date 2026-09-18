# 시작 15:02
# score_grid 따로 업데이트 해주기. 주사위 인덱스 관리 잘하면 될듯..
# 그 이외 특이사항은 없어보인다? 방향 잘 꺾고 하면 될듯


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move():
    next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    next_dir = curr_dir
    if not in_range(next_row, next_col):
        next_dir = (curr_dir + 2) % 4
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
    
    if next_dir == 0:
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
    elif next_dir == 1:
        dice[0], dice[1], dice[5], dice[3] = dice[3], dice[0], dice[1], dice[5]
    elif next_dir == 2:
        dice[0], dice[2], dice[5], dice[4] = dice[4], dice[0], dice[2], dice[5]
    else:
        dice[0], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[0]
    
    if grid[next_row][next_col] < dice[-1]:
        next_dir = (next_dir+1)%4
    elif grid[next_row][next_col] > dice[-1]:
        next_dir = (next_dir-1)%4
    
    return next_row, next_col, next_dir
    

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dice = [1, 2, 4, 5, 3, 6]

visited = [[False] * N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if visited[row][col]:
            continue
        visited[row][col] = True
        Q = [(row, col)]
        cnt, pointer = 1, 0
        while pointer < cnt:
            for d in range(4):
                next_row, next_col = Q[pointer][0] + dr[d], Q[pointer][1] + dc[d]

                if not in_range(next_row, next_col) or visited[next_row][next_col]:
                    continue
                if grid[next_row][next_col] != grid[Q[pointer][0]][Q[pointer][1]]:
                    continue

                visited[next_row][next_col] = True
                Q.append((next_row, next_col))
                cnt += 1
            pointer += 1
        
        write_num = grid[row][col]*cnt
        for qr, qc in Q:
            visited[qr][qc] = write_num

curr_row, curr_col, curr_dir = 0, 0, 0
answer = 0
for _ in range(M):
    curr_row, curr_col, curr_dir = move()
    answer += visited[curr_row][curr_col]

print(answer)