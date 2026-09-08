# 격자와 잘 상호작용해서 풀면 되는 문제이다.
# 팩맨 : 그냥 전역 변수로 세팅해서 관리하면 될듯?
# 알 : dict? grid? 잘 쓰면 될 듯 싶다.
# 몬스터 : dict? grid? 걍 grid 쓸까
# 우선 순위를 어떻게 찾는가? -> 백트래킹 쓰면 될 듯 싶은데? itertools 해도 되고
# 격자 만들어서 풀자 그냥. ㄱㄱ


# 팩맨이 쓸 것.
pack_dr = [-1, 0, 1, 0]
pack_dc = [0, -1, 0, 1]

# 몬스터가 쓸 것.
mon_dr = [-1, -1, 0, 1, 1, 1, 0, -1]
mon_dc = [0, -1, -1, -1, 0, 1, 1, 1]


def in_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4


def make_eggs():
    global egg_grid
    egg_grid = [[lst[:] for lst in row] for row in monster_grid]


def move_monster():
    global monster_grid
    new_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            for d in range(8):
                if monster_grid[row][col][d] == 0:
                    continue
                for delta_d in range(8):
                    next_dir = (d + delta_d) % 8
                    next_row, next_col = row + mon_dr[next_dir], col + mon_dc[next_dir]

                    if not in_range(next_row, next_col) or (next_row, next_col) == (packman_row, packman_col):
                        continue
                    if death_grid[next_row][next_col] >= turn:
                        continue

                    new_grid[next_row][next_col][next_dir] += monster_grid[row][col][d]
                    break

                else:
                    new_grid[row][col][d] += monster_grid[row][col][d]

    monster_grid = new_grid


def find_priority(cnt, acc, curr_row, curr_col):
    global curr_max, move_command
    if cnt == 3:
        if curr_max < acc:
            curr_max = acc
            move_command = temp_command[:]
        return

    for d in range(4):
        next_row, next_col = curr_row + pack_dr[d], curr_col + pack_dc[d]
        if not in_range(next_row, next_col):
            continue
        now_lst = monster_grid[next_row][next_col][:]
        monster_grid[next_row][next_col] = [0]*8
        temp_command.append(d)
        find_priority(cnt+1, acc+sum(now_lst), next_row, next_col)
        monster_grid[next_row][next_col] = now_lst
        temp_command.pop()


def move_packman():
    global curr_max, packman_row, packman_col
    curr_max = -1

    find_priority(0, 0, packman_row, packman_col)

    for command in move_command:
        packman_row, packman_col = packman_row + pack_dr[command], packman_col + pack_dc[command]
        temp = sum(monster_grid[packman_row][packman_col])
        if temp:
            death_grid[packman_row][packman_col] = turn+2
            monster_grid[packman_row][packman_col] = [0]*8

def birth():
    for row in range(4):
        for col in range(4):
            for d in range(8):
                monster_grid[row][col][d] += egg_grid[row][col][d]
            egg_grid[row][col] = [0]*8


def get_answer():
    temp = 0
    for row in range(4):
        for col in range(4):
            temp += sum(monster_grid[row][col])
    return temp


def custom_print():
    print(f'----monster_grid----')
    for row in monster_grid:
        print(*row)
    print(f'----death_grid----')
    for row in death_grid:
        print(*row)
    print(f'----egg_grid----')
    for row in egg_grid:
        print(*row)
    print(f'----packman_info----')
    print(move_command)
    print(packman_row, packman_col)


scaling = lambda x: int(x)-1
curr_max, temp_command, move_command = 0, [], [-1, -1, -1]
M, T = map(int, input().split())
packman_row, packman_col = map(scaling, input().split())

monster_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
egg_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
death_grid = [[-1] * 4 for _ in range(4)]
for _ in range(M):
    row, col, direction = map(scaling, input().split())
    monster_grid[row][col][direction] += 1

for turn in range(1, T+1):
    # 1. 알 복사
    make_eggs()

    # 2. 몬스터 이동
    move_monster()

    # 3. 팩맨 이동
    move_packman()

    # 4. 알에서 태어나기.
    birth()

answer = get_answer()
print(answer)