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
            temp = [[0] * chunk for _ in range(chunk)]

            for row in range(rotate_size):
                for col in range(rotate_size):
                    # 좌상단 -> 우상단
                    temp[row][rotate_size+col] = grid[sr+row][sc+col]
                    # 우상단 -> 우하단
                    temp[rotate_size+row][rotate_size+col] = grid[sr+row][sc+rotate_size+col]
                    # 우하단 -> 좌하단
                    temp[rotate_size+row][col] = grid[sr+rotate_size+row][sc+rotate_size+col]
                    # 좌하단 -> 좌상단
                    temp[row][col] = grid[sr+rotate_size+row][sc+col]
            
            # 해당 청크 업데이트
            for row in range(chunk):
                for col in range(chunk):
                    grid[sr+row][sc+col] = temp[row][col]

def cry():
    to_water = set()

    for row in range(N):
        for col in range(N):

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

# 출력
print(answer1)
print(answer2)