''' AI 로봇청소기 / 20260930 / 체감 난이도 : 골드 4
소요 시간 : 47분 / 시도 : 1회 / 실행 시간 : 144ms / 메모리 : 20MB

타임 라인 : 구상(15분) - 구현(25분) - 검증(7분)


[구상]
    - 처음에 클래스를 세팅하다가, 그냥 함수로 하는 게 익숙해서 그런가 땡기지는 않았다. 곧바로 수정해
    서 구상을 이어나갔다.
    - 주석 부분 수정을 꽤나 많이 했던 것 같다. 격자마다 최대 20만큼 청소 가능하다는 조건을 빼먹을까
    혹시 몰라 적어주었고, 그냥 내가 착각할 만한 부분들, 문제 조건들 위주로 작성해주었다.

[구현]
    - 묘수가 이것저것 떠오르긴 했는데, 금방금방 떨쳐내고 건실한 풀이를 이어나갈 수 있었다. 이건 확실
    히 잘한 부분 같다.
    - 변수명을 나름 고민하고 넘어갔었는데 d <-> clean_d를 잘못 적는다거나, 초기 세팅에서 cleaner
    grid를 -1로 초기화를 했었는데, 해당 부분을 잊고 그냥 0으로 지워주는 등 실수가 있었다. 다행히 구
    현 과정에서 곧바로 찾아 수정할 수 있었다.
    - move를 안하는 경우를 생각 못 했었다! 격자마다 최대 20만큼만 청소 가능하다 보니, 현 위치에 먼
    지가 남아있는 경우도 분명 존재한다. 확산도 있고.. 2번 테케 디버깅 과정에서 꽤나 오랜 시간을 투자
    해 발견할 수 있었다. 예전에도 시작 지점 == 도착 지점인 문제에서 해당 부분을 놓친 적이 있었는데,
    반성해야 한다.

[검증]
    - 문제 <-> 주석 <-> 코드 과정을 계속 거쳤다. 테케 디버깅을 마친 이후기도 하고, 각 로직 별로 구
    현 때 재차 확인했어서 크게 문제될 구석은 없다고 판단했다.

* 시작하고 바로 끝나는 경우 잊지 말고 체크하기.
'''

# 전형적인 시키는거 잘하면 풀 수 있는 문제 같다. 델타 세팅해서 접근하면 될듯?
# 1. move : 가장 가까운 오염된 격자로 이동하기.
#       - 물건이 있으면 이동X
#       - 행작, 열작 + 오염된 정도는 상관 없음에 유의하자.
# 2. clean : ㅗ 모양으로 청소 가능. 바라보는 방향은 선택이 가능하다.
#       - 가장 먼지량 많은 게 우선
#       - 그 방향이 여러개인 경우 오-아-왼-위 우선순위를 가짐.
#       - 청소는 청소기마다 순서대로 진행.
#       - 격자마다 최대 20.
# 3. accumulate : 먼지 축적. 먼지가 있는 모든 격자에 5씩 추가.
# 4. spread : 먼지 확산. 인접 네 방향 먼지량 합을 10으로 나눈만큼 확산됨.
#       - 깨끗한 격자에서만 "동시" 확산
# 먼지량 합을 매턴 출력하자.


from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def move(idx):
    start_row, start_col = cleaner[idx]
    cleaner_grid[start_row][start_col] = -1

    if grid[start_row][start_col] > 0:
        return start_row, start_col

    visited = [[False] * N for _ in range(N)]
    visited[start_row][start_col] = True

    find = []
    Q = deque([(start_row, start_col)])
    while Q:
        if find:
            find.sort()
            return find[0][0], find[0][1]

        for _ in range(len(Q)):
            curr_row, curr_col = Q.popleft()
            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                    continue
                if visited[next_row][next_col] or cleaner_grid[next_row][next_col] != -1:
                    continue

                visited[next_row][next_col] = True
                Q.append((next_row, next_col))

                if grid[next_row][next_col] > 0:
                    find.append((next_row, next_col))

    # 아마 어디에도 못가면..? 이게 있나.
    return start_row, start_col


def find_dir(idx):
    curr_row, curr_col = cleaner[idx]
    curr_max, max_dir = -1, -1

    clean_lst = [min(20, grid[curr_row+dr[d]][curr_col+dc[d]]) if in_range(curr_row+dr[d], curr_col+dc[d]) and grid[curr_row+dr[d]][curr_col+dc[d]] > 0 else 0 for d in range(4)]
    for d in range(4):
        can_clean = 0
        for clean_d in range(4):
            # 등 뒤는 청소할 수 없음
            if clean_d == (d + 2) % 4:
                continue
            can_clean += clean_lst[clean_d]
            
        if curr_max < can_clean:
            curr_max = can_clean
            max_dir = d

    return max_dir


def clean(idx):
    curr_row, curr_col = cleaner[idx]
    grid[curr_row][curr_col] -= min(20, grid[curr_row][curr_col])

    clean_dir = find_dir(idx)
    for d in range(4):
        if d == (clean_dir + 2) % 4:
            continue

        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
            continue

        grid[next_row][next_col] -= min(20, grid[next_row][next_col])


def accumulate():
    for row in range(N):
        for col in range(N):
            if grid[row][col] > 0:
                grid[row][col] += 5


def spread():
    update_grid = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if grid[row][col] != 0:
                continue

            total = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                    continue
                total += grid[next_row][next_col]

            update_grid[row][col] += total // 10

    for row in range(N):
        for col in range(N):
            grid[row][col] += update_grid[row][col]


def get_answer():
    total = 0
    for row in range(N):
        for col in range(N):
            if grid[row][col] < 1:
                continue
            total += grid[row][col]
    return total


def print_grid():
    for idx in range(K):
        print(f'----idx: {idx+1}----')
        print(*cleaner[idx])
    print(f'----grid----')
    for row in grid:
        print(*row)


# =============================================================
# 세팅

N, K, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

cleaner = []
cleaner_grid = [[-1] * N for _ in range(N)]
for i in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    cleaner.append((r, c))
    cleaner_grid[r][c] = i

# ==============================================================
# 실행부

for _ in range(L):
    # 1. 청소기 움직이기.
    for idx in range(K):
        nr, nc = move(idx)
        cleaner[idx] = (nr, nc)
        cleaner_grid[nr][nc] = idx

    # 2. 청소하기.
    for idx in range(K):
        clean(idx)

    # 3. 먼지 축적
    accumulate()

    # 4. 먼지 확산.
    spread()

    # 5. 정답 출력
    print(get_answer())