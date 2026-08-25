''' 이상한 체스 / 20260825 / 체감 난이도 : 실버 1~2
소요 시간 : 24분 / 제출 시도 : 1회 / 실행 시간 : 116ms / 메모리 : 20MB

타임 라인 : 구상(5분) - 구현(14분) - 검증(5분)


[구상]
    - 풀 수 있는 방법론이 여럿 떠올랐다. 대략적인 시간 복잡도에 대해서 생각해보았는데 크게 문제될 것 같진 않았다.
     그 중 가장 검증이 쉽고, 편하게 풀 수 있는 방법을 채택하게 되었다.
    - 상대 방향을 정의한 것은 꽤 괜찮은 방법론이라고 생각한다.

[구현]
    - 내 말에 대해서는 넘어갈 수 있다는 요소라던가, 솔직히 깊게 생각하고 들어가진 않았었다. 근데 구현 과정에서
    해당 조건이 자연스럽게 만족된 것 같다. 운이 좋았다.
    - 사실 5일 때는 방향을 생각할 필요가 없었다는 점 등을 고려하면 더 최적화시킬 수 있지 않았을까 생각이 든다.

[검증]
    - 사실 itertools.product를 사용해서 내가 빼먹은 케이스가 있다고는 생각 못한 것 같다.
    - 빈 칸의 수를 세는 로직이 엄밀한지, 혹시 잘못 적은 코드가 있는지, 상대 방향들은 올바르게 작성하였는지 등을
    중점으로 다시 한 번 생각해보고 제출했다.

[리팩토링 예정 사항]
    - 5인 케이스에 대해서 따로 빼놓고 진행하자. 시간을 줄일 수 있을 것이라 생각된다.
'''

# 백트래킹 문제인가? 격자의 크기는 최대 8*8
# 자신의 말도 최대 8개. 음.. 4^8의 가짓수면 그냥 완탐이긴 하다.
# 뭘 어떻게 풀어도 다 될 것 같긴 한데, 그냥 itertools 써보면 될 것도 같다.

from itertools import product

def in_range(row, col):
    return 0 <= row < N and 0 <= col < M

def update_grid(row, col, dir, curr_grid):
    next_row, next_col = row, col
    erase_cnt = 0

    while True:
        next_row += dr[dir]
        next_col += dc[dir]

        if not in_range(next_row, next_col) or grid[next_row][next_col] == 6:
            break

        if grid[next_row][next_col] == 0 and curr_grid[next_row][next_col] == 0:
            erase_cnt += 1
            curr_grid[next_row][next_col] = 1

    return erase_cnt

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 돌아가는 방향에 대한 부분
# deltas[idx] : idx번호의 기물이 컨트롤 하는 상대방향
deltas = [None, [0], [-1, 1], [0, 1], [-1, 0, 1], [-1, 0, 1, 2]]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cnt, ours, fives = 0, [], []
empty = 0
for row in range(N):
    for col in range(M):
        if 1 <= grid[row][col] <= 4:
            ours.append((row, col))
            cnt += 1
        elif grid[row][col] == 5:
            fives.append((row, col))
        elif grid[row][col] == 0:
            empty += 1

for curr_row, curr_col in fives:
    for d in range(4):
        erase_cnt = update_grid(curr_row, curr_col, d, grid)
        empty -= erase_cnt
        
answer = empty
# 각 조합에 대한 빈 칸의 개수 세기.
for t in product((0, 1, 2, 3), repeat=cnt):
    temp_grid = [[0]*M for _ in range(N)]
    temp_cnt = empty

    for idx in range(cnt):
        curr_row, curr_col = ours[idx]
        curr_dir = t[idx]
        for delta_d in deltas[grid[curr_row][curr_col]]:
            temp_cnt -= update_grid(curr_row, curr_col, (curr_dir + delta_d)%4, temp_grid)

    if temp_cnt < answer:
        answer = temp_cnt

print(answer)