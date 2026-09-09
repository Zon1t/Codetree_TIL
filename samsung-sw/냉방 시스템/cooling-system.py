''' 냉방 시스템 / 20260909 / 체감 난이도 : 골드 2~3
소요 시간 : 88분 / 시도 : 2회(1회차 : 틀림) / 실행 시간 : 189ms / 메모리 : 24MB

타임 라인 : 구상 및 틀 만들기(40분) - 구현(24분) - 검증(8분) - 수정(16분)


[구상]
    - 시원함 전파 로직을 어떻게 구성할 수 있을까에 대해서 많은 고민을 했던 것 같다. 규칙성?이라기엔
    좀 그렇지만 각 방향 별로, 어느 칸에 전파되기 위해선 확인해야 하는 벽들이 정해져 있음을 발견하고
    해당 벽의 type과 위치를 판단하기 위해 세팅을 진행하였다. 사실상 40분 중 대부분은 이 리스트를
    떠올리고 만드는 것에 다 쓴 것 같다.
    - 이렇게 만든 matrix를 재탕하면 된다 정도를 생각하고 넘어갔다. 그 밖의 부분은 구현 단계에서 생
    각하며 구현해도 될 것이라 판단했다.

[구현]
    - 구현 중간에 매번 순회하면서 반영할까 vs 나중에 연산할 때 turn을 곱해줘서 사용할까 정도 고민
    했었는데, 외벽 깎는 로직이 0 아닐때만 진행되기도 하고, 매번 인접한 칸과 비교하며 공기를 섞어야
    하다 보니 그냥 순회하며 업데이트 하기로 결정했다.
    - 틀을 잘 만들어 둬서 그 밖에 구현함에 있어서는 큰 문제가 없었다.

[검증]
    - 똑같이 매 grid 찍어보면서 시원함의 정도가 올바르게 변화하는지 관찰해보았다. 구현 단계에서 이미
    기능이 똑바로 수행되는지는 확인했어서 문제될 게 없다고 생각했다.

[수정]
    - 왜 틀렸지? 생각이 들었다. 나름 잘 구현했다고 생각했는데 하면서 내 코드를 쭉 훑어보았다. 델타
    세팅이나 check_lst를 봐도 문제가 없길래 문제를 다시 읽어보았다. 정독하자마자 뭘 빼먹었는지 눈에
    보였다. 심지어 문제에서
    ----------------------------------------------------
    " 벽을 사이에 두고 있는 칸끼리는 일어나지 않음에 유의합니다. "
    ----------------------------------------------------
    이거 까만색으로 굵게 칠해줬음; 왜 못 봤지.
    - 곧바로 수정한 뒤, 예제에서 작게 공기 섞이는 로직 중 벽이 있는 경우를 설명해준 예시가 있었다.
    이를 바탕으로 시도해보았고 문제 없이 돌아감을 확인했다. 문제가 되는 테케 복사해서 정답만 확인해
    보고 제출했다.
'''


# 0 : 빈칸, 1 : 사무실, 2~5 : 왼 위 오 아
# 에어컨이 있는 장소는 동일. 즉 update_matrix를 만들어서 매 분 추가해주는 느낌으로 진행하면
# 될 것 같다? 아예 턴마다 연산해주는 느낌으로.. 기본 grid는 냄겨두고.. 진행할까 싶기도 하다.
# 시원함 정도를 잘 업데이트 해주는 것이 좋다. 벽 있는 경우 처리에 대해서도 잘 생각해볼 필요가 있다.
# 벽도 패턴화해서 업데이트하면 될듯? 틀을 짜보자

from collections import deque

# 문제에서 주어진대로 델타 세팅.
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 에어컨 시원함 전파 방향. 순서 주의
delta_lst = [[(-1, -1), (0, -1), (1, -1)],
             [(-1, -1), (-1, 0), (-1, 1)],
             [(-1, 1), (0, 1), (1, 1)],
             [(1, -1), (1, 0), (1, 1)]]

# 전파 방향에 대해서 확인할 벽의 타입과 상대 좌표를 미리 담아둠. 왼, 위, 오, 아 순서
# (type, row, col)의 양식을 가짐.
check_lst = [[[(0, 0, 0), (1, -1, 0)], [(1, 0, 0)], [(0, 1, 0), (1, 1, 0)]],
             [[(0, 0, -1), (1, 0, 0)], [(0, 0, 0)], [(0, 0, 1), (1, 0, 1)]],
             [[(0, 0, 0), (1, -1, 1)], [(1, 0, 1)], [(0, 1, 0), (1, 1, 1)]],
             [[(0, 1, -1), (1, 0, 0)], [(0, 1, 0)], [(0, 1, 1), (1, 0, 1)]]]

