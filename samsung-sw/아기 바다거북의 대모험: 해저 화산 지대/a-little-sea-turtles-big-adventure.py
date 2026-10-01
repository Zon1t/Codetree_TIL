from collections import deque

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def custom_print(title):
    if debug:
        print(f'========{title}========')
        print('현재 턴수는', turns)
        print('바다 정보')
        for row in sea:
            print(*row)
        print('거북이 정보')
        print(turtle_loc)
        print('화산 정보')
        print(vinfo)
        print('답')
        print(arrival)
        print()

def bfs(si, sj, ei, ej):
    visited = [[-1] * n for _ in range(n)]
    visited[ei][ej] = 0
    q = deque([[ei, ej]])

    while q:
        found = False

        for _ in range(len(q)):
            ci, cj = q.popleft()

            if ci == si and cj == sj:
                found = True
                break

            for d in range(4):
                ni = ci + di[d]
                nj = cj + dj[d]

                # 범위내, 미방문, 지나갈 수 있는 칸
                if in_range(ni, nj) and visited[ni][nj] == -1 and sea[ni][nj] == 0:
                    visited[ni][nj] = visited[ci][cj]+1
                    q.append([ni, nj])
        if found:
            break

    # 경로가 존재하는 경우
    for d in range(4):
        ni = si + di[d]
        nj = sj + dj[d]

        if in_range(ni, nj) and visited[ni][nj] == visited[si][sj]-1:
            return ni, nj # 다음 칸 좌표 리턴

    # 경로가 존재하지 않는 경우
    return si, sj # 기존 좌표 리턴

def explosion():
    heat = [[0] * n for _ in range(n)]
    exploded = set()

    while True:
        added = False # 새로 폭발한 화산이 있었는지
        for num in range(1, k + 1):
            if num in exploded: # 이미 분출했으면 스킵
                continue

            vi, vj = vinfo[num - 1][2], vinfo[num - 1][3]
            acc_heat = vinfo[num - 1][0] + heat[vi][vj] # 현재 마그마 압력 + 누적된 열기

            if acc_heat >= vinfo[num - 1][1]: # 임계치 이상이면 분출
                added = True
                exploded.add(num)
                heat[vi][vj] += vinfo[num - 1][1]

                # dfs
                for d in range(4):
                    ci, cj = vi, vj
                    cur_heat = vinfo[num - 1][1] # 분출할 열기

                    while True:
                        cur_heat //= 2
                        ni = ci + di[d]
                        nj = cj + dj[d]

                        # 범위 밖 or 산호초 만남 or 열기 0 되면 break
                        if not in_range(ni, nj) or sea[ni][nj] == -11 or cur_heat == 0:
                            break

                        heat[ni][nj] += cur_heat
                        ci, cj = ni, nj

        # 새로 폭발한 화산이 없었다면 멈춤
        if not added:
            break

    for i in range(n):
        for j in range(n):
            # 열기 20 이상인 칸에 거북이가 있는 경우
            if heat[i][j] >= 20 and sea[i][j] > 0:
                turtle_num = sea[i][j]
                sea[i][j] = -turtle_num # 화석으로 변함
                arrival[turtle_num - 1] = -1

    return exploded

# ================================================================
# 세팅

n, m, k = map(int, input().split())
# 0: 빈 공간
# -11: 산호초
# 1 ~ 10: 살아있는 거북이
# -1 ~ -10: 화석 거북이
sea = [list(map(int, input().split())) for _ in range(n)]
turtle_loc = [] # 거북이 좌표
vinfo = [] # [마그마 압력, 임계치, i, j]

for i in range(n):
    for j in range(n):
        if sea[i][j] == 1:
            sea[i][j] = -11

for num in range(1, m + 1):
    r, c = map(int, input().split())
    sea[r][c] = num
    turtle_loc.append([r, c])

for num in range(1, k + 1):
    r, c, p = map(int, input().split())
    vinfo.append([0, p, r, c])

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

home_i, home_j = n - 1, n - 1
arrival = [0] * m
turns = 1

debug = False

# ================================================================
# 실행부

while True:
    # [1] 바다거북이 이동
    for num in range(1, m + 1):
        if arrival[num - 1] != 0: # 이미 도착/화석이 된 거북이면 스킵
            continue
        ti, tj = turtle_loc[num - 1]
        sea[ti][tj] = 0 # 기존 위치 0

        # 거북이 정보 업데이트
        ni, nj = bfs(ti, tj, home_i, home_j) # bfs 호출
        turtle_loc[num - 1] = [ni, nj] # 거북이 좌표 업데이트
        if ni == home_i and nj == home_j: # 안식처 도착
            arrival[num - 1] = turns
        else: # 도착 안 함
            sea[ni][nj] = num

    custom_print('바다거북이가 이동했어요.')

    # [2] 화산 압력 증가
    for num in range(k):
        vinfo[num][0] += 10

    # [3] 화산 분출
    exploded = explosion() # 리턴: 분출한 화산

    # [4] 분출한 화산 마그마 압력 초기화
    for num in exploded:
        vinfo[num - 1][0] = 0

    custom_print('화산 분출했어요.')

    # [5] 종료 확인
    # 1) 모두 도착 or 화석이 된 경우
    done = True
    for time in arrival:
        if time == 0:
            done = False
    if done:
        break

    # 2) 100턴 지난 경우
    turns += 1
    if turns == 101:
        for t in range(m):
            if arrival[t] == 0:
                arrival[t] = -1
        break

# [6] 출력
for t in range(m):
    print(arrival[t])
