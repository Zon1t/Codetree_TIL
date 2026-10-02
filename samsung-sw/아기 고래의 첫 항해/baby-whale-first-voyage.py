''' 아기 고래의 첫 항해 / 20261002 / 체감 난이도 : 골드 4~5
소요 시간 : 119분 / 시도 : 1회 / 실행 시간 : 122ms / 메모리 : 20MB

타임 라인 : 구상(18분) - 구현(30분) - 검증(71분)


[구상]
    - 0-based 좌표를 사용하고자 해서 세팅을 하다가, 장애물이 있기도 하고 정답 출력할 때에 불편
    할 것으로 예상되어 그냥 grid를 padding해 사용하게 되었다.
    - 인접 탐색에 대한 델타 배열을 만들까 고민하다가 그냥 dr, dc 세팅을 우선 순위(좌 하 우 상
    에 맞게 두고 delta_dir을 활용하게 되었다. 초기에는 입력에 의거한 상 하 좌 우 세팅이였다.
    - 나머지는 구현할 때에 문제 없이 잘 구현할 수 있을 것이라 판단하여 넘어갔다.

[구현]
    - 변수명을 헷갈렸던 것 같다. 초기에 whale_row, whale_col이 아닌 curr_row, curr_col을
    사용했었는데, 이를 bfs 노드 뽑으면서 curr_row, curr_col을 쓰다보니 헷갈렸었다. 전체적으로
    whale_row, whale_col로 수정을 진행했고 원활하게 수행하였으나, 이후 코드를 짜는 과정에서
    whale_row, whale_col을 curr_row, curr_col로 자꾸 적어버리는 실수를 범했다. 'curr_'은
    bfs 내부에서만, 혹은 하나의 객체 좌표에 대해서 다룰 때만 써야겠다.
    - 이외에는 어려웠던 부분이 없었던 것 같다. 근데 대상을 찾고 곧바로 고래의 방향을 결정지을 수
    있는가에 대해서 많이 고민했던 것 같다.

[검증]
    - 'ㅁ' 한자 키로 특수 문자를 활용해 고래를 격자에 표현해보았다. 방향 관련된 문제는 직관적으로
    보기 좋은 것 같다.
    - 49짜리 큰 테케에서도 원활하게 돌아가는지 확인했고, 문제 / 주석 / 코드를 반복적으로 읽으며
    이상한 부분은 없는지 체크해보았다.
'''

# 아기 고래가 갈 수 있는 모든 바다를 방문하는 것이 목적.

# 1. 인접 탐험. 인접한 칸에 대해서 방문하지 않은 바다가 있는 경우 해당 바다 탐색.
#       - 우선 순위. 직진 - 좌회전 - 우회전 - 180도
#       - 이동한 방향으로 바라보는 방향이 갱신됨에 유의하자!
#       - 해당 과정을 인접한 칸에 방문 가능한 바다가 없을 때까지 반복

# 2. 가장 가까운 바다로 이동. 인접 탐험이 불가한 경우 진행한다.
#       - 최소 이동 횟수를 기준으로 삼는다.
#       - 가장 가까운 칸이 여러개면 행작 - 열작 우선순위
#       - 이 때에도 좌 하 우 상 우선순위에 의거하여 이동. 마지막 바라보는 방향이 중요하다.
#       - 이거 마지막 칸만 확인하면 되는 것 같은.. 그런 묘수 있을 것 같긴 한데 그냥 가자.

# 1단계부터 다시 반복. 시키는대로 잘해보자.


from collections import deque

#    좌  하  우  상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
dir_dict = {1: 3, 2: 1, 3: 0, 4: 2}
for_debug = ['←', '↓', '→', '↑']

# 직진, 좌회전, 우회전, 180도
delta_lst = [0, 1, -1, 2]


def adj_move():
    global whale_row, whale_col, whale_dir
    for delta_dir in delta_lst:
        next_dir = (whale_dir + delta_dir) % 4
        next_row, next_col = whale_row + dr[next_dir], whale_col + dc[next_dir]

        if grid[next_row][next_col] or visited[next_row][next_col]:
            continue

        whale_row, whale_col, whale_dir = next_row, next_col, next_dir
        visited[whale_row][whale_col] = True
        answer.append((whale_row, whale_col))
        return True

    return False


def find_next():
    global whale_row, whale_col, whale_dir

    dist_grid = [[-1] * (N+2) for _ in range(N+2)]
    dist_grid[whale_row][whale_col] = 0

    find = (N+2, N+2, 0)
    Q = deque([(whale_row, whale_col, whale_dir)])
    while Q:
        for _ in range(len(Q)):
            curr_row, curr_col, curr_dir = Q.popleft()

            for d in range(4):
                next_row, next_col = curr_row + dr[d], curr_col + dc[d]

                if grid[next_row][next_col] or dist_grid[next_row][next_col] != -1:
                    continue

                dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
                Q.append((next_row, next_col, d))

                if not visited[next_row][next_col]:
                    find = min(find, (next_row, next_col, d))

        if find[0] != N+2:
            whale_row, whale_col, whale_dir = find
            visited[whale_row][whale_col] = True
            answer.append((whale_row, whale_col))
            return True

    return False


def print_grid():
    print(f'----grid----')
    temp_grid = [row[:] for row in grid]
    temp_grid[whale_row][whale_col] = for_debug[whale_dir]
    for row in temp_grid:
        print(*row)
    print()


# ==============================================================
# 세팅

N, whale_row, whale_col, whale_dir = map(int, input().split())
whale_dir = dir_dict[whale_dir]

# 좌표 기록의 편의를 위함.
grid = [[1] * (N+2)] + \
       [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + \
       [[1] * (N+2)]

visited = [[False] * (N+2) for _ in range(N+2)]
visited[whale_row][whale_col] = True

answer = [(whale_row, whale_col)]

# ===============================================================
# 실행부

while True:
    # 1. 인접 탐험.
    while adj_move():
        continue

    # 2. 가장 가까운 바다 이동.
    if not find_next():
        break

# 정답 출력
print('\n'.join([' '.join(map(str, pos)) for pos in answer]))