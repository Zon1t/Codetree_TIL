# 백트래킹 문제인가? 격자의 크기는 최대 8*8
# 자신의 말도 최대 8개. 음.. 4^8의 가짓수면 그냥 완탐이긴 하다.
# 뭘 어떻게 풀어도 다 될 것 같긴 한데, 그냥 itertools 써보면 될 것도 같다.

from itertools import product

def in_range(row, col):
    return 0 <= row < N and 0 <= col < M

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 돌아가는 방향에 대한 부분
# deltas[idx] : idx번호의 기물이 컨트롤 하는 상대방향
deltas = [None, [0], [-1, 1], [0, 1], [-1, 0, 1], [-1, 0, 1, 2]]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 64

cnt, ours = 0, []
empty = 0
for row in range(N):
    for col in range(M):
        if 1 <= grid[row][col] <= 5:
            ours.append((row, col))
            cnt += 1
        elif grid[row][col] == 0:
            empty += 1

comb_lst = []
for row, col in ours:
    if grid[row][col] == 2:
        comb_lst.append((0, 1))
    elif grid[row][col] == 5:
        comb_lst.append((0,))
    else:
        comb_lst.append((0, 1, 2, 3))

# 각 조합에 대한 빈 칸의 개수 세기.
for t in product(*comb_lst):
    temp_grid = [[0]*M for _ in range(N)]
    temp_cnt = empty
    for idx in range(cnt):
        curr_row, curr_col = ours[idx]
        curr_dir = t[idx]
        for delta_d in deltas[grid[curr_row][curr_col]]:
            next_dir = (curr_dir + delta_d)%4
            next_row, next_col = curr_row, curr_col
            while True:
                next_row += dr[next_dir]
                next_col += dc[next_dir]

                if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
                    break

                if grid[next_row][next_col] == 0 and temp_grid[next_row][next_col] == 0:
                    temp_cnt -= 1
                    temp_grid[next_row][next_col] = 1

    if temp_cnt < answer:
        answer = temp_cnt

print(answer)
