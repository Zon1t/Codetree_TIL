# 10:52 시작  [] /
# 1. 몬스터 알 낳기. 격자 8방향 업데이트 하면서 진행.
# 2. 몬스터 이동. 방향 잘 찾아서, 시체&팩맨 없는 방향으로 이동
# 3. 팩맨 이동. 백트래킹 활용해서 이동 경로 찾기
# 4. 시체 소멸시키기. 유통기한 다루기
# 5. 알에서 몬스터 복제.


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def in_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4


def move_monsters():
    new_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
    for curr_row in range(4):
        for curr_col in range(4):
            for curr_dir, num in enumerate(monster_grid[curr_row][curr_col]):
                if not num:
                    continue

                for delta_dir in range(8):
                    next_dir = (curr_dir+delta_dir)%8
                    next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
                    if not in_range(next_row, next_col) or [next_row, next_col] == PACKMAN:
                        continue
                    if turn <= death_grid[next_row][next_col]:
                        continue

                    new_grid[next_row][next_col][next_dir] += num
                    break
                else:
                    new_grid[curr_row][curr_col][curr_dir] += num

    return new_grid


def find_priority(curr_row, curr_col, cnt, acc, visited):
    global curr_cnt, selected
    if cnt == 3:
        if curr_cnt < acc:
            curr_cnt = acc
            selected = temp[:]
        return

    for d in range(0, 8, 2):
        next_row, next_col = curr_row + dr[d], curr_col + dc[d]
        if not in_range(next_row, next_col):
            continue

        temp[cnt] = d
        find_priority(next_row, next_col, cnt+1, \
                      acc+(0 if (next_row, next_col) in visited else sum(monster_grid[next_row][next_col])), visited+[(next_row, next_col)])


def move_packman():
    global curr_cnt
    curr_cnt = 0

    find_priority(PACKMAN[0], PACKMAN[1], 0, 0, [])
    for direction in selected:
        PACKMAN[0], PACKMAN[1] = PACKMAN[0] + dr[direction], PACKMAN[1] + dc[direction]
        if sum(monster_grid[PACKMAN[0]][PACKMAN[1]]):
            death_grid[PACKMAN[0]][PACKMAN[1]] = turn+2
            monster_grid[PACKMAN[0]][PACKMAN[1]] = [0]*8


def monster_birthday():
    for row in range(4):
        for col in range(4):
            for d in range(8):
                monster_grid[row][col][d] += egg_grid[row][col][d]


def print_status():
    print(f'----gird----')
    for row in monster_grid:
        print(*row)
    print(f'----PACKMAN----')
    print(*selected)
    print(*PACKMAN)


# ===============================================================
# 세팅

scaling = lambda x: int(x)-1
M, T = map(int, input().split())
PACKMAN = list(map(scaling, input().split()))

monster_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(scaling, input().split())
    monster_grid[r][c][d] += 1
death_grid = [[-1]*4 for _ in range(4)]

curr_cnt = 0
temp, selected = [0, 0, 0], [0, 0, 0]

# ===============================================================
# 실행부

for turn in range(1, T+1):
    # 1. 알 만들기.
    egg_grid = [row[:] for row in monster_grid]

    # 2. 몬스터 움직이기.
    monster_grid = move_monsters()

    # 3. 팩맨 움직이기.
    move_packman()

    # 4. 몬스터 복제
    monster_birthday()

# 정답 출력
print(sum([sum([sum(dirs) for dirs in row]) for row in monster_grid]))