from collections import deque
from heapq import heappush, heappop

def find_bomb_group():
    group = [[0] * n for _ in range(n)]
    group_num = 0
    hq = []

    for i in range(n):
        for j in range(n):
            # 그룹 배정 안 된 색깔 있는 돌을 찾으면 bfs 진행 (빨간색 제외)
            if arr[i][j] > 0 and group[i][j] == 0:

                group_color = arr[i][j]
                group_num += 1
                group_cnt = 1 # 그룹 크기
                red_cnt = 0 # 빨간 폭탄 개수
                red_lst = [] # 빨간 폭탄 좌표
                new_hq = []
                heappush(new_hq, (-i, j)) # 기준점 후보

                # bfs
                q = deque([[i, j]])
                group[i][j] = group_num

                while q:
                    ci, cj = q.popleft()

                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni = ci + di
                        nj = cj + dj

                        # 범위내, 그룹 배정 안됐고, 같은 색이거나 빨간색이면
                        if 0 <= ni < n and 0 <= nj < n and group[ni][nj] == 0 and (arr[ni][nj] == group_color or arr[ni][nj] == -2): # or 쓸 때 괄호 까먹지 말자...

                            group_cnt += 1 # 그룹 크기 업데이트
                            q.append([ni, nj])
                            group[ni][nj] = group_num  # 그룹 번호 배정 (빨간색도 일단 해줘야 된다... 안그러면 무한루프돈다...)

                            # 빨간색이면 개수 업데이트
                            if arr[ni][nj] == -2:
                                red_cnt += 1
                                red_lst.append([ni, nj]) # i, j를 쓰고 앉아있니

                            # 다른 색이면 기준점 후보로 넣어둠
                            else:
                                heappush(new_hq, (-ni, nj))

                # 빨간색은 또 그룹 만드는 데 쓰일 수 있으니까 0으로 만들어주기
                if red_lst:
                    for ri, rj in red_lst:
                        group[ri][rj] = 0

                # 한개짜리 그룹이면 넘어감
                if group_cnt == 1:
                    continue

                # 기준점 힙팝
                ki, kj = heappop(new_hq)
                ki = ki * (-1)

                # 두개 이상이면, 힙큐에 (그룹 크기 큰순, 빨간 폭탄 개수 작은순, 기준점 행 큰순, 기준점 열 작은순) 저장
                heappush(hq, (-group_cnt, red_cnt, -ki, kj))

    # 힙큐가 비었으면... 2 이상 그룹 없는 거임
    if not hq:
        return None

    else:
        group_cnt, _, ki, kj = heappop(hq)
        group_cnt = group_cnt * (-1)
        ki = ki * (-1)

        return group_cnt, ki, kj

def remove_bomb_group(i, j):
    group_color = arr[i][j]

    q = deque([[i, j]])

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci + di
            nj = cj + dj

            if 0 <= ni < n and 0 <= nj < n and (arr[ni][nj] == group_color or arr[ni][nj] == -2):
                arr[ni][nj] = 0
                q.append([ni, nj])

def apply_gravity(arr):
    narr = [[0] * n for _ in range(n)]

    for j in range(n):
        lst = []
        zero_cnt = 0

        for i in range(n - 1, -1, -1):
            # 돌도 아니고 빈칸도 아니다
            if arr[i][j] != -1 and arr[i][j] != 0:
                lst.append(arr[i][j])
            # 빈칸이다
            if arr[i][j] == 0:
                zero_cnt += 1
            # 돌이다
            if arr[i][j] == -1:
                if zero_cnt > 0:
                    lst.extend([0] * zero_cnt)
                lst.append(-1)
                zero_cnt = 0

        for i in range(n - len(lst)):
            lst.append(0)

        x = 0
        for i in range(n - 1, -1, -1):
            narr[i][j] = lst[x]
            x += 1

    return narr

def apply_spin(arr):
    narr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            narr[i][j] = arr[j][n - i - 1]

    return narr

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 빨간 폭탄은 -2로 저장하자... 0은 빈칸
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = -2

score = 0

while True:
    # [1] 제거할 폭탄 묶음 찾기
    result = find_bomb_group()

    # 리턴값 없으면 종료
    if result is None:
        break

    # 제거할 폭탄 개수, 기준점 리턴받기
    group_cnt, ki, kj = result

    # [2] 선택된 폭탄 묶음 제거, 점수 업데이트
    remove_bomb_group(ki, kj)
    score += group_cnt ** 2

    # [3] 중력 작용
    arr = apply_gravity(arr)

    # [4] 반시계방향 회전
    arr = apply_spin(arr)

    # [5] 중력 작용
    arr = apply_gravity(arr)

print(score)

