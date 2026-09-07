''' 색깔 폭탄 / 20260907 / 체감 난이도 : 골드 3
소요 시간 : 67분 / 시도 : 2회(1회차 : 틀림) / 실행 시간 : 154ms / 메모리 : 21MB

타임 라인 : 구상(17분) - 구현(31분) - 검증(9분) - 수정(10분)


[구상]
    - 가능한 폭탄 묶음을 어떻게 찾을 수 있을까에 대해서 가장 많은 고민을 했던 것 같다. 뭔가 비슷한
    문제들이 떠오르긴 하는데 마냥 똑같지도 않고 빨간색에 대한 처리가 애매하다고 생각하여, 색깔을 지
    정해주어 완탐 느낌으로 해결하고자 했다.
    - 그 밖의 로직들은 크게 문제가 될 게 없다고 생각했다.

[구현]
    - 처음엔 매 bfs 수행마다 visited_red를 만들어 빨강에 대한 방문 처리를 따로 해주어야 겠다는
    생각을 가졌다. 이렇게 하면 우선 순위 연산 때에도 len(visited_red)를 만들어 해결할 수 있어
    좋은 방식이라 생각했었다.
    - 폭탄 묶음을 찾는 로직을 수정했다. 해당 과정에서 폭발해야 하는 좌표들도 모두 담았어야 한다는
    사실을 망각했어서 갑자기 visited_red를 visited_set으로 바꿔 좌표를 담는 만행을 저질렀다.
    이러고 빨강에 대해서 따로 처리해주어야 했는데 그러지 않았다.
    - 여튼 해당 사실을 모른채 각 기능별 수행 함수를 구축하고 올바르게 작동함을 확인했다.

[검증]
    - 그냥 grid만 찍어보고, 내가 짠 코드만 재차 확인하고 제출했다. 테케의 변화 양상도 확인했고
    문제 없이 잘 돌아간다고 생각했었다.
    - 루틴대로 안하고 그냥 제출해버렸다. 에지나 그렇다고 판단할 부분이 없다고 생각했기 때문이다.

[수정]
    - 문제를 읽자마자 아차 싶었다. visited_red를 다른 용도로 변수명을 바꿔 재사용한 것이 생각
    났기 때문이다. 해당 부분으로 가서 곧바로 수정하고, 다시 문제 정독하고, 제출했다.

* 피드백
    - 루틴 잘 지켜라
'''
# 가면 갈수록 문제가 이상한 것 같다. 맨정신인 것 같은데 이해가 잘 안 된다. 잘 읽고 풀어보자.
# 1. 가장 큰 폭탄 묶음 찾기. 모두 같은 색 or 빨강 포함 2색. 상하좌우 인접해 있어야 함.(중요)
# -> 이걸 어떻게 수행할 수 있을까? 빨간색 폭탄이 징검다리 역할도 가능..? 그럴 것 같다.
# -> 색칠을 해가면서 판단하는 것이 가장 좋아 보인다. 예술성이랑 비슷?하게 풀 수 있을지도
# 2. 우선 순위 잘 따지기. 큰 폭탄 중 빨간 폭탄이 가장 적은 것. 빨강 제외 행 큰, 열 작.
# 3. 폭탄 제거 후 중력 적용.. 이건 뭐 쉬울 것 같다.
# 4. 반 시계 돌리기.. 가지가지한다.
# 5. 중력 재적용.
# 차근차근 위 기능을 수행하는 함수들을 잘 짜보자.


from collections import deque

# 델타 세팅
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 범위 안 벗어나는지 체크
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 폭탄 묶음 확인을 위함.
def bfs(start_row, start_col, visited):
    # 기준점을 잡기 위함.
    curr_color, standard_row, standard_col = grid[start_row][start_col], start_row, start_col
    visited[start_row][start_col] = True

    # 얘는 반환할거임.
    visit_set = set()                       # visited_red -> visited_set으로 변하는 과정에서 빨강을 안셌다;
    visit_set.add((start_row, start_col))
    red_cnt = 0

    # 탐색 진행.
    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            # 범위 밖에 있거나, 이미 방문한 칸, 빈칸/돌에 대해서는 탐색X.
            if not in_range(next_row, next_col):
                continue
            if (next_row, next_col) in visit_set or grid[next_row][next_col] < 0:
                continue

            # 만약 빨강이면 카운트해주고 append. 이때 visited는 업뎃X. visited_set만 방문처리.
            if grid[next_row][next_col] == 0:
                visit_set.add((next_row, next_col))
                red_cnt += 1
                Q.append((next_row, next_col))
            # 같은 색상에 대해서는 visited처리까지..
            elif grid[next_row][next_col] == curr_color:
                visited[next_row][next_col] = True
                visit_set.add((next_row, next_col))
                Q.append((next_row, next_col))

                # 기준점 업데이트
                if (-next_row, next_col) < (-standard_row, standard_col):
                    standard_row, standard_col = next_row, next_col

    # 필요 변수 반환
    return visit_set, len(visit_set), standard_row, standard_col, red_cnt

# 최소 2개 이상의 칸으로 이루어져야 함.
def find():
    global answer
    visited = [[False] * N for _ in range(N)]

    # 변수 초기화.
    target_set, curr_cnt, curr_row, curr_col, curr_red = set(), 0, -1, N, N*N
    for row in range(N):
        for col in range(N):
            # 빈칸, 돌, 빨강은 탐색 시작점이 될 수 없다.
            if visited[row][col] or grid[row][col] < 1:
                continue

            # 해당 점을 시작으로 탐색 진행.
            bomb_set, cnt, standard_row, standard_col, red_cnt = bfs(row, col, visited)
            # 묶음의 정의에 의거.
            if cnt < 2:
                continue

            # 우선 순위에 의거. 변수 업데이트.
            if (-cnt, red_cnt, -standard_row, standard_col) < (-curr_cnt, curr_red, -curr_row, curr_col):
                target_set, curr_cnt, curr_row, curr_col, curr_red = bomb_set, cnt, standard_row, standard_col, red_cnt

    # 터뜨릴 애들이 있으면 터뜨리기.
    if target_set:
        answer += curr_cnt ** 2
        for row, col in target_set:
            grid[row][col] = -2
        return True
    else:
        return False

# 중력 적용 로직
def apply_gravity():
    for col in range(N):
        pointer = N-1
        for row in range(N-1, -1, -1):
            # 돌이면 바로 위에 얹기
            if grid[row][col] == -1:
                pointer = row-1
            # 아니라면..
            else:
                # 빈 칸이 아닌 칸에 대해서
                if grid[row][col] != -2:
                    # 만약 떨어뜨릴 수 있다면 떨구기.
                    if pointer != row:
                        grid[row][col], grid[pointer][col] = -2, grid[row][col]
                    # 포인터 이동.
                    pointer -= 1

# 반시계 회전 로직
def rotate():
    global grid
    grid = [list(row[:]) for row in zip(*grid)][::-1]

# 찍어보자.
def print_grid():
    print()
    for row in grid:
        print(*row)

# 입력받기
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 실행부
answer = 0

# 1. 묶음 찾으면 터뜨리기.
while find():
    # 2. 중력 적용
    apply_gravity()

    # 3. 돌리기
    rotate()

    # 4. 중력 적용
    apply_gravity()

# 정답 출력
print(answer)