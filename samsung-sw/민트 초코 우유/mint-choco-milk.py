# 09:30 시작

# 1. 아침 시간
#       - 신앙심 모두 1씩 더해주기

# 2. 점심 시간
#       - 대표자 선정(신앙심, row, col 기록)
#       - 저녁 시간 대비 정보 기록(group, 신앙심, row, col 기록)

# 3. 저녁 시간
#       - 점심에 연산한 순서에 의거하여 전파
#       - 강한 / 약한 전파 조건 잘 적용하기
#       - 전파 받으면 그 턴에는 전파X, 받는건 가능

from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def lunch():
    rep_info = []
    Q = deque()
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue
            visited[row][col] = True

            cnt = 1
            rep = [-trust[row][col], row, col]

            Q.append((row, col))
            while Q:
                curr_row, curr_col = Q.popleft()
                for d in range(4):
                    next_row, next_col = curr_row + dr[d], curr_col + dc[d]
                    if not in_range(next_row, next_col) or visited[next_row][next_col]:
                        continue
                    if group[curr_row][curr_col] != group[next_row][next_col]:
                        continue

                    rep = min(rep, [-trust[next_row][next_col], next_row, next_col])
                    visited[next_row][next_col] = True
                    Q.append((next_row, next_col))
                    cnt += 1

            rep[0] -= cnt
            trust[rep[1]][rep[2]] += cnt
            rep_info.append((group_cnt[group[rep[1]][rep[2]]], rep[0], rep[1], rep[2]))

    rep_info.sort()
    return rep_info


def dinner():
    already_change = set()
    for _, minus_b, start_row, start_col in rep_lst:
        if (start_row, start_col) in already_change:
            continue
        trust[start_row][start_col] = 1

        remain = -1-minus_b
        curr_group = group[start_row][start_col]
        direction = (-minus_b)%4

        next_row, next_col = start_row + dr[direction], start_col + dc[direction]
        while in_range(next_row, next_col) and remain:
            if group[next_row][next_col] == curr_group:
                next_row += dr[direction]
                next_col += dc[direction]
                continue

            target_b = trust[next_row][next_col]
            already_change.add((next_row, next_col))
            if remain > target_b:
                remain -= target_b+1
                group[next_row][next_col] = curr_group
                trust[next_row][next_col] = target_b+1
            else:
                group[next_row][next_col] |= curr_group
                trust[next_row][next_col] += remain
                break

            next_row += dr[direction]
            next_col += dc[direction]


def get_answer():
    score = [0] * 8
    for row in range(N):
        for col in range(N):
            score[group[row][col]] += trust[row][col]
    for order in answer_order:
        yield score[order]


# =======================================================================
# 세팅

N, T = map(int, input().split())
group = []
for _ in range(N):
    temp = list(map(lambda x: 1 if x == 'T' else 2 if x == 'C' else 4, input()))
    group.append(temp)
trust = [list(map(int, input().split())) for _ in range(N)]
group_cnt = [None, 1, 1, 2, 1, 2, 2, 3]
answer_order = [7, 3, 5, 6, 4, 2, 1]

# =======================================================================
# 실행부

for _ in range(T):
    # 1. 아점먹기
    rep_lst = lunch()

    # 2. 저녁먹기
    dinner()

    # 3. 정답출력
    print(*get_answer())