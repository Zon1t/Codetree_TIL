# 독점계약 턴 수는 end_grid에 덮으쓰는 방식으로 진행한다.
# 우선순위 관리 -> 각 플레이어 index에 맞게 리스트를 만들어 순차탐색 하는 방향으로 가자.
# if 갈 길이 없으면 주위 우선순위 기반 독점계약 땅으로 이동. 이것도 잘 처리하기
# 같은 칸에 있으면 게임에서 사라짐. 사라지면 계약한 땅은? 예제 보니까 남아있긴 하네.
# 게임이 안끝나는 경우는 없나?

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def simulate():
    global pos_to_idx
    new_dict = dict()
    for player_idx in list(idx_to_pos.keys()):
        curr_row, curr_col = idx_to_pos[player_idx]
        # 1-1. 비어있는 공간 찾기.
        for next_dir in priority_info[player_idx][dir_info[player_idx]]:
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
            if not in_range(next_row, next_col):
                continue
            if spot_info[next_row][next_col][0] < turn:
                break
        # 1-2. 비어있는 공간을 못찾은 경우. 내 계약 칸으로 이동.
        else:
            for next_dir in priority_info[player_idx][dir_info[player_idx]]:
                next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
                if not in_range(next_row, next_col):
                    continue
                if spot_info[next_row][next_col][1] == player_idx:
                    break

        # 2. 적절하게 정보 업데이트 해주기.
        dir_info[player_idx] = next_dir
        idx_to_pos[player_idx] = (next_row, next_col)
        new_dict[next_row, next_col] = new_dict.get((next_row, next_col), []) + [player_idx]

    # 3. 다 수행하고 남길 사람 남기기.
    for row, col in new_dict:
        new_dict[(row, col)].sort()
        remain_player = new_dict[(row, col)][0]
        for erase_player in new_dict[(row, col)][1:]:
            idx_to_pos.pop(erase_player)
        new_dict[(row, col)] = remain_player
        spot_info[row][col] = (turn+K, remain_player)

    pos_to_idx = new_dict

def custom_print():
    print(f'-------pos_info--------')
    for row in range(N):
        for col in range(N):
            if (row, col) in pos_to_idx:
                print(pos_to_idx[(row, col)], end=' ')
            else:
                print(0, end=' ')
        print()
    print(f'-------spot_info---------')
    for row in spot_info:
        print(*row)
    print(f'-------player_info--------')
    for k in sorted(idx_to_pos):
        print(f'key:{k}, pos:{idx_to_pos[k]}')
        print(f'dir:{dir_info[k]}')


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dir_info = [None] + list(map(lambda x: int(x)-1, input().split()))

idx_to_pos = dict()
pos_to_idx = dict()
spot_info = [[(-1, -1)] * N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if grid[row][col]:
            idx_to_pos[grid[row][col]] = (row, col)
            pos_to_idx[(row, col)] = grid[row][col]
            spot_info[row][col] = (K, grid[row][col])

priority_info = [None]
for _ in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(lambda x: int(x)-1, input().split())))
    priority_info.append(temp)

answer = -1
for turn in range(1, 1001):
    # 시뮬레이션 진행.
    simulate()
    # custom_print()
    # 종료 체크
    if len(idx_to_pos) == 1:
        answer = turn
        break

print(answer)