# 공기 섰을 때 사용할 델타 세팅.
for_mix = [(1, 0), (0, 1)]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 에어컨 인접해 벽X + 격자 벗어남X 를 잘 이용해보자.
def make_update_grid(d, r, c):
    # 겹치면 안되니까 따로따로 진행하자.
    temp = [[0] * N for _ in range(N)]
    start_row, start_col = r + dr[d], c + dc[d]
    temp[start_row][start_col] = 5

    # bfs 진행
    Q = deque([(start_row, start_col, 5)])
    while Q:
        curr_row, curr_col, curr_num = Q.popleft()

        # 1이면 이후 볼 필요 X
        if curr_num == 1:
            break

        # 위 세팅에 맞게끔 진행하면 문제 없을 것!
        for order, (delta_row, delta_col) in enumerate(delta_lst[d]):
            next_row, next_col = curr_row + delta_row, curr_col + delta_col

            # 범위 밖이면 pass
            if not in_range(next_row, next_col):
                continue

            # 벽이 있는지에 대한 체크리스트 확인.
            for wt, ddr, ddc in check_lst[d][order]:
                check_row, check_col = curr_row + ddr, curr_col + ddc
                if (check_row, check_col) in (wall_type0 if wt == 0 else wall_type1):
                    break
            # break 안당했으면 여기! 격자에 적어주고 bfs 계속 ㄱㄱ
            else:
                temp[next_row][next_col] = curr_num-1
                Q.append((next_row, next_col, curr_num-1))

    # 다 돌렸으면 update_grid 업데이트
    for row in range(N):
        for col in range(N):
            update_grid[row][col] += temp[row][col]

# 시원함 업데이트하기
def update():
    for row in range(N):
        for col in range(N):
            air_grid[row][col] += update_grid[row][col]

# 공기 섞자! 벽 사이 로직을 구현 안했다.. 또 안읽네
def mix():
    temp = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            curr_air = air_grid[row][col]
            for idx, (delta_row, delta_col) in enumerate(for_mix):
                next_row, next_col = row + delta_row, col + delta_col

                # 범위 밖이거나 사이에 벽이 있는 경우 넘기기.
                if not in_range(next_row, next_col):
                    continue
                if idx == 0 and (next_row, next_col) in wall_type0:
                    continue
                if idx == 1 and (next_row, next_col) in wall_type1:
                    continue

                # 조건에 맞게 연산 ㄱㄱ
                next_air = air_grid[next_row][next_col]
                D = abs(next_air-curr_air) // 4
                if D:
                    temp[row][col] += D if curr_air < next_air else -D
                    temp[next_row][next_col] -= D if curr_air < next_air else -D

    # 최종 반영. 공기 섞는 과정은 한 번에 일어나므로.
    for row in range(N):
        for col in range(N):
            air_grid[row][col] += temp[row][col]

# 외벽 0이 아닌 애들 업데이트하기.
def reduce():
    for row in range(N):
        if air_grid[row][0]:
            air_grid[row][0] -= 1
        if air_grid[row][-1]:
            air_grid[row][-1] -= 1
    for col in range(1, N-1):
        if air_grid[0][col]:
            air_grid[0][col] -= 1
        if air_grid[-1][col]:
            air_grid[-1][col] -= 1

# 각 사무실 시원함 정도 체크
def check():
    for curr_row, curr_col in office:
        if air_grid[curr_row][curr_col] < K:
            return False
    return True

# 찍자
def print_grid():
    print(f'----air_grid----')
    for row in air_grid:
        print(*row)


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 격자 순회하면서 정보 저장.
office, air_cond = [], []
for row in range(N):
    for col in range(N):
        if grid[row][col] == 1:
            office.append((row, col))
        elif 2 <= grid[row][col] <= 5:
            air_cond.append((grid[row][col]-2, row, col))

# 현재 시원함 정도를 계속 반영하자.
air_grid = [[0] * N for _ in range(N)]

# 벽 세팅
wall_type0, wall_type1 = set(), set()
for _ in range(M):
    r, c, t = map(int, input().split())
    if t == 0:
        wall_type0.add((r-1, c-1))
    else:
        wall_type1.add((r-1, c-1))

# 에어컨으로 만들어지는 시원함 격자 세팅
update_grid = [[0] * N for _ in range(N)]
for d, r, c in air_cond:
    make_update_grid(d, r, c)

# 실행부
answer = -1
for turn in range(1, 101):
    # 시원함 업데이트.
    update()

    # 공기 섞기.
    mix()

    # 외벽 감소
    reduce()

    # 종료 체크
    if check():
        answer = turn
        break

# 정답 출력
print(answer)