# 뭐 이런 문제가 다 있지 싶지만 열심히 풀어보자.
# 1. 격자에 대해서 조화로움 값 연산 로직을 구성하자.
# 2. 회전 로직을 구성하자. 헷갈리니까 십자, 사각형 나눠서 구현
# 점수 연산 -> 회전 -> 점수 연산 -> 회전 -> 점수 연산 -> 정답 출력

# 조화 점수에 대한 생각을 해볼 필요가 있다.
# 그룹 나누기 -> 색칠하기 문제처럼 해볼까? 색칠하기 -> 맞닿은 부분 연산하기 -> 데이터 업데이트.
# 매번 matrix를 구축하면 편할 듯 싶다. N이 29.. 면 우짜냐 이거 일단 하긴 해야할듯?
# 이거 안되면 인접리스트 마냥 만들어야 할듯. adj[small_num] = (large_num, cnts) 이정도?
# 첨부터 인접으로 가자.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def take_number(start_row, start_col):
    numbers[start_row][start_col] = curr_num
    info = dict()
    cnt = 0

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()
        cnt += 1
        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if numbers[next_row][next_col]:
                if numbers[next_row][next_col] != curr_num:
                    info[numbers[next_row][next_col]] = info.get(numbers[next_row][next_col], 0) + 1
                continue
            if grid[curr_row][curr_col] != grid[next_row][next_col]:
                continue
            numbers[next_row][next_col] = curr_num
            Q.append((next_row, next_col))

    return cnt, info

def rotate_center():
    for k in range(1, center+1):
        temp = grid[center-k][center]
        grid[center-k][center] = grid[center][center+k]
        grid[center][center+k] = grid[center+k][center]
        grid[center+k][center] = grid[center][center-k]
        grid[center][center-k] = temp


def rotate_side(sr, sc):
    temp = [row[sc:sc+center] for row in grid[sr:sr+center]]
    temp = [row[::-1] for row in zip(*temp)]
    for row in range(center):
        for col in range(center):
            grid[sr+row][sc+col] = temp[row][col]

def print_grid():
    print(f'------------{i + 1}------------')
    for row in grid:
        print(*row)

N = int(input())
center = N >> 1
grid = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(4):
    # 1. 색칠하기
    numbers = [[0]*N for _ in range(N)]
    cnts, number_dict = [None], dict()
    curr_num = 1
    for row in range(N):
        for col in range(N):
            if numbers[row][col]:
                continue

            # 색칠하고 정보 저장.
            cnt, info = take_number(row, col)
            number_dict[curr_num] = grid[row][col]
            cnts.append(cnt)

            # 점수 더해주기
            for color, line_cnt in info.items():
                this_number, this_count = number_dict[color], cnts[color]
                answer += (this_count + cnt) * this_number * grid[row][col] * line_cnt

            # 색칠할 색깔 변경
            curr_num += 1

    # 종료 조건
    if i == 3:
        break

    # 2-1. 십자회전
    rotate_center()

    # 2-2. 사각회전
    rotate_side(0, 0)
    rotate_side(0, center+1)
    rotate_side(center+1, 0)
    rotate_side(center+1, center+1)

# 정답 출력
print(answer)