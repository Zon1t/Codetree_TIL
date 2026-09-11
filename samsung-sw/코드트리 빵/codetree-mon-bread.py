''' 코드트리 빵 / 20260911 / 체감 난이도 : 플레 5 ~ 골드 1
소요 시간 : 70분 / 시도 : 1회 / 실행 시간 : 63ms / 메모리 : 16MB

타임 라인 : 구상(22분) - 구현(35분) - 검증(13분)


[구상]
    - 틀도 안 짜면서 문제만 10분 넘게 읽은 건 처음인 것 같다. 고려 사항 및 주어지는 조건들이 꽤나
    까다롭다는 생각이 들었다. 업데이트 시점 / 우선 순위의 적용 기준(현재?) 등등.. 어느 정도 정리를
    해야 구현이 가능하다고 생각해서 구상에 시간을 아끼지 않았다.
    - 최악을 상정하면 시간이 빡셀 수 있을까라는 생각이 들었기도 했지만, 이거 아니면 달리 방법이 떠
    오르지 않았기에 구현을 일단 들어가기로 마음 먹었다.

[구현]
    - 나름의 최적화를 위해 업데이트 시점을 관리했다. need_update flag를 활용하여 가지 못하는 지
    점이 생길 때만 업데이트 해주기로 했다. 이를 활용하여 각 개인의 격자를 관리하겠다고 생각하니 그
    래도 시간 초과에 대해서는 자유로울 수 있겠다 판단했다. 덕분에 꽤 많은 부분을 수정했다.
    - idx 세팅을 실수했다고 생각했다. 1번 부터 하는 편이 좋을 것이라 생각해서 쭉 이어가다가 나중에
    다시 생각해보니 그냥 0번부터 하는 게 더 편했겠다고 판단했다. 이로 인해 헷갈리는 부분들이 다소
    있었는데 이렇게 구현을 너무 많이 진행하여서 해당 세팅으로 계속 진행해버렸다.

[검증]
    - update_grid가 정상적으로 동작하지 않았다. custom_print 함수를 만들어 지속적으로 확인해보
    았다. 놓쳤던 부분은 내가 있는 위치가 다은 사람에 의해 가지 못하는 칸으로 변할 수 있는데 해당 경
    우 update_grid 과정에서 내 위치를 찾지 못하는 사태가 발생했다.
    - 수정한 뒤에는 문제 다시 읽고, 코드 다시 보고, 커스텀 프린트 다시 찍어보고 제출하게 되었다. 테
    케가 너무 단순하게 주어진 만큼 내 로직에 대해서 더 의심을 가지고 검증했던 것 같다.
'''


# 생각할 부분이 많은 문제인 듯. 천천히 읽고 들어가자.
# 격자에 있는 사람들이 모두 이동한 뒤에 이동할 수 없어짐 <- 이거 굉장히 중요한 조건이다.
# 매턴 bfs 돌려가면서 위치 찾고 넣어주고 등등.. 수행하는 거 잘하면 생각보다는? 괜찮을 것 같다.
# 움직이는 방법론에 대해서 고민을 좀 해봐야 하는데.. 개인 격자 만들어주기? 이거 생각보다 괜찮겠다.
# 사람은 많아야 30명이니 시간도 괜찮을지도.. 더 고능한 방법 없나? 일단 해보자.
# 배이스캠프 == 편의점 이건 있을 수 있나? 없다고 한다.


from collections import deque

