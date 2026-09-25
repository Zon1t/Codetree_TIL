# 0912 시작  [] /
# 1. 밀가루 양이 가장 작은 위치에 밀가루 넣기
# 2. 도우 말기.. 회전 + append 반복
# 3. 델타로 처리. 마는거는 항상 모양이 일정하게 나올 수 밖에 없다. 그럼 재사용도 가능할 듯
# 4. 두 번 접고 누르기


dr = [0, 1]
dc = [1, 0]


def add_one(value):
    for i in range(N):
        if milgaru[i] == value:
            milgaru[i] += 1


def make_snail():
    curr_idx, remain = 4, N-4
    curr_mat = [[1, 0],
                [2, 3]]
    while True:
        need_mil = len(curr_mat)

        if remain < need_mil:
            break

        curr_mat = [list(row[::-1]) for row in zip(*curr_mat)]
        curr_mat.append(list(range(curr_idx, curr_idx+need_mil)))

        curr_idx += need_mil
        remain -= need_mil

    if remain:
        curr_mat[-1].extend(list(range(curr_idx, N)))
        for row in range(len(curr_mat)-1):
            curr_mat[row] += [-1] * remain

    R, C, curr_idx = len(curr_mat), len(curr_mat[0]), 0
    pos_mat = [[-1] * C for _ in range(R)]
    for col in range(C):
        for row in range(R-1, -1, -1):
            if curr_mat[row][col] == -1:
                break
            pos_mat[row][col] = curr_idx
            curr_idx += 1

    return curr_mat, pos_mat, R, C


def press_snail():
    new_garu = [0] * N
    for row in range(R):
        for col in range(C):
            curr_idx = idx_snail[row][col]
            if curr_idx == -1:
                continue
            curr_mil = milgaru[curr_idx]

            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if next_row < 0 or next_row >= R or next_col < 0 or next_col >= C:
                    continue

                next_idx = idx_snail[next_row][next_col]
                if next_idx == -1:
                    continue
                next_mil = milgaru[next_idx]

                D = abs(curr_mil-next_mil) // 5
                if D:
                    curr_move, next_move = pos_snail[row][col], pos_snail[next_row][next_col]
                    new_garu[curr_move] += -D if curr_mil > next_mil else D
                    new_garu[next_move] -= -D if curr_mil > next_mil else D

    curr_idx = 0
    for col in range(C):
        for row in range(R-1, -1, -1):
            if pos_snail[row][col] == -1:
                break
            new_garu[curr_idx] += milgaru[idx_snail[row][col]]
            curr_idx += 1

    return new_garu


def make_twice():
    idx_lst = list(range(N))
    idx_mat = [idx_lst[half:half+quat][::-1],
               idx_lst[quat:half],
               idx_lst[:quat][::-1],
               idx_lst[half+quat:]]

    curr_idx = 0
    pos_mat = [[-1] * quat for _ in range(4)]
    for col in range(quat):
        for row in range(3, -1, -1):
            pos_mat[row][col] = curr_idx
            curr_idx += 1

    return idx_mat, pos_mat


def twice():
    new_garu = [0] * N
    for row in range(4):
        for col in range(quat):
            curr_idx = idx_twice[row][col]
            curr_mil = milgaru[curr_idx]
            for d in range(2):
                next_row, next_col = row+dr[d], col+dc[d]
                if next_row < 0 or next_row >= 4 or next_col < 0 or next_col >= quat:
                    continue

                next_idx = idx_twice[next_row][next_col]
                next_mil = milgaru[next_idx]

                D = abs(curr_mil-next_mil) // 5
                if D:
                    curr_move, next_move = pos_twice[row][col], pos_twice[next_row][next_col]
                    new_garu[curr_move] -= D if curr_mil > next_mil else -D
                    new_garu[next_move] += D if curr_mil > next_mil else -D

    curr_idx = 0
    for col in range(quat):
        for row in range(3, -1, -1):
            new_garu[curr_idx] += milgaru[idx_twice[row][col]]
            curr_idx += 1

    return new_garu


def print_snail(what, snail):
    print('----', what, '----')
    for row in snail:
        print(*row)


# ===================================================
# 세팅하기

N, K = map(int, input().split())
milgaru = list(map(int, input().split()))
half, quat = N >> 1, N >> 2

idx_snail, pos_snail, R, C = make_snail()
idx_twice, pos_twice = make_twice()
turn = 0

# ===================================================
# 실행부

while True:
    # 0. 초기 세팅
    min_garu = min(milgaru)
    if max(milgaru) - min_garu <= K:
        break
    turn += 1

    # 1. 밀가루 넣기
    add_one(min_garu)

    # 2. 달팽이 누르기.
    milgaru = press_snail()

    # 3. 두 번 접고 누르기.
    milgaru = twice()

# 정답 출력
print(turn)