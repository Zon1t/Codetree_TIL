# 좀 불친절한? 예제를 자세히 풀어서 주지 않았다. 잘 생각해서 문제를 풀어보자.
# 최단거리는 맨해튼 거리로 정의. 출구 방향으로 어쨋든 움직이긴 해야 한다.
# move -> rotate 이동은 할 때마다 answer에 넣어주는 방식으로 진햄.
# find와 같은 세부 기능 수행을 위함 함수 정의도 필요할 듯?
# N이 그렇게 크진 않음. K도 그렇고.. 시간초과? 그건 괜찮을듯?
# 위치 -> 사람, 사람 -> 위치가 가능해야 함.

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def move():
    global answer
    for idx, pos in enumerate(human):

        if arrive[idx]:
            continue

        curr_dist = get_dist(pos, EXIT)
        for d in range(4):
            next_row, next_col = pos[0] + dr[d], pos[1] + dc[d]

            if not in_range(next_row, next_col):
                continue
            if grid[next_row][next_col]:
                continue

            next_dist = get_dist((next_row, next_col), EXIT)
            if next_dist < curr_dist:

                if (next_row, next_col) == EXIT:
                    arrive[idx] = True

                human[idx] = (next_row, next_col)
                answer += 1
                break


def find():
    standard = (10, 10, 10)
    for idx, pos in enumerate(human):
        if arrive[idx]:
            continue
        curr_size = max(abs(pos[0]-EXIT[0]), abs(pos[1]-EXIT[1]))
        end_row, end_col = max(pos[0], EXIT[0]), max(pos[1], EXIT[1])
        start_row, start_col = max(end_row-curr_size, 0), max(end_col-curr_size, 0)
        if (curr_size, start_row, start_col) < standard:
            standard = (curr_size, start_row, start_col)
    return standard


def rotate(start_row, start_col, size):
    global EXIT
    end_row, end_col = start_row+size, start_col+size
    temp = [[0] * (size+1) for _ in range(size+1)]

    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if grid[row][col]:
                grid[row][col] -= 1
            temp[col-start_col][-1-row+start_row] = grid[row][col]

    for idx, (row, col) in enumerate(human):
        if arrive[idx]:
            continue

        if start_row <= row <= end_row and start_col <= col <= end_col:
            human[idx] = (start_row+col-start_col, end_col-row+start_row)

    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            grid[row][col] = temp[row-start_row][col-start_col]

    EXIT = (start_row+EXIT[1]-start_col, end_col-EXIT[0]+start_row)


def custom_print():
    print(f'----turn:{turn+1}----')
    print(f'----human----')
    print(*human)
    print(f'----arrive----')
    print(*arrive)
    print(f'----EXIT----')
    print(*EXIT)
    print(f'----grid----')
    for row in grid:
        print(*row)


scaling = lambda x: int(x)-1

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
human = [tuple(map(scaling, input().split())) for _ in range(M)]
EXIT = tuple(map(scaling, input().split()))
arrive = [False] * M

answer = 0
for turn in range(K):
    # 1. 동시에 움직이자.
    move()

    # 조기 종료
    if sum(arrive) == M:
        break

    # 2. 작은 사각형 찾고 돌리기.
    size, start_row, start_col = find()
    rotate(start_row, start_col, size)

# 정답 출력
print(answer)
print(EXIT[0]+1, EXIT[1]+1)