# 주어진 대로 델타 세팅(우선순위)
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# 범위 체크
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 베이스 캠프를 찾아라!
def find_basecamp(idx):
    target_row, target_col = conb[idx]
    visited = individual_grid[idx]              # 해당 가변 객체를 수정할 것.
    visited[target_row][target_col] = 0
    
    # bfs 세팅
    find = []
    curr_dist = -1
    Q = deque([(target_row, target_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        # 평소 좋아하던 방식으로 (거리,행,열) 우선순위에 맞는 베이스 캠프 찾기
        if curr_dist != visited[curr_row][curr_col]:
            if find:
                find.sort()
                return find[0][0], find[0][1]
            curr_dist = visited[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 못 가거나 이미 간 경우 스킵
            if not in_range(next_row, next_col) or lock_grid[next_row][next_col]:
                continue
            if visited[next_row][next_col] != -1:
                continue

            # 만약 베이스 캠프면 추가!
            if grid[next_row][next_col]:
                find.append((next_row, next_col))
            
            # bfs 계속 진행..
            visited[next_row][next_col] = visited[curr_row][curr_col] + 1
            Q.append((next_row, next_col))

    # 여기까지 올 일은 없긴 하다.
    return -1, -1

# 격자 업데이트 함수. 만약 다른 사람들로 인해 못 가는 지점들이 생겼다면 개인 격자를 업데이트!
def update_grid():
    for idx in range(1, min(curr_time, M) + 1):
        
        # 이미 도착한 애는 살필 필요X
        if arrival[idx]:
            continue

        # 편의점을 시작으로 개인 격자 업데이트
        target_row, target_col = conb[idx]
        
        # 꼭 이렇게 안해도 됨. 난 visited 변수명이 너무 편해서 이렇게 사용
        visited = individual_grid[idx] = [[-1] * N for _ in range(N)]
        visited[target_row][target_col] = 0

        # bfs again.
        Q = deque([(target_row, target_col)])
        while Q:
            curr_row, curr_col = Q.popleft()

            # 내 위치 찾았으면 굳이? 더 살필 필욘 없다
            if (curr_row, curr_col) == human[idx]:
                break

            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                
                # 디버깅 하면서 발견한 부분. 내 위치가 lock된 칸 일 수도 있다!
                if not in_range(next_row, next_col) or (lock_grid[next_row][next_col] and (next_row, next_col) != human[idx]):
                    continue
                if visited[next_row][next_col] != -1:
                    continue

                visited[next_row][next_col] = visited[curr_row][curr_col] + 1
                Q.append((next_row, next_col))


# 최단거리란 항상 현재를 기준으로 하는가? 아니면 미래를 예측해서 하는가? 전자겠지?
def move():
    global need_update
    # 격자 업데이트가 필요하면 업데이트 하고 움직이자!
    if need_update:
        update_grid()
        need_update = False

    # 움직임 시작
    arrival_lst = []
    for idx in range(1, min(curr_time, M)+1):
        # 이미 도착했으면 움직일 필요 없음
        if arrival[idx]:
            continue

        # 현재 위치 받아오기
        curr_row, curr_col = human[idx]
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 격자 밖이면 스킵
            if not in_range(next_row, next_col):
                continue

            # 개인 격자 및 우선 순위에 의거하여 최단 거리로 ㄱㄱ
            if individual_grid[idx][next_row][next_col] == individual_grid[idx][curr_row][curr_col] - 1:
                
                # 만약 편의점에 도착했으면 체크하자
                if individual_grid[idx][next_row][next_col] == 0:
                    arrival_lst.append((idx, next_row, next_col))
                
                # 이동 처리 및 종료
                human[idx] = (next_row, next_col)
                break

    # 필요 값 반환
    return arrival_lst

# 열심히 찍어보자
def custom_print():
    print(f'----arrival----')
    print(*arrival[1:])
    print(f'----human----')
    print(*human[1:])
    print(f'----indiv_grid----')
    for idx in range(1, M+1):
        print(f'----{idx}----')
        for row in individual_grid[idx]:
            print(*row)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 최단 경로를 위해 각 개인에게 격자를 할당한다.
individual_grid = [[[-1] * N for _ in range(N)] for _ in range(M+1)]

lock_grid = [[0] * N for _ in range(N)]         # 가지 못하는 칸 체크를 위함.
arrival = [False] * (M+1)                       # 도착한 애들도 체크해야 함.

# index에 맞는 편의점 위치, 현재 위치를 받기 위함.
conb = [None] + [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
human = [None]

# 실행부
curr_time, visit_cnt, need_update = 0, 0, False
while True:
    # 0. 이미 다 편의점에 갔으면 종료
    if visit_cnt == M:
        break

    # 1. 격자에 사람들이 있다면 move
    cant_go = move()

    # 2. 못가는 칸 업데이트!
    for idx, row, col in cant_go:
        lock_grid[row][col] = 1
        visit_cnt += 1
        arrival[idx] = True
        need_update = True

    # 3. 베이스 캠프 배치가 가능하면 배치
    if curr_time < M:
        base_row, base_col = find_basecamp(curr_time+1)
        lock_grid[base_row][base_col] = 1
        human.append((base_row, base_col))
        need_update = True

    curr_time += 1

# 정답 출력
print(curr_time)