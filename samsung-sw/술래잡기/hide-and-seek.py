# n : 격자, m : 도망자, h : 나무 수, k : 진행 턴
# 술래의 위치와 시선 방향에 대해서 어떻게 처리할 것인가? 미리 다 구해놓는다? k턴 분량으로?
# move_runner -> move_catcher -> get_score 정도의 진행?
# 다른건 다 괜찮은데 술래 처리가 제일 중요할 듯 싶다. 특히 끝 점에서 도는 것도.
# 술래가 바라보는 좌표 -> 있는 사람들 이게 되어야 하다 보니 dict[좌표] = list 이런 방식으로 저장
# 술래 주위 격자를 따로 따와서 만들어볼까? <- 지금 방법이 안되면 한 번 해볼만하다.

# 상, 우, 하, 좌 -> 술래 이동 경로를 따름.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 이거 왜 빵꾸냈냐.. 잘 좀 생각하지.
delta_lst = [                  (-3, 0),
                     (-2, -1), (-2, 0), (-2, 1),
           (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
    (0, -3), (0, -2), (0, -1), (0, 0),  (0, 1),  (0, 2), (0, 3),
            (1, -2), (1, -1),  (1, 0),  (1, 1),  (1, 2),
                     (2, -1),  (2, 0),  (2, 1),
                               (3, 0)]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def move_runner():
    update_dict.clear()
    for delta_row, delta_col in delta_lst:
        curr_row, curr_col = catcher_row + delta_row, catcher_col + delta_col
        if not in_range(curr_row, curr_col):
            continue

        if (curr_row, curr_col) not in runner_dict:
            continue

        # 인덱스 == d 임을 이용
        for curr_dir, num in enumerate(runner_dict[(curr_row, curr_col)]):
            if not num:
                continue

            next_row, next_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
            # 격자 밖으로 나가는지 처리.
            if not in_range(next_row, next_col):
                next_dir = (curr_dir + 2) % 4
                next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
            else:
                next_dir = curr_dir

            # 방향까지 잘 맞춰줬으면 술래가 있는지 여부에 따라 이동처리.
            if next_row == catcher_row and next_col == catcher_col:
                if (curr_row, curr_col) not in update_dict:
                    update_dict[(curr_row, curr_col)] = [0, 0, 0, 0]
                update_dict[(curr_row, curr_col)][next_dir] += num
            else:
                if (next_row, next_col) not in update_dict:
                    update_dict[(next_row, next_col)] = [0, 0, 0, 0]
                update_dict[(next_row, next_col)][next_dir] += num
        # 다 돌았으면 삭제
        runner_dict.pop((curr_row, curr_col))

    # 이제 업데이트
    for row, col in update_dict:

        if (row, col) not in runner_dict:
            runner_dict[(row, col)] = [0, 0, 0, 0]

        for d in range(4):
            runner_dict[(row, col)][d] += update_dict[(row, col)][d]


def move_catcher():
    global cnt_pointer, cnt, reverse, catcher_row, catcher_col, catcher_dir

    catcher_row += dr[catcher_dir]
    catcher_col += dc[catcher_dir]

    # 돌릴건 돌려야지
    cnt += 1
    if cnt == cnt_lst[cnt_pointer]:
        cnt_pointer += 1 if not reverse else -1
        catcher_dir += 1 if not reverse else -1
        catcher_dir %= 4
        cnt = 0

    # 끝 지점 따로 세팅!
    if catcher_row == 0 and catcher_col == 0:
        catcher_dir = 2
        cnt_pointer, cnt = len(cnt_lst)-1, 0
        reverse = True
    elif catcher_row == center and catcher_col == center:
        catcher_dir = 0
        cnt_pointer, cnt = 0, 0
        reverse = False


def get_score():
    temp = 0
    for k in range(3):
        find_row, find_col = catcher_row + dr[catcher_dir] * k, catcher_col + dc[catcher_dir] * k
        if (find_row, find_col) in runner_dict and (find_row, find_col) not in tree_collect:
            temp += sum(runner_dict[(find_row, find_col)]) * turn
            runner_dict.pop((find_row, find_col))
    return temp

def custom_print():
    print(f'-------grid-------')
    for row in range(N):
        for col in range(N):
            if (row, col) in runner_dict:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()
    print(f'-------runner-------')
    for k, v in runner_dict.items():
        print(f'key : {k}, value : {v}')

def custom_print2():
    print(f'--------soolae----------')
    print(catcher_row, catcher_col, catcher_dir)
    print(cnt, cnt_pointer, reverse)


N, M, H, K = map(int, input().split())
center = N//2
runner_dict, update_dict = dict(), dict()
for _ in range(M):
    x, y, d = map(lambda x: int(x)-1, input().split())
    if (x, y) not in runner_dict:
        runner_dict[(x, y)] = [0, 0, 0, 0]
    runner_dict[(x, y)][1 if d == 0 else 2] += 1

tree_collect = set()
for _ in range(H):
    tree_collect.add(tuple(map(lambda x: int(x)-1, input().split())))

answer = 0
catcher_row, catcher_col, catcher_dir = N//2, N//2, 0
cnt_lst = [i//2+1 for i in range(2*N-2)] + [N-1]    # 동은님이 썼던 전략
cnt_pointer, cnt = 0, 0
reverse = False
for turn in range(1, K+1):
    # 1. 도망자 이동하기.
    move_runner()

    # 2. 술래 이동하기. 이런건 클래스가 훨씬 편해 보인다.
    move_catcher()

    # 3. 도망자 잡기. 점수 업데이트.
    answer += get_score()

# 점수 출력
print(answer)