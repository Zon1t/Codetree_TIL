''' 루돌프의 반란 / 20260916 / 체감 난이도 : 골드 2
소요 시간 : 75분 / 시도 : 1회 / 실행 시간 : 92ms / 메모리 : 19MB

타임 라인 : 구상(18분) - 구현(45분) - 검증(12분)


[구상]
    - 아주 디테일하게 설계하진 않았지만 대략적인 방향성이라던가, 주의사항 등 잘 정리하고 넘어간 것
    같다. 틀 짜면서도 변수 필요 여부나 더 나은 방식에 대해서 고민했고 수정을 계속 해보았다.
    - 아쉬운 점은 delta 세팅할 때 한 번에 하는 거 라던가, 굳이 아웃된 산타들 카운트하진 않아도
    괜찮았다는 거.. 나머지 수정한 부분은 미리 생각하기에는 어렵거나 그냥 구현 단계에서 수정하는 것
    이 효율적인 부분이었다고 생각한다.

[구현]
    - 움직임 로직 구현 이후 바로 검증하고자 계획했었는데, 까맣게 잊어버리고 충돌 부분을 구현하던
    도중 이동 로직 검증을 깜빡해서 바로 중단하고 검증을 진행했다. 부등호 방향을 잘못하는 등 이슈
    가 있긴 했는데 곧 바로 찾아내서 수정할 수 있었다.
    - 업데이트 부분을 너무 분산해뒀나 생각이 들었다. santa에 대한 데이터를 grid, lst 두 방식
    으로 저장을 하는데, 이동만 한 지점/밀쳐난 지점/상호작용 하는 지점 이렇게 나뉘다 보니 업데이트
    를 올바르게 적용했는지 검증하는 것에 좀 시간을 쓴 건 같다.

[검증]
    - custom_print 정의한 것을 바탕으로 쭉 찍어보았다. 중간에 밀려난 로직이 이상하게 적용됨을
    발견할 수 있었는데 산타가 자체적으로 밀려날 때, 루돌프 기준이 아닌 현 지점을 기준으로 밀려났
    었다. 이를 수정하니 예제 설명은 모두 맞게 출력됨을 확인했다.
    - 문제에서 요구하는 부분들을 재차 확인하고, 내가 이동해가며 남겼던 주석들을 확인하며 재차 검
    증을 진행했다. 걸릴만한 부분이 있다면 예제에서 걸렸겠지 생각했었지만, 최근 너무 많이 틀렸어서
    꾹 참고 검증한 뒤에 제출했다.
'''

# 굉장히 귀찮은 문제이다. 1. 구성에 의거 get_dist 함수를 따로 선언하자.
# 2. 우선 순위에 의거해서 산타를 찾자. 이때 중요한 점은 거리가 우리가 생각하는 거리가 아니라는 것.
# -> 즉 단순 bfs로 찾아야 하는 부분이 절대 아니라는 것이다.
# + 8방향 처리 잘해주기.
# 3. 1~P번 순서대로 move 처리. 이동 로직을 적절하게 구성해 이동할 수 있고 없고를 정확하게 판단하자.
# 4. 2, 3번 과정에서의 충돌 처리를 잘하자. 점수 업뎃 + 밀려난 위치 잘 판단하기.
# 5. 상호작용도 함수 맞게끔 세팅
# 6. 기절은 따로 변수 만들어서 관리
# 7. 조기 종료 처리 적절하게 잘하면 문제 없을 듯??
# 거리 연산 등 그냥 순회하면서 찾아보자. 그러면 될 듯?
# 클래스 쓰고 싶다..


dr = [-1, 0, 1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, 1, -1]

INF = float('inf')


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2


def gorani_move():
    global gorani_row, gorani_col

    # 타겟 산타 찾기.
    target = (INF, INF, INF)
    for idx in range(P):
        if santa_out[idx]:
            continue

        curr_dist = get_dist((gorani_row, gorani_col), santa_lst[idx])
        santa_row, santa_col = santa_lst[idx]
        curr_status = (curr_dist, -santa_row, -santa_col)

        if curr_status < target:
            target = curr_status

    # 해당 대상으로 이동하기 위해 최단 거리 찾기
    min_dist, next_dir = INF, -1
    for d in range(8):
        next_row, next_col = gorani_row + dr[d], gorani_col + dc[d]

        if not in_range(next_row, next_col):
            continue

        next_dist = get_dist((next_row, next_col), (-target[1], -target[2]))
        if next_dist < min_dist:
            min_dist, next_dir = next_dist, d

    # 고라니 정보 업데이트 + 충돌 확인
    gorani_row, gorani_col = gorani_row + dr[next_dir], gorani_col + dc[next_dir]
    if santa_grid[gorani_row][gorani_col] != -1:
        gorani_accident(santa_grid[gorani_row][gorani_col], next_dir)


