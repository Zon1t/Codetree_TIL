from collections import deque

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def custom_print(title):
    if debug:
        print(f'========{title}========')
        print(test, '번째')
        print('현재 먼지')
        for i in range(n):
            for j in range(n):
                val = room[i][j]
                print(f'{val:2d}', end = ' ')
            print()
        print('현재 청소기')
        for i in range(n):
            for j in range(n):
                val = vacuum[i][j]
                print(f'{val:2d}', end = ' ')
            print()
        print(vloc)

def vacuum_move():
    for num in range(1, k + 1):
        si, sj = vloc[num]

        # 청소기 기존 위치에 이미 먼지가 있는 경우
        if room[si][sj] > 0:
            continue # 아 리턴 아니야!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

        visited = [[0] * n for _ in range(n)]
        visited[si][sj] = 1
        q = deque([[si, sj]])
        closest = (INF, INF) # 행 최소, 열 최소
        found = False

        while q:
            for _ in range(len(q)):
                ci, cj = q.popleft()

                for d in range(4):
                    ni = ci + di[d]
                    nj = cj + dj[d]

                    # 범위내, 미방문, 물건 칸 아님, 청소기 칸 아님
                    if in_range(ni, nj) and visited[ni][nj] == 0 and room[ni][nj] != -1 and vacuum[ni][nj] != -1:
                        visited[ni][nj] = 1
                        q.append([ni, nj])

                        # 먼지 있는 칸
                        if room[ni][nj] > 0:
                            found = True
                            closest = min(closest, (ni, nj))

            if found:
                nni, nnj = closest
                # 청소기 좌표 업데이트
                vloc[num] = [nni, nnj]
                vacuum[si][sj] = 0
                vacuum[nni][nnj] = -1
                break # break 걸어!!!

def vacuum_clean():
    for num in range(1, k + 1):
        ci, cj = vloc[num]
        max_dust = 0
        max_d = -1

        for d in range(4):
            dust = 0
            for di, dj in rel[d]:
                ni = ci + di
                nj = cj + dj

                # 범위내, 먼지 있는 칸
                if in_range(ni, nj) and room[ni][nj] > 0:
                    dust += min(room[ni][nj], 20) # 최대 20만큼만

            if dust > max_dust:
                max_dust = dust
                max_d = d

        # 어디로 가도 청소 하나도 못하는 경우
        if max_dust == 0:
            continue

        # 최대로 청소할 수 있는 방향으로 먼지 청소
        for di, dj in rel[max_d]:
            ni = ci + di
            nj = cj + dj

            # 범위내, 먼지 있는 칸
            if in_range(ni, nj) and room[ni][nj] > 0:
                room[ni][nj] -= min(room[ni][nj], 20) # 최대 20만큼만

def add_dust():
    for i in range(n):
        for j in range(n):
            if room[i][j] > 0:
                room[i][j] += 5

def spread_dust():
    spread = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if room[i][j] != 0: # 청소기 있는 곳은 확산 되는 것 같은데...
                continue

            dust = 0
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if in_range(ni, nj) and room[ni][nj] > 0:
                    dust += room[ni][nj]

            spread[i][j] += dust // 10

    for i in range(n):
        for j in range(n):
            room[i][j] += spread[i][j]

def calc_dust():
    total_dust = 0

    for i in range(n):
        for j in range(n):
            if room[i][j] <= 0:
                continue
            total_dust += room[i][j]

    return total_dust

# ========================================================
# 세팅
n, k, l = map(int, input().split())
# -1: 물건, 0 이상: 먼지 양
room = [list(map(int, input().split())) for _ in range(n)]
# -1: 청소기 있음, 0: 없음
vacuum = [[0] * n for _ in range(n)]
vloc = [[]] # 각 청소기 좌표

for num in range(1, k + 1):
    r, c = map(lambda x: int(x) - 1, input().split())
    vacuum[r][c] = -1
    vloc.append([r, c])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
rel = [[[0, 0], [-1, 0], [1, 0], [0, 1]],
       [[0, 0], [0, 1], [0, -1], [1, 0]],
       [[0, 0], [-1, 0], [1, 0], [0, -1]],
       [[0, 0], [0, 1], [0, -1], [-1, 0]]]

INF = float('inf')
debug = False

# ========================================================
# 실행부

for test in range(1, l + 1):
    # [1] 청소기 이동
    vacuum_move()
    custom_print('청소기 이동했습니다.')

    # [2] 먼지 청소
    vacuum_clean()
    custom_print('먼지 청소했습니다.')

    # [3] 먼지 추가
    add_dust()
    custom_print('먼지 추가했습니다.')

    # [4] 먼지 확산
    spread_dust()
    custom_print('먼지 확산했습니다.')

    # [5] 먼지 양 계산
    total_dust = calc_dust()
    print(total_dust)
