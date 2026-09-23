''' 민트 초코 우유 / 20260923 / 체감 난이도 : 골드 3~4
소요 시간 : 150분 / 시도 : 1회 / 실행 시간 : 382ms / 메모리 : 24MB

타임 라인 : 구상(17분) - 구현(41분) - 검증(92분)


[구상]
    - 문제 전체를 이해하고 정리하는 것이 조금 오래 걸렸던 것 같다. 우선 순위도 잘 따져야 하고, 순차적
    으로 시키는 거 열심히 하자 라는 마음가짐으로 들어갔던 것 같다.
    - 주석으로 크게 수행해야 할 로직을 정리하고, 세부적인 것들은 구현 단계에서 읽어가며 해도 괜찮을 것
    이라 생각해 곧바로 구현에 들어갔다.

[구현]
    - 유혹?이 많았던 것 같다. 아침 거르고 수행하는 것, 점심 시간을 할애해서 저녁 시간을 준비하는 등등
    아이디어가 떠오르는 게 조금씩 있었다. 점심 시간을 할애하는 것 말고는 전부 기각해, 로직을 구축하고자
    하였다. 다시는 나대지 말기로 결심했기 때문이다.
    - 구현 과정에서 검증 및 세팅에 심혈을 기울였다. 로직이 얼마 안되기는 하지만, 우선순위 잘 따지는지
    기능 구현할 때마다 최종 결과물과 과정을 찍어보았다. 크게 어렵다거나 할 부분은 없었던 것 같다.

[검증]
    - 문제 읽고, 찍어 보고, 손으로 써보고, 로직 따로 temp.py에 갖다 놓고, 정상 작동 확인하고, 과정
    찍고.. 등등등 무한으로 진행했다. 어제나 그제 문제 같으면 몰랐겠는데, 시간이 생각보다 많이 남아서
    아예 일정 시간 동안 명상도 하고, 마음 가다듬고, 새로운 시선으로 보려고 하고.. 수정한 부분은 없었지
    만, 마음 편하게 제출했던 것 같다.
'''

# 비트마스킹 써서 해결하면 될 것 같다.
# 1. 아침 시간 : 모든 사람의 신앙심이 1 증가
# 2. 점심 시간 : 1. 그룹 형성. 그룹 & 대표자에 대한 정보 기록 필요
#               2. 신앙심 1씩 대표자에게 넘기기
# 3. 저녁 시간 : 1. 신앙 전파. 이것도 우선순위에 의거하여, 대표자 신앙심, 행작, 열작
#               2. 해당 순서대로, 정해진 방향에 대해 전파 시작.

# 테케 검증 완료 - 9:58
# 대표자 먼저 찾으면 아침 과정 스킵 가능. 그래도 굳이 나대지 말자.

from collections import deque

# 주어진 조건에 의거
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def lunch():
    visited = [[False] * N for _ in range(N)]
    rep_lst = []
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue
            visited[row][col] = True

            cnt, rep = 0, (-how_much[row][col], row, col)
            Q.append((row, col))
            while Q:
                curr_row, curr_col = Q.popleft()
                cnt += 1
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if trust_grid[curr_row][curr_col] != trust_grid[next_row][next_col]:
                        continue

                    rep = min(rep, (-how_much[next_row][next_col], next_row, next_col))
                    visited[next_row][next_col] = True
                    Q.append((next_row, next_col))

            # 신앙심 모으기.
            rep_row, rep_col = rep[1], rep[2]
            how_much[rep_row][rep_col] += cnt

            # 저녁 시간을 수월하게 보내기 위한 세팅들..
            pick_cnt = cnt_lst[trust_grid[row][col]]
            rep_lst.append((rep_row, rep_col, how_much[rep_row][rep_col], pick_cnt))

    # pick_cnt 작은 순, 신앙심이 큰 순, 행 작은 순, 열 작은 순
    rep_lst.sort(key=lambda x: (x[3], -x[2], x[0], x[1]))
    return rep_lst


def dinner():
    change_set.clear()
    for row, col, B, _ in rep_lst:
        if (row, col) in change_set:
            continue

        how_much[row][col] = 1
        remain, my_fav = B-1, trust_grid[row][col]

        curr_dir = B%4
        next_row, next_col = row + dr[curr_dir], col + dc[curr_dir]
        while remain > 0 and in_range(next_row, next_col):
            if trust_grid[next_row][next_col] == my_fav:
                next_row += dr[curr_dir]
                next_col += dc[curr_dir]
                continue

            # 전파.
            change_set.add((next_row, next_col))
            if how_much[next_row][next_col] < remain:
                trust_grid[next_row][next_col] = my_fav
                how_much[next_row][next_col] += 1
                remain -= how_much[next_row][next_col]
            else:
                trust_grid[next_row][next_col] |= my_fav
                how_much[next_row][next_col] += remain
                break

            next_row += dr[curr_dir]
            next_col += dc[curr_dir]


def get_answer():
    total_lst = [0] * 8
    for row in range(N):
        for col in range(N):
            total_lst[trust_grid[row][col]] += how_much[row][col]

    for idx in answer_idx:
        yield total_lst[idx]


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# ==================================================
# 세팅

N, T = map(int, input().split())

trust_grid = [[0] * N for _ in range(N)]
for i in range(N):
    for j, val in enumerate(input()):
        trust_grid[i][j] = 1 if val == 'T' else 2 if val == 'C' else 4

how_much = [list(map(int, input().split())) for _ in range(N)]
answer_idx = [7, 3, 5, 6, 4, 2, 1]
cnt_lst = [0, 1, 1, 2, 1, 2, 2, 3]
change_set = set()
Q = deque()

# ==================================================
# 실행부

for _ in range(T):
    # 1. 나는 아침 안 먹어
    rep_lst = lunch()

    # 2. 저녁 시간
    dinner()

    # 3. 정답 출력
    answer = get_answer()
    print(*answer)