def gorani_accident(santa_idx, d):
    # 충돌 처리
    santa_row, santa_col = santa_lst[santa_idx]
    santa_grid[santa_row][santa_col] = -1
    scores[santa_idx] += C
    sturn[santa_idx] = turn+2

    # 낙하 지점 확인. 분기문 적절하게 작성.
    next_row, next_col = santa_row + dr[d]*C, santa_col + dc[d]*C
    interaction(santa_idx, next_row, next_col, d)


def santa_move(idx):
    curr_row, curr_col = santa_lst[idx]
    santa_grid[curr_row][curr_col] = -1

    # 우선 순위에 의거한 이동 방향 찾기
    min_dist, next_dir = get_dist((gorani_row, gorani_col), (curr_row, curr_col)), -1
    for d in range(4):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col) or santa_grid[next_row][next_col] != -1:
            continue
        next_dist = get_dist((gorani_row, gorani_col), (next_row, next_col))
        if next_dist < min_dist:
            min_dist, next_dir = next_dist, d

    # 이동할 수 없는 경우
    if next_dir == -1:
        santa_grid[curr_row][curr_col] = idx
        return

    # 이동 지점에 대한 충돌 여부 확인.
    curr_row, curr_col = curr_row+dr[next_dir], curr_col+dc[next_dir]
    if curr_row == gorani_row and curr_col == gorani_col:
        santa_accident(idx, next_dir)
    else:
        santa_grid[curr_row][curr_col] = idx
        santa_lst[idx] = (curr_row, curr_col)


def santa_accident(santa_idx, d):
    # 충돌 처리
    santa_row, santa_col = santa_lst[santa_idx]
    santa_grid[santa_row][santa_col] = -1
    scores[santa_idx] += D
    sturn[santa_idx] = turn+2

    # 낙하 지점에 의거한 분기문 처리
    next_row, next_col = santa_row - dr[d]*(D-1), santa_col - dc[d]*(D-1)
    interaction(santa_idx, next_row, next_col, (d+2)%4)


def interaction(attack_idx, row, col, direction):
    # 격자 밖이면 아웃처리
    if not in_range(row, col):
        santa_out[attack_idx] = True
        return

    # 밀침 대상 확인 및 정보 업데이트.
    pushed_santa = santa_grid[row][col]
    santa_grid[row][col] = attack_idx
    santa_lst[attack_idx] = (row, col)

    # 비어있으면 그냥 안착
    if pushed_santa == -1:
        return

    # 밀쳐지는 지점에 따른 적절한 분기문 처리.
    next_row, next_col = row + dr[direction], col + dc[direction]
    interaction(pushed_santa, next_row, next_col, direction)


def custom_print():
    print(f'----grid----')
    for row in range(N):
        for col in range(N):
            if row == gorani_row and col == gorani_col:
                print('G', end=' ')
            else:
                print(santa_grid[row][col], end=' ')
        print()
    print(f'----turn:{turn}----')
    print(*scores)


# ========================================================
# 입력받기
# ========================================================

scaling = lambda x: int(x)-1
N, M, P, C, D = map(int, input().split())
gorani_row, gorani_col = map(scaling, input().split())

santa_lst = [(-1, -1)] * P
santa_grid = [[-1] * N for _ in range(N)]
for _ in range(P):
    num, santa_row, santa_col = map(scaling, input().split())
    santa_grid[santa_row][santa_col] = num
    santa_lst[num] = (santa_row, santa_col)

santa_out = [False] * P
scores = [0] * P
sturn = [0] * P

# ========================================================
# 실행부
# ========================================================

for turn in range(1, M+1):
    # 1. 루돌프 움직이기.
    gorani_move()

    # 2. 산타 움직이기.
    for idx in range(P):
        # 경기장에서 벗어난 산타 or 기절했으면 넘기기.
        if santa_out[idx] or turn < sturn[idx]:
            continue

        santa_move(idx)

    # 3. 턴 종료
    keep_going = False
    for idx in range(P):
        if santa_out[idx]:
            continue
        scores[idx] += 1
        keep_going = True

    # 종료 체크
    if not keep_going:
        break

# 정답 출력
print(*scores)