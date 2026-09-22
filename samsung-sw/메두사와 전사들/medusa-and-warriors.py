''' 메두사와 전사들 / 20260922 / 체감 난이도 : 골드 1
소요 시간 : 111분 / 시도 : 2회 (1회차 : 런타임 에러) / 실행 시간 : 394ms / 메모리 : 25MB

타임 라인 : 구상(21분) - 구현(66분) - 검증(22분) - 수정(2분)


[구상]
    - 복잡하고 시키는거 많기는 하지만, 개별적으로 보았을 때에는 어렵지 않다고 생각했다. 그나마 시선
    처리하는 부분에서의 고민 정도? 조금 있었던 것 같다.
    - 최단 경로와 최단 거리에 대한 부분?이 조금 헷갈렸던 것 같다. 위 네 단계에서 맨해튼으로 생각해
    라 라고 명시되어 있었는데, 예제 1번에서 맨해튼을 따라가면 메두사는 공원으로 이동하지 못한다. 그
    래서 경로는 그냥 우리가 bfs에서 소위 생각하는 최단 경로임을 확정짓고 넘어갔다.

[구현]
    - 묘수에 한 번 빠졌다가 헤어나오지 못할 뻔 했다. 시선이 메두사를 기준으로 전파되면서 뻗어나가다
    전사를 만나면 그 뒤로 전파가 안되게 끔 처리하기 위한 여러 세팅들을 시도해보았었다. 그러다가 꼬여
    그냥 완탐 하듯이 만나면 뒤에 처리해주는 식으로.. 비효율적이지만 그렇게 진행했다. 그냥 하드코딩으
    로 밀고 나가면 되는데 이걸 왜 하기 싫어하는지 모르겠다. 이거 갈아 엎는 것 때문에 꽤나 많은 시간
    을 쓰게 되었다. 영상 보니까 30분 넘게 이짓거리 하고, 10분만에 해당 로직을 완성했다..
    - 그 외에는 그냥 평범하게 잘 구현한 것 같다. 그나마 용사 움직이는 로직에 조금 신경을 많이 써가며
    검증했던 것 같다.

[검증]
    - 우선 용사 움직이는 로직에서 아예 움직이지 못하는 경우를 적절하게 처리하지 못해, 해당 부분을 수
    정했다. 애초에 움직이지 못한다는 선택지가 있는 줄도 몰랐는데 2번 테케를 따라가보니, 움직이지 못하
    는 경우가 무조건 있는게 맞았다.
    - 시선 처리를 확인해보는데 케이스가 조금 부족하다고 생각해서 문제에 있는 경우를 직접 만들어 넣어
    보았다. 그러다가 status 판별을 똑바로 하지 못함을 발견하고 인덱싱을 잘못했다는 사실을 발견해 해당
    부분을 수정해주었다.
    - 구현 과정에서 꼼꼼하게 확인하기도 했고 검증도 디버깅 & 검증도 충분히 해보았다고 생각해서 문제
    재차 읽어보고 제출하게 되었다.

[수정]
    - 런타임 에러가 날 구석이 있나 싶었다.. 어지간하면 오타라고 생각해서 변수명 위주로 확인하는데 바로
    발견할 수 있었다. dist_grid를 만드는 과정에서 start_row와 start_col에 각각 er과 er을 할당한
    것이다;; 원래 좌표 변수명은 항상 _row, _col로 끝내는 게 루틴인데 문제에서 사용할 변수도 워낙 많
    고 구현해야 할 부분도 많다보니 변수명을 좀 조잡하게 세팅하긴 했었다. 도대체 테케랑 내가 만든 테케는
    왜 정상 작독했는지 확인해보니, er과 ec가 애초에 같거나 해당 경로 위에 도착점이 있어 운 좋게 통과
    한 것.. 어지간하면 익숙한, 정해둔 변수명을 사용하도록 하자.


예제에서 나오는 시선 처리 케이스
9 6
5 4 0 0
2 2 4 2 4 5 4 6 4 7 4 8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

9 3
0 5 0 0
4 2 4 4 6 6
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

# 굉장히 귀찮은 문제이지만, 그냥 시키는대로 천천히 하면 된다. 어려운 로직은 없어 보인다.
# m_move() -> see() -> w_move() -> attack() 이런 느낌으로..
# 최단 거리는 맨해튼 거리로 연산하면 된다. << 이거 쉽지않네
# 유의할 점? 시야각을 잘 처리해야 할 것 같은데.. bfs까진 맞고. 용사 만나는 위치 기준으로 덧씌우기?
# 단순히 생각하면 안 될 것 같다. 일단 구현 ㄱㄱ


from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 이거 폐기, 그냥 완탐하면 되는데 무슨 부귀영화를 누리겠다고;
# # 직선 따로 대각 따로? 대각은 이후 직선도 퍼지게끔? 이것도 좋아보인다.
# deltas = [[[(-1, -1), (-1, 0), (None, None)], [(None, None), (-1, 0), (None, None)], [(None, None), (-1, 0), (-1, 1)]],
#           [[(1, -1), (1, 0), (None, None)],   [(None, None), (1, 0), (None, None)],  [(None, None), (1, 0), (1, 1)]],
#           [[(-1, -1), (0, -1), (None, None)], [(None, None), (0, -1), (None, None)], [(None, None), (0, -1), (1, -1)]],
#           [[(-1, 1), (0, 1), (None, None)],   [(None, None), (0, 1), (None, None)],  [(None, None), (0, 1), (1, 1)]]]

init_delta = [[(-1, -1), (-1, 0), (-1, 1)],
              [(1, -1), (1, 0), (1, 1)],
              [(-1, -1), (0, -1), (1, -1)],
              [(-1, 1), (0, 1), (1, 1)]]
deltas = [[[(-1, -1), (-1, 0)], [(-1, 0)], [(-1, 0), (-1, 1)]],
          [[(1, -1), (1, 0)],   [(1, 0)],  [(1, 0), (1, 1)]],
          [[(-1, -1), (0, -1)], [(0, -1)], [(0, -1), (1, -1)]],
          [[(-1, 1), (0, 1)],   [(0, 1)],  [(0, 1), (1, 1)]]]



def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def make_dist_grid():
    start_row, start_col = er, ec
    dist_grid = [[-1] * N for _ in range(N)]
    dist_grid[start_row][start_col] = 0

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_row == mr and curr_col == mc:
            break

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]
            if not in_range(next_row, next_col) or dist_grid[next_row][next_col] != -1:
                continue
            if grid[next_row][next_col] == 1:
                continue
            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    return dist_grid


def m_move():
    for d in range(4):
        next_row, next_col = mr+dr[d], mc+dc[d]
        if not in_range(next_row, next_col):
            continue
        if dist_grid[next_row][next_col] == dist_grid[mr][mc]-1:
            return next_row, next_col


def update_grid(row, col, status, direction, check_grid):
    Q = deque([(row, col)])
    new_grid = [[0] * N for _ in range(N)]
    while Q:
        curr_row, curr_col = Q.popleft()
        for delta_row, delta_col in deltas[direction][status]:
            next_row, next_col = curr_row + delta_row, curr_col + delta_col
            if not in_range(next_row, next_col) or new_grid[next_row][next_col]:
                continue
            new_grid[next_row][next_col] = 1
            Q.append((next_row, next_col))

    for row in range(N):
        for col in range(N):
            if new_grid[row][col]:
                check_grid[row][col] = 1


# 돌로 된 전사의 수 반환
def see():
    watch_grid = [[[0] * N for _ in range(N)] for _ in range(4)]
    max_cnt, max_direction = 0, 0
    for d in range(4):
        curr_cnt = 0
        check_grid = [[0] * N for _ in range(N)]

        Q = deque([(mr, mc)])
        while Q:
            curr_row, curr_col = Q.popleft()
            for delta_row, delta_col in init_delta[d]:
                next_row, next_col = curr_row + delta_row, curr_col + delta_col
                if not in_range(next_row, next_col) or watch_grid[d][next_row][next_col]:
                    continue
                if check_grid[next_row][next_col]:
                    continue

                watch_grid[d][next_row][next_col] = 1
                Q.append((next_row, next_col))

                if w_grid[next_row][next_col]:
                    curr_cnt += w_grid[next_row][next_col]
                    if dr[d]:
                        status = 0 if next_col < mc else 1 if next_col == mc else 2
                    else:
                        status = 0 if next_row < mr else 1 if next_row == mr else 2
                    update_grid(next_row, next_col, status, d, check_grid)

        if curr_cnt > max_cnt:
            max_cnt, max_direction = curr_cnt, d

    return max_cnt, watch_grid[max_direction]


# 이동 거리의 합. + 공격한 전사의 수 반환
def w_move():
    new_w_grid = [[0] * N for _ in range(N)]
    attack_cnt, move_cnt = 0, 0
    for row in range(N):
        for col in range(N):
            if not w_grid[row][col]:
                continue

            if watch_grid[row][col]:
                new_w_grid[row][col] += w_grid[row][col]
                continue

            curr_dist = get_dist((row, col), (mr, mc))
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue

                next_dist = get_dist((next_row, next_col), (mr, mc))
                if watch_grid[next_row][next_col] or next_dist >= curr_dist:
                    continue

                move_cnt += w_grid[row][col]
                if next_dist == 0:
                    attack_cnt += w_grid[row][col]
                else:
                    for d_ in range(2, 6):
                        nnr, nnc = next_row + dr[d_%4], next_col + dc[d_%4]
                        if not in_range(nnr, nnc):
                            continue

                        nnd = get_dist((nnr, nnc), (mr, mc))
                        if watch_grid[nnr][nnc] or nnd >= next_dist:
                            continue

                        move_cnt += w_grid[row][col]
                        if nnd == 0:
                            attack_cnt += w_grid[row][col]
                        else:
                            new_w_grid[nnr][nnc] += w_grid[row][col]

                        break

                    else:
                        new_w_grid[next_row][next_col] += w_grid[row][col]

                break

            else:
                new_w_grid[row][col] += w_grid[row][col]

    return attack_cnt, move_cnt, new_w_grid


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# ==============================================
# 세팅

N, M = map(int, input().split())
mr, mc, er, ec = map(int, input().split())

w_grid = [[0] * N for _ in range(N)]
w_info = list(map(int, input().split()))
for i in range(M):
    ar, ac = w_info[i<<1], w_info[i<<1|1]
    w_grid[ar][ac] += 1

grid = [list(map(int, input().split())) for _ in range(N)]
dist_grid = make_dist_grid()

# ==============================================
# 실행부

if dist_grid[mr][mc] == -1:
    print(-1)
else:
    while mr != er or mc != ec:
        # 1. 메두사 움직이기.
        mr, mc = m_move()
        w_grid[mr][mc] = 0
        if mr == er and mc == ec:
            print(0)
            break

        # 2. 시선처리
        rock_cnt, watch_grid = see()

        # 3. 전사들 움직임.
        attack_cnt, move_cnt, w_grid = w_move()

        # 4. 정답 출력
        print(move_cnt, rock_cnt, attack_cnt)