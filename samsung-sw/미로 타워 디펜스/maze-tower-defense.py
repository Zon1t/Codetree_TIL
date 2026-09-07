# 또또또 달팽이 문제. 이전에 풀었던 문제에서는 이동할 칸이나 이러한 데이터들을 미리 저장하는 방식
# 을 택했는데, 얘도 좌표를 순서대로 모아둬서 문제를 해결하면 될 듯 싶다. 당연 list로 관리
# 땡기는 것도 예전에 만들었던 중력 로직? pointer 써서 만드는.. 그런 느낌으로 하면 될 것 같다.
# 개수를 count해서 다시 미로에 집어넣기.. 얘는 아예 update를 해줘야 하나? or 덮어쓰기 + 0으로
# 초기화하기? 이건 구현 과정에서 쉬운 방향으로 가져가보자. 점수 update는 죽이면서 진행!

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def shot(d, p):
    global answer
    for k in range(1, p+1):
        shot_row, shot_col = center + dr[d] * k, center + dc[d] * k

        if not in_range(shot_row, shot_col):
            break

        answer += grid[shot_row][shot_col]
        grid[shot_row][shot_col] = 0

def push():
    pointer = 0
    for idx in range(end_idx):
        if grid[ordered_position[idx][0]][ordered_position[idx][1]] != 0:
            if pointer != idx:
                grid[ordered_position[idx][0]][ordered_position[idx][1]], grid[ordered_position[pointer][0]][ordered_position[pointer][1]] = \
                    grid[ordered_position[pointer][0]][ordered_position[pointer][1]], grid[ordered_position[idx][0]][ordered_position[idx][1]]
            pointer += 1


def check():
    global answer
    cnt, curr_num, is_killed = 0, -1, False
    final_idx = end_idx
    for idx in range(end_idx):
        if grid[ordered_position[idx][0]][ordered_position[idx][1]] == 0:
            final_idx = idx
            break

        if curr_num != grid[ordered_position[idx][0]][ordered_position[idx][1]]:
            if cnt >= 4:
                is_killed = True
                answer += cnt * curr_num
                for kill_idx in range(idx-cnt, idx):
                    grid[ordered_position[kill_idx][0]][ordered_position[kill_idx][1]] = 0
            cnt, curr_num = 1, grid[ordered_position[idx][0]][ordered_position[idx][1]]
        else:
            cnt += 1

    # 마지막 남아있는 것 확인도 잊지 말기!
    if cnt >= 4:
        is_killed = True
        answer += cnt * curr_num
        for kill_idx in range(final_idx-cnt, final_idx):
            grid[ordered_position[kill_idx][0]][ordered_position[kill_idx][1]] = 0

    return is_killed


def update():
    cnt, curr_num = 1, grid[ordered_position[0][0]][ordered_position[0][1]]

    if curr_num == 0:
        return

    write_lst = []
    for idx in range(1, end_idx):
        if grid[ordered_position[idx][0]][ordered_position[idx][1]] == 0:
            break

        if curr_num != grid[ordered_position[idx][0]][ordered_position[idx][1]]:
            write_lst.append(cnt)
            write_lst.append(curr_num)
            cnt, curr_num = 1, grid[ordered_position[idx][0]][ordered_position[idx][1]]
        else:
            cnt += 1

    if cnt:
        write_lst.append(cnt)
        write_lst.append(curr_num)

    cut_idx = min(len(write_lst), end_idx)
    for idx in range(cut_idx):
        grid[ordered_position[idx][0]][ordered_position[idx][1]] = write_lst[idx]

    if cut_idx < end_idx:
        for idx in range(cut_idx, end_idx):
            grid[ordered_position[idx][0]][ordered_position[idx][1]] = 0


def print_grid():
    for row in grid:
        print(*row)

N, M = map(int, input().split())
center, end_idx = N >> 1, N**2 - 1
grid = [list(map(int, input().split())) for _ in range(N)]

# 초기 세팅하기.
cnt_lst = [i//2+1 for i in range(2*N-2)] + [N-1]
ordered_position = []   # 아마 핵심이 될 듯 싶다.
curr_row, curr_col, curr_dir = center, center, 2
curr_cnt, curr_pointer = 0, 0
while True:
    curr_row, curr_col = curr_row + dr[curr_dir], curr_col + dc[curr_dir]
    curr_cnt += 1
    ordered_position.append((curr_row, curr_col))

    if curr_row == 0 and curr_col == 0:
        break

    if curr_cnt == cnt_lst[curr_pointer]:
        curr_cnt = 0
        curr_pointer += 1
        curr_dir = (curr_dir - 1) % 4

answer = 0
for round in range(M):
    # 1. 플레이어 공격.
    d, p = map(int, input().split())
    shot(d, p)

    # 2. 빈 공간 채우기.
    push()

    # 3. 반복 몬스터 삭제.
    while check():
        push()

    # 4. 격자 업데이트.
    update()

print(answer)