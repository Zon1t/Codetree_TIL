''' 승자독식 모노폴리 / 20260903 / 체감 난이도 : 골드 4
소요 시간 : 57분 / 시도 : 1회 / 실행 시간 : 193ms / 메모리 : 22MB

타임 라인 : 구상 및 틀 만들기(19분) - 구현(20분) - 검증(18분)


[구상]
    - 문제가 이해하기 빡세고, 내가 생각했을 때의 애매한 부분이 좀 있었어서 예제를 보며 몇 가지를
    단정 짓고 넘어갔다. K턴 이후에 사라짐과 탈락한 플레이어의 계약 유지 여부가 이에 해당했고, 명
    확하게 하니 풀이 방식이 곧바로 떠오른 것 같다.
    - 저장하거나 접근해야 할 정보들이 꽤나 많았다고 생각이 들었다. 헷갈리지 않고, 정의를 명확히 해
    구현해야겠다 생각이 들었다.
    - 사람 번호는 주는대로, 방향은 0부터 시작하는 것으로 했다. 입력받거나 사용할 때의 편의를 고려
    한 결과이다.

[구현]
    - 틀을 다 짜둬서 simulate 함수만 구성하면 되었는데, 생각보다 훨씬 시간이 오래 걸렸던 것 같다.
    확실히 다뤄야 하는 변수가 많으니, 정의했던 부분으로 가서 재차 확인해보는 등의 과정을 많이 거쳤던
    것 같다.
    - idx_to_pos 딕셔너리 기준으로 계속 진행을 했었는데, 막바지에 pos_to_idx 딕셔너리를 기준으로
    해야 여럿 아낄 수 있는 요소들이 많았다는 생각이 들었다. 일단 그걸 바꾸기에는 너무 멀리 건너와서
    기존 방식으로 쭉 구현을 진행했다.

[검증]
    - custom_print 함수를 만들어 검증을 진행했다. 확인해야 할 요소들이 너무 많았기에, 각 턴마다
    적절하게 변화하는지를 중점으로 확인해보았다.
    - 업데이트 로직에 일부 하자가 있어 수정했다. 동시에 업데이트가 일어나야 한다고 생각해 새로운
    딕셔너리까지 만들었었는데, 업데이트를 개별로 하고 있었다;
    - 그 이외에는 모두 올바르게 구성했다고 판단하여, 문제를 재차 읽고 제출했다.
'''

# 독점계약 턴 수는 end_grid에 덮으쓰는 방식으로 진행한다.
# 우선순위 관리 -> 각 플레이어 index에 맞게 리스트를 만들어 순차탐색 하는 방향으로 가자.
# if 갈 길이 없으면 주위 우선순위 기반 독점계약 땅으로 이동. 이것도 잘 처리하기
# 같은 칸에 있으면 게임에서 사라짐. 사라지면 계약한 땅은? 예제 보니까 남아있긴 하네.
# 게임이 안끝나는 경우는 없나? 있다. 1000 이상 -1 처리

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 좌표를 반환하는 함수
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def simulate():
    global pos_to_idx
    new_dict = dict()
    for curr_row, curr_col in pos_to_idx:
        player_idx = pos_to_idx[(curr_row, curr_col)]
        # 1-1. 비어있는 공간 찾기.
        for next_dir in priority_info[player_idx][dir_info[player_idx]]:
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
            # 만약 격자 밖이면 pass
            if not in_range(next_row, next_col):
                continue
            # 격자 안 + 계약 종료 지점 or 계약 시작 안한 지점(-1로 초기화 했음) 이면 빈칸이므로 이동.
            if spot_info[next_row][next_col][0] < turn:
                break
        # 1-2. 비어있는 공간을 못찾은 경우. 내 계약 칸으로 이동. (break 되지 않은 경우이다.)
        else:
            for next_dir in priority_info[player_idx][dir_info[player_idx]]:
                next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
                # 격자 밖이면 pass
                if not in_range(next_row, next_col):
                    continue
                # 만약 내 땅이면 break
                if spot_info[next_row][next_col][1] == player_idx:
                    break

        # 2. 적절하게 정보 업데이트 해주기. 빈 칸이거나 내 땅이거나 무조건 둘 중 하나이므로
        # 그냥 가져다가 쓰면 된다.
        dir_info[player_idx] = next_dir
        idx_to_pos[player_idx] = (next_row, next_col)
        new_dict[(next_row, next_col)] = min(new_dict.get((next_row, next_col), 99999), player_idx)

    # 3. 남은 사람 기준 계약 진행.
    for row, col in new_dict:
        spot_info[row][col] = (turn+K, new_dict[(row, col)])

    # 4. 업데이트 사항 반영
    pos_to_idx = new_dict


# def custom_print():
#     print(f'-------pos_info--------')
#     for row in range(N):
#         for col in range(N):
#             if (row, col) in pos_to_idx:
#                 print(pos_to_idx[(row, col)], end=' ')
#             else:
#                 print(0, end=' ')
#         print()
#     print(f'-------spot_info---------')
#     for row in spot_info:
#         print(*row)
#     print(f'-------player_info--------')
#     for k in sorted(idx_to_pos):
#         print(f'key:{k}, pos:{idx_to_pos[k]}')
#         print(f'dir:{dir_info[k]}')


N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dir_info = [None] + list(map(lambda x: int(x)-1, input().split()))

idx_to_pos = dict()                             # idx_to_pos[idx] : idx 번호 플레이어가 가진 위치를 저장
pos_to_idx = dict()                             # pos_to_idx[(row, col)] : 해당 위치에 있는 플레이어 저장
spot_info = [[(-1, -1)] * N for _ in range(N)]  # 계약 정보를 저장할 grid. (유효 마감일, 계약자) 형태로 저장.
for row in range(N):
    for col in range(N):
        if grid[row][col]:
            idx_to_pos[grid[row][col]] = (row, col)
            pos_to_idx[(row, col)] = grid[row][col]
            spot_info[row][col] = (K, grid[row][col])

# 우선 순위를 저장할 변수
priority_info = [None]
for _ in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(lambda x: int(x)-1, input().split())))
    priority_info.append(temp)

# 실행부
answer = -1
for turn in range(1, 1001):
    # 시뮬레이션 진행.
    simulate()

    # 종료 체크
    if len(pos_to_idx) == 1:
        answer = turn
        break

# 정답 출력
print(answer)