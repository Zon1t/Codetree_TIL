''' 청소는 즐거워 / 20260826 / 체감 난이도 : 골드 5~4
소요 시간 : 37분 / 시도 : 1회 / 실행 시간 : 416 / 메모리 : 24MB

타임 라인 : 구상+세팅(12분) - 구현(20분) - 검증(5분)


[구상]
    - 각 위치와 비율에 맞게끔 먼지를 퍼뜨려 줘야 하는데 이를 어떤 방식으로 구현할 지 고민이 되었다.
    - 좀 일반화해서 풀고자 상대 좌표별 이동 칸 수, 비율 정보를 저장해서 끌어다가 쓰게 되었다.
    - 더불어 이동 칸 수에 대해서도 고민해본 결과, 그냥 규칙에 맞는 배열을 생성해 사용하기로 했다.

[구현]
    - 충분한 구상을 거쳤다고 생각했고, 그대로 구현할 수 있어 코드를 치는 시간이 많지는 않았던 것 같다.
    - Curr칸에는 먼지가 없어진다고는 하지만 사실상 영향이 없다. 이를 인지하고 따로 처리해주지는 않았는데
    예시 자료와 비교를 위해 따로 0으로 처리해주었다. 검증 때 용이했다.

[검증]
    - 혹시 에지 케이스가 존재할지 구상때도 고민을 했었는데 달리 없다고 생각했다.
    - 인덱스를 사용한 부분에서 혹시 경계 처리를 안했는지 등 한 번 더 체크해보고 곧바로 제출해보았다.
'''

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
ratios = [5, 10, 10, 2, 7, 7, 2, 1, 1]
deltas = [
    [(0, -2), (-1, -1), (1, -1), (-2, 0), (-1, 0), (1, 0), (2, 0), (-1, 1), (1, 1)]
]
for _ in range(3):
    temp = []
    for dr_, dc_ in deltas[-1]:
        temp.append((-dc_, dr_))
    deltas.append(temp)

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
        next_row, next_col = curr_row + deltas[curr_dir][i][0], curr_col + deltas[curr_dir][i][1]
        move_munji = (now_munji * ratios[i]) // 100

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

    # 현재 위치 먼지 양 없애기. 주는 영향이 없어서 안 없애도 되는데 혹시 모르니?
    grid[curr_row][curr_col] = 0


# 입력 받기
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 전역변수 선언
curr_dir, turn, cnt = 0, 0, 0
target_cnt = turn // 2 + 1
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
    if cnt == target_cnt:
        curr_dir = (curr_dir + 1) % 4
        turn += 1
        target_cnt = turn // 2 + 1
        cnt = 0

print(answer)