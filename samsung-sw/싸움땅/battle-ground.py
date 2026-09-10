''' 싸움땅 / 20260910 / 체감 난이도 : 골드 4~3
소요 시간 : 58분 / 시도 : 1회 / 실행 시간 : 112ms / 메모리 : 19MB

타임 라인 : 구상(16분) - 구현(32분) - 검증(10분)


[구상]
    - 굉장히 전형적인 ? '시키는 거 잘해라' 하는 문제라고 생각되었다. 조건이 나름 세세하게 잘 주어져
    있다고 생각되어서 기본적인 틀만 잡고, 구현 단계에서 문제 읽으며 구현하면 되겠다는 생각이 들었다.
    - 상호작용을 하기 위해 필요한 변수들을 쭉 생각해보았다. 좌표를 알면 해당 칸 플레이어가 누가 있는
    지 알아야 하고, 총이 여러개 떨어져 있을 수도 있고 등등.. 조건을 생각하며 변수들을 선언했다.

[구현]
    - 그냥 시키는대로 쭉 구현했다. 간만에 함수 거의 안나누고 쭉 하드코딩한 문제였다.
    - 구현 때 유일하게 까다로웠던 것은 정보 업데이트 시점이였던 것 같다. 업데이트 시점을 잘못 잡으면
    덮어 씌워질 수 있기 때문에 이를 염두하며 구현을 진행했다. win/lose player 정도만 일반화 작업
    을 진행했다. 총 줍기 등 일부 로직은 함수화하는 게 더 괜찮았을지도?

[검증]
    - 주저리주저리 길게 작성한 코드이다 보니 혹시 헷갈린 부분이 있었을까, 잘못 작성한 부분이 있었을까
    생각해보며 검증을 이어갔다.
    - pprint와 내가 보고자 하는 변수들을 찍어보며 상태를 관찰해보았다. 모두 올바르게 출력됨을 확인한
    뒤 문제 한 번 더 읽고 제출해보았다.
'''


# 격자 위 여러 객체에 대한 상호작용을 다루는 전형적인 문제같다.
# 시키는 대로 잘만 하면 될듯? 이럴 때 클래스 쓸 줄 알면 좋은 것 같은데.. 일단은 그냥 하자.
# 생각해보니 좌표 -> 플레이어도 가능해야 함.. 이것도 저장하자.

# 주어진 순서에 맞게 델타 세팅
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(player):
    curr_row, curr_col = positions[player]
    next_dir = directions[player]

    # 1-1. 다음 이동 위치 판단
    next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
    if not in_range(next_row, next_col):
        next_dir = (next_dir + 2) % 4
        next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

    player_grid[curr_row][curr_col] = -1
    positions[player] = (next_row, next_col)
    directions[player] = next_dir

    # 2-1. 플레이어가 없다면.. 총 줍기.
    if player_grid[next_row][next_col] == -1:
        if guns[next_row][next_col]:
            my_gun, max_gun = having_guns[player], max(guns[next_row][next_col])
            if my_gun < max_gun:
                max_idx = guns[next_row][next_col].index(max_gun)

                if my_gun:
                    guns[next_row][next_col][max_idx] = my_gun
                else:
                    guns[next_row][next_col].pop(max_idx)

                having_guns[player] = max_gun

        # 정보 업데이트 잘하자.
        player_grid[next_row][next_col] = player

    # 2-2. 만약 플레이어가 있다면?!
    else:
        another_player = player_grid[next_row][next_col]
        my_power, another_power = status[player]+having_guns[player], status[another_player]+having_guns[another_player]

        # 승자 패자 판단하기.
        if my_power > another_power or \
                (my_power == another_power and status[player] > status[another_player]):
            win_player, lose_player = player, another_player
        else:
            win_player, lose_player = another_player, player

        scores[win_player] += abs(my_power-another_power)

        # 패배자 총 떨구기
        if having_guns[lose_player]:
            guns[next_row][next_col].append(having_guns[lose_player])
            having_guns[lose_player] = 0

        # 패배자 이동시키기
        lose_row, lose_col = positions[lose_player]
        lose_dir = directions[lose_player]
        for delta_d in range(4):
            lose_nd = (lose_dir + delta_d) % 4
            lose_nr, lose_nc = lose_row + dr[lose_nd], lose_col + dc[lose_nd]

            if not in_range(lose_nr, lose_nc) or player_grid[lose_nr][lose_nc] != -1:
                continue

            # 정보 업데이트
            lose_row, lose_col, lose_dir = lose_nr, lose_nc, lose_nd
            player_grid[lose_row][lose_col] = lose_player
            positions[lose_player] = (lose_row, lose_col)
            directions[lose_player] = lose_dir
            break

        # 총 줍기
        if guns[lose_row][lose_col]:
            max_gun = max(guns[lose_row][lose_col])
            max_idx = guns[lose_row][lose_col].index(max_gun)
            guns[lose_row][lose_col].pop(max_idx)
            having_guns[lose_player] = max_gun

        # 이긴 애도 총 줍기.
        if guns[next_row][next_col]:
            my_gun, max_gun = having_guns[win_player], max(guns[next_row][next_col])
            if my_gun < max_gun:
                max_idx = guns[next_row][next_col].index(max_gun)

                if my_gun:
                    guns[next_row][next_col][max_idx] = my_gun
                else:
                    guns[next_row][next_col].pop(max_idx)

                having_guns[win_player] = max_gun

        # 정보 업데이트
        player_grid[next_row][next_col] = win_player

# import pprint
# def print_grid():
#     print(f'----player_grid----')
#     for row in player_grid:
#         print(*row)
#
#     print(f'----gun_grid----')
#     pprint.pprint(guns)
#
#     print(f'----player_status----')
#     print(*having_guns)
#     print(*positions)
#     print(*directions)


# 플레이어 정보 관리
N, M, K = map(int, input().split())
positions = []
directions = []
status = []
having_guns = [0] * M          # 초기엔 총 없음

# 총 정보 받기
guns = [[[] for _ in range(N)] for _ in range(N)]
for row in range(N):
    for col, val in enumerate(map(int, input().split())):
        if not val:
            continue
        guns[row][col].append(val)

# 플레이어 정보 받기
player_grid = [[-1] * N for _ in range(N)]
for idx in range(M):
    r, c, d, s = map(int, input().split())
    player_grid[r-1][c-1] = idx
    positions.append((r-1, c-1))
    directions.append(d)
    status.append(s)

# 실행부
scores = [0] * M
for _ in range(K):
    for player in range(M):
        move(player)

# 정답 출력
print(*scores)