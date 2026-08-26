''' 회전하는 빙하 / 20260826 / 체감 난이도 : 골드 4~5
소요 시간 : 42분 / 시도 : 1회 / 실행 시간 : 363ms / 메모리 : 25MB

타임 라인 : 구상(10분) - 구현(27분) - 검증(5분)


[구상]
    - 배열 회전, 구역 나누기, 얼음(치즈) 녹이기 등 너무나 익숙한 기능들의 연속이라 쉽게 풀 수 있을 것이라
    생각이 들었다.
    - 배열 회전이 아주 일반적인 회전이 아니라는 점, 해당 과정에서 어떻게 최적화할 수 있을까에 대한 고민 이후
    문제 풀이를 시작하였다.

[구현]
    - rotate 로직을 재차 검증하면서, 아마 가장 많은 시간을 쏟은 것 같다. 덕분에 한 번에 정상 동작하는 rotate
    함수를 얻을 수 있었다.
    - 짜잘한 실수가 있었다. 반환 순서, d range 범위 정도인데 곧바로 실수를 발견해 수정할 수 있었다.

[검증]
    - 구현 과정에서 계속 실행시켜보고, 예제와 결과 비교, 로직 반영하는 과정에서 빼먹은 게 없는지 등등 체크했었기에,
    빙하가 없어지는 경우에 대해서만 에지케이스를 만들어보고 정상 동작하는지 확인해보았다.
'''

# 회전에 대한 정의 잘 따지기. 만약 L이 주어지면 2^(n-L)만큼 row, col 반복하여
# 2^(L-1) size만큼 잘라 회전한다. 이는 구현이 크게 어렵진 않을 것 같다.
# -> 이후 완탐을 진행하여 녹일 수 있는 얼음은 1씩 녹인다.
# -> "회전이 모두 끝나면" bfs를 진행하여 가장 큰 얼음 군집 크기, 빙하의 총 양 연산

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def rotate(level):
    if level == 0:
        return

    chunk = 1 << level
    rotate_size = 1 << (level-1)

    for sr in range(0, N, chunk):
        for sc in range(0, N, chunk):
            for row in range(sr, sr+rotate_size):
                for col in range(sc, sc+rotate_size):
                    temp = grid[row][col]
                    # 좌하단 -> 좌상단
                    grid[row][col] = grid[row+rotate_size][col]
                    # 우하단 -> 좌하단
                    grid[row+rotate_size][col] = grid[row+rotate_size][col+rotate_size]
                    # 우상단 -> 우하단
                    grid[row+rotate_size][col+rotate_size] = grid[row][col+rotate_size]
                    # 좌상단 -> 우상단
                    grid[row][col+rotate_size] = temp

def cry():
    to_water = set()

    for row in range(N):
        for col in range(N):

            # 빼먹을 뻔 했던 부분
            if not grid[row][col]:
                continue

            cnt = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col) or grid[next_row][next_col] == 0:
                    cnt += 1
            if cnt >= 2:
                to_water.add((row, col))

    # 얼음 녹는 것은 동시에 진행.
    for row, col in to_water:
        grid[row][col] -= 1

def bfs(sr, sc, visited):
    Q.clear()

    cnt = 0
    Q.append((sr, sc))
    while Q:
        curr_row, curr_col = Q.popleft()
        cnt += 1

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or visited[next_row][next_col] or not grid[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            Q.append((next_row, next_col))

    return cnt

def calc_answer():

    visited = [[False] * N for _ in range(N)]
    max_cnt = 0

    for row in range(N):
        for col in range(N):

            if visited[row][col] or not grid[row][col]:
                continue

            visited[row][col] = True
            cnt = bfs(row, col, visited)

            if max_cnt < cnt:
                max_cnt = cnt

    total = sum([sum(row) for row in grid])
    return total, max_cnt

n, q = map(int, input().split())
N = 1 << n
Q = deque()

grid = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

for level in commands:
    # 1. 회전시키기
    rotate(level)

    # 2. 빙하 녹이기
    cry()

# 3. 정답 연산하기
answer1, answer2 = calc_answer()

# 출력 형식에 맞게 출력하기*
print(answer1)
print(answer2)