# 해야 할 것.
# 흩어지는 먼지에 대한 연산 처리(델타 어떻게 세팅할지, 비율 체크 등)
# *나머지는 바로 앞 칸으로 넘겨주기.
# 이동 칸 수는 어떻게? 1, 1, 2, 2, 3, 3, .... (턴 수) // 2 + 1 정도?


# 진행 상황에 맞게끔 세팅
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 흩어지는 먼지 양 연산에 관하여 세팅(진행 방향 기준 연산)
# d[idx] : (진행방향, 좌회전, 뒤, 우회전, 비율), 대칭 생각하면 좀 줄일 수 있을 것 같은데 혹시
# 빼먹을 우려가 있으니 완탐으로 진행하자.
deltas = [
    (2, 0, 0, 0, 0.05),
    (1, 1, 0, 0, 0.1),
    (1, 0, 0, 1, 0.1),
    (0, 1, 0, 0, 0.07),
    (0, 0, 0, 1, 0.07),
    (0, 2, 0, 0, 0.02),
    (0, 0, 0, 2, 0.02),
    (0, 1, 1, 0, 0.01),
    (0, 0, 1, 1, 0.01)
]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def simulate():
    global answer

    # 쓰일 변수들 선언.
    now_munji = grid[curr_row][curr_col]
    remain_munji = now_munji

    # 조기 종료 조건
    if now_munji == 0:
        return

    # 먼지의 양 업데이트
    for i in range(9):
        next_row, next_col = curr_row, curr_col

        # 조건에 맞게 위치 이동시키기
        for d in range(4):
            if deltas[i][d]:
                next_row += dr[(curr_dir+d)%4] * deltas[i][d]
                next_col += dc[(curr_dir+d)%4] * deltas[i][d]

        ratio = deltas[i][4]
        move_munji = int(now_munji * ratio)

        # 격자에서 벗어나면 제외.
        if not in_range(next_row, next_col):
            answer += move_munji
        else:
            grid[next_row][next_col] += move_munji
        remain_munji -= move_munji

    # 나머지는 바로 앞 칸에 업데이트
    front_row, front_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    if not in_range(front_row, front_col):
        answer += remain_munji
    else:
        grid[front_row][front_col] += remain_munji

    # 현재 위치 먼지 양 없애기. 주는 영향이 없어서 안없애도 되는데 혹시 모르니?
    grid[curr_row][curr_col] = 0


# 입력 받기
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 전역변수 선언
curr_dir, turn_idx, cnt = 0, 0, 0
target_cnt = [i//2+1 for i in range(2*N)]     # 연산해보니 2*N 만큼 진행되길래..
curr_row, curr_col = N//2, N//2
answer = 0

# 시뮬 진행
while True:
    # 종료조건 잘 달기.
    if curr_row == 0 and curr_col == 0:
        break

    # 이동시키기
    curr_row += dr[curr_dir]
    curr_col += dc[curr_dir]

    # 직관적으로 진행되는 순서에 맞게 업데이트를 진행하자.
    simulate()
    cnt += 1

    # 조건에 맞게 전역변수들 업데이트
    if cnt == target_cnt[turn_idx]:
        curr_dir = (curr_dir + 1) % 4
        turn_idx += 1
        cnt = 0

print(answer)