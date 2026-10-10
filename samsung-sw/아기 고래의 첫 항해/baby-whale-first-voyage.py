# 1. 인접 탐험.
#       - delta_lst = [0, 1, -1, 2] 활용해서 우선순위 체크
#       - 인접한 칸이 없을 때까지 반복하기.

# 2. 가장 가까운 바다로 이동.
#       - 가장 가까운, 행작-열작 칸 방문하기.
#       - 이동 우선순위는 좌-하-우-상
#       - 마지막 방향으로 갱신되는 게 중요.

from collections import deque

def adj_move():
    global whale, whale_dir
    for delta_d in delta_dir:
        next_dir = (whale_dir + delta_d) % 4
        next_whale = whale + delta_pos[next_dir]
        
        if visited[next_whale] or grid[next_whale]:
            continue

        whale, whale_dir = next_whale, next_dir
        visited[whale] = True
        answer.append(str(whale//N) + ' ' + str(whale%N))
        return True

    return False

def sea_move():
    global whale, whale_dir
    dir_grid = [-1] * max_pos
    dir_grid[whale] = whale_dir
    next_pos = max_pos
    
    Q = deque([whale])
    while Q:
        for _ in range(len(Q)):
            curr_whale = Q.popleft()
            for d in range(4):
                next_whale = curr_whale + delta_pos[d]

                if grid[next_whale] or dir_grid[next_whale] != -1:
                    continue

                dir_grid[next_whale] = d
                Q.append(next_whale)
                
                if not visited[next_whale]:
                    next_pos = min(next_pos, next_whale)
        if next_pos != max_pos:
            break

    if next_pos == max_pos:
        return False

    whale, whale_dir = next_pos, dir_grid[next_pos]
    visited[whale] = True
    answer.append(str(whale//N) + ' ' + str(whale%N))
    return True


# ========================================================================================
# 세팅

N, whale_row, whale_col, whale_dir = map(int, input().split())
grid = [1] * (N+2)
for _ in range(N):
    grid.extend([1] + list(map(int, input().split())) + [1])
grid += [1] * (N+2)

N += 2
max_pos = N**2

delta_pos = [-1, N, 1, -N]
delta_dir = [0, 1, -1, 2]
dir_lst = [None, 3, 1, 0, 2]
whale_dir = dir_lst[whale_dir]

whale = whale_row * N + whale_col
visited = [False] * N**2
visited[whale] = True

answer = [str(whale_row) + ' ' + str(whale_col)]

# =========================================================================================
# 실행부

while True:
    while adj_move():
        continue

    if not sea_move():
        break

print('\n'.join(answer))