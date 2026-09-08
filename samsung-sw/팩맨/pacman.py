''' 팩맨 / 20260908 / 체감 난이도 : 골드 4
소요 시간 : 55분 / 시도 : 1회 / 실행 시간 : 60ms / 메모리 : 17MB

타임 라인 : 구상(18분) - 구현(30분) - 검증(7분)


[구상]
    - 사이즈가 작기도 하고 해서, 필요한 grid를 여럿 만들어두고 독립적으로 관리하면 되겠다는 생각이
    들었다. 팩맨의 위치만 전역으로 관리하고, 알/몬스터/시체는 grid를 그려 방향별 관리를 해보았다.
    - 팩맨 움직임의 우선순위를 어떻게 찾을까 고민했었는데 itertools 쓰는 것보단 그냥 백트래킹으로
    업데이트해가며 찾는게 좋을 것이라 판단했다.
    - 초기에는 방향을 각 위치에 append해서 관리하자고 생각했다.

[구현]
    - 구현을 하던 중간에 문득 진행되는 동안 살아있는 몬스터의 수가 100만개가 넘지 않는다는 문장이
    떠올랐다. 그렇게 몬스터가 많은 케이스가 존재할 수 있나? 싶다가도 혹시 모르니 방향별로 몇마리
    존재하는지 관리하는 방식으로 변경했다. 몬스터가 많다면 이 방식이 더 효율적이라 생각했다.
    - 함수 내부에서 백트래킹을 호출해봤던 적이 손에 꼽는다. 최대한 실수 안하려고 했는데 세팅이나
    이러한 부분에서 잔실수가 많았다. 전역으로 세팅한 변수를 지속적으로 업데이트하는 방식을 취했다.
    - 시체처리도 죽일 때만 하고, 문제와 계속 비교해가며 빼먹는 부분이 없고자 했다. custom_print
    정의해서 각 변수의 변화 양상을 관찰하는 식으로 검증을 지속해나갔다.

[검증]
    - 다시 마음을 가다듬고 문제를 정독했다. 테케 예시도 따라가보며 정확하게 업데이트 되는지, 주석과
    코드를 한 번 더 읽은 뒤 제출하게 되었다.
'''


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

# 범위에서 벗어나는지 체크하기 위함.
def in_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4

# 알 격자 업데이트. 자연스럽게 초기화도 된다!
def make_eggs():
    global egg_grid
    egg_grid = [[lst[:] for lst in row] for row in monster_grid]

# 몬스터 이동 함수.
def move_monster():
    global monster_grid
    new_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            for d in range(8):
                # 해당 방향의 몬스터가 없으면 굳이 따질 필요는 없다.
                if monster_grid[row][col][d] == 0:
                    continue
                
                # 현재 방향을 기준으로 돌면서 판가름.
                for delta_d in range(8):
                    next_dir = (d + delta_d) % 8
                    next_row, next_col = row + mon_dr[next_dir], col + mon_dc[next_dir]
                    
                    # 만약 격자 밖을 벗어나거나 팩맨이 있다? continue
                    if not in_range(next_row, next_col) or (next_row, next_col) == (packman_row, packman_col):
                        continue
                    # 만약 시체가 있다? continue
                    if death_grid[next_row][next_col] >= turn:
                        continue

                    # 새로운 격자에 몬스터 수 업뎃 + break
                    new_grid[next_row][next_col][next_dir] += monster_grid[row][col][d]
                    break
                # 여기까지 왔으면 break 안당했다는 뜻! -> 제자리에 제방향으로 업데이트
                else:
                    new_grid[row][col][d] += monster_grid[row][col][d]
    
    # grid 갈아끼기
    monster_grid = new_grid

# 팩맨 이동 우선순위를 찾기 위한 백트래킹 함수.
def find_priority(cnt, acc, curr_row, curr_col):
    global curr_max, move_command
    # 3번 움직였으면..
    if cnt == 3:
        # 몬스터를 더 많이 잡을 수 있다? command 업데이트!
        if curr_max < acc:
            curr_max = acc
            move_command = temp_command[:]
        return
    
    # 인접한 네 방향에 대해서 탐색 진행.
    for d in range(4):
        next_row, next_col = curr_row + pack_dr[d], curr_col + pack_dc[d]
        if not in_range(next_row, next_col):
            continue

        # 잡아 먹는다면, monster_grid도 zero_list로 갈아끼고, 누적합 연산해서 업데이트
        now_lst = monster_grid[next_row][next_col][:]
        monster_grid[next_row][next_col] = [0]*8
        temp_command.append(d)
        find_priority(cnt+1, acc+sum(now_lst), next_row, next_col)
        
        # 복구는 잊지 말고 해주자!
        monster_grid[next_row][next_col] = now_lst
        temp_command.pop()

# 팩맨 이동 함수.
def move_packman():
    global curr_max, packman_row, packman_col
    curr_max = -1   # 백트래킹을 위한 준비

    # 백트래킹으로 이동 우선순위 받아오기. move_command는 전역으로 미리 선언해뒀음.
    find_priority(0, 0, packman_row, packman_col)

    # 찾은 command 기반 몬스터 잡아먹기.
    for command in move_command:
        packman_row, packman_col = packman_row + pack_dr[command], packman_col + pack_dc[command]
        temp = sum(monster_grid[packman_row][packman_col])
        if temp:
            # 잡아 먹었을 때만 시체 처리!
            death_grid[packman_row][packman_col] = turn+2
            monster_grid[packman_row][packman_col] = [0]*8

# 몬스터가 알 깨고 나온다.
def birth():
    for row in range(4):
        for col in range(4):
            for d in range(8):
                monster_grid[row][col][d] += egg_grid[row][col][d]

# 정답 연산하는 함수.
def get_answer():
    temp = 0
    for row in range(4):
        for col in range(4):
            temp += sum(monster_grid[row][col])
    return temp

# 찍어보자!
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


scaling = lambda x: int(x)-1                                # 방향도 좌표도 편하게 쓰기 위함.
curr_max, temp_command, move_command = 0, [], [-1, -1, -1]  # 백트래킹에 필요!

# 입력받기
M, T = map(int, input().split())
packman_row, packman_col = map(scaling, input().split())

# 필요한 격자들 선언.
monster_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
egg_grid = [[[0]*8 for _ in range(4)] for _ in range(4)]
death_grid = [[-1] * 4 for _ in range(4)]

# 몬스터도 입력받기
for _ in range(M):
    row, col, direction = map(scaling, input().split())
    monster_grid[row][col][direction] += 1

# 실행부.
for turn in range(1, T+1):
    # 1. 알 복사
    make_eggs()

    # 2. 몬스터 이동
    move_monster()

    # 3. 팩맨 이동
    move_packman()

    # 4. 알에서 태어나기.
    birth()

# 정답 연산 후 출력하기.
answer = get_answer()
print(answer)