# 17:11 시작
# 다른 사람들이 사용했던 달팽이 로직을 써보자.
# 도망자 - 100명 안쪽이라 음.. 그냥 리스트로 관리할까? 싶기도 하다. 이렇게 해보자.
# 술래 - 따로 전역변수로 관리할 것.
# 나무 로직 처리를 잘해보자. ㄱㄱ


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


deltas = [
                                (-3, 0),
                      (-2, -1), (-2, 0), (-2, 1),
            (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
   (0, -3), ( 0, -2), ( 0, -1), ( 0, 0), ( 0, 1), ( 0, 2), ( 0, 3),
            ( 1, -2), ( 1, -1), ( 1, 0), ( 1, 1), ( 1, 2),
                      ( 2, -1), ( 2, 0), ( 2, 1),
                                ( 3, 0)
]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def choono():
    new_nobi = dict()
    for delta_row, delta_col in deltas:
        curr_row, curr_col = catcher_row + delta_row, catcher_col + delta_col
        if not in_range(curr_row, curr_col) or (curr_row, curr_col) not in nobi_dict:
            continue

        for curr_dir, num in enumerate(nobi_dict[(curr_row, curr_col)]):
            if not num:
                continue

            next_row, next_col, next_dir = curr_row+dr[curr_dir], curr_col+dc[curr_dir], curr_dir
            if not in_range(next_row, next_col):
                next_dir = (next_dir+2)%4
                next_row, next_col = curr_row+dr[next_dir], curr_col+dc[next_dir]

            if next_row == catcher_row and next_col == catcher_col:
                next_row, next_col = curr_row, curr_col

            if (next_row, next_col) not in new_nobi:
                new_nobi[(next_row, next_col)] = [0, 0, 0, 0]
            new_nobi[(next_row, next_col)][next_dir] += num

        nobi_dict.pop((curr_row, curr_col))

    for (row, col), d_lst in new_nobi.items():
        if (row, col) not in nobi_dict:
            nobi_dict[(row, col)] = [0, 0, 0, 0]
        for curr_dir, num in enumerate(d_lst):
            nobi_dict[(row, col)][curr_dir] += num
    

def move():
    global catcher_row, catcher_col, catcher_dir, pointer, cnt, reverse

    catcher_row += dr[catcher_dir]
    catcher_col += dc[catcher_dir]
    cnt += 1

    if cnt == cnt_lst[pointer]:
        pointer += 1 if not reverse else -1
        catcher_dir += 1 if not reverse else -1
        catcher_dir %= 4
        cnt = 0

    if catcher_row == 0 and catcher_col == 0:
        catcher_dir = 2
        pointer = -1
        reverse = True

    if catcher_row == center and catcher_col == center:
        catcher_dir = 0
        pointer = 0
        reverse = False


def catch():
    temp = 0
    for k in range(3):
        watch_row, watch_col = catcher_row+dr[catcher_dir]*k, catcher_col+dc[catcher_dir]*k
        if not in_range(watch_row, watch_col) or (watch_row, watch_col) not in nobi_dict:
            continue
        if (watch_row, watch_col) in trees:
            continue
        temp += sum(nobi_dict[(watch_row, watch_col)])
        nobi_dict.pop((watch_row, watch_col))

    return temp


# ================================================
# 세팅

scaling = lambda x: int(x)-1

N, M, H, K = map(int, input().split())
center = N >> 1

nobi_dict = dict()
for _ in range(M):
    r, c, d = map(scaling, input().split())
    if (r, c) in nobi_dict:
        nobi_dict[(r, c)][d+1] += 1
    else:
        nobi_dict[(r, c)] = [0, 0, 0, 0]
        nobi_dict[(r, c)][d+1] += 1

trees = set([tuple(map(scaling, input().split())) for _ in range(H)])

catcher_row, catcher_col, catcher_dir = center, center, 0
cnt_lst = [i//2+1 for i in range(2*N-2)] + [N-1]
pointer, cnt, reverse = 0, 0, False

# ================================================
# 실행부

answer = 0
for turn in range(1, K+1):
    # 1. 도망가기.
    choono()

    # 2. 술래 움직이기.
    move()

    # 3. 잡기
    answer += turn * catch()

# 정답 출력
print(answer)