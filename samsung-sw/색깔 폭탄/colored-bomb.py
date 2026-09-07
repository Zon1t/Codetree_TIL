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

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def bfs(start_row, start_col, visited):
    curr_color, standard_row, standard_col = grid[start_row][start_col], start_row, start_col
    visited[start_row][start_col] = True
    visit_set = set()                       # visited_red -> visited_set으로 변하는 과정에서 빨강을 안셌다;
    visit_set.add((start_row, start_col))
    red_cnt = 0
    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if (next_row, next_col) in visit_set or grid[next_row][next_col] < 0:
                continue

            if grid[next_row][next_col] == 0:
                visit_set.add((next_row, next_col))
                red_cnt += 1
                Q.append((next_row, next_col))
            elif grid[next_row][next_col] == curr_color:
                visited[next_row][next_col] = True
                visit_set.add((next_row, next_col))
                Q.append((next_row, next_col))

                if next_row > standard_row:
                    standard_row, standard_col = next_row, next_col
                elif next_row == standard_row:
                    if next_col < standard_col:
                        standard_col = next_col

    return visit_set, len(visit_set), standard_row, standard_col, red_cnt

# 최소 2개 이상의 칸으로 이루어져야 함.
def find():
    global answer
    visited = [[False] * N for _ in range(N)]
    target_set, curr_cnt, curr_row, curr_col, curr_red = set(), 0, -1, N, N*N
    for row in range(N):
        for col in range(N):
            if visited[row][col] or grid[row][col] < 1:
                continue

            bomb_set, cnt, standard_row, standard_col, red_cnt = bfs(row, col, visited)
            if cnt < 2:
                continue

            if (-cnt, red_cnt, -standard_row, standard_col) < (-curr_cnt, curr_red, -curr_row, curr_col):
                target_set, curr_cnt, curr_row, curr_col, curr_red = bomb_set, cnt, standard_row, standard_col, red_cnt
    if target_set:
        answer += curr_cnt ** 2
        for row, col in target_set:
            grid[row][col] = -2
        return True
    else:
        return False

def apply_gravity():
    for col in range(N):
        pointer = N-1
        for row in range(N-1, -1, -1):
            if grid[row][col] == -1:
                pointer = row-1
            else:
                if grid[row][col] != -2:
                    if pointer != row:
                        grid[row][col], grid[pointer][col] = -2, grid[row][col]
                    pointer -= 1


def rotate():
    global grid
    grid = [list(row[:]) for row in zip(*grid)][::-1]


def print_grid():
    print()
    for row in grid:
        print(*row)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while True:
    # 1. 폭탄묶음 찾고 제거. 터질 묶음이 없을 때까지 반복하므로, 종료 조건으로 사용
    if not find():
        break

    # 2. 중력 적용
    apply_gravity()

    # 3. 돌리기
    rotate()

    # 4. 중력 적용
    apply_gravity()

# 정답 출력
print(answer)