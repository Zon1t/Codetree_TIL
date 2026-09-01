''' 술래잡기 체스 / 20260901 / 체감 난이도 : 골드 4
소요 시간 : 54분 / 시도 : 1회 / 실행 시간 : 52ms / 메모리 : 16MB

타임 라인 : 구상 및 틀 만들기(17분) - 구현(20분) - 수정 및 검증(17분)

[구상]
    - 데이터를 어떻게 관리하냐가 중요한 문제라고 생각했다. 숫자가 작은 순서대로 진행이 되어야 한다는 점,
    이동할 대상이 되는 좌표의 정보 역시 알 수 있어야 한다는 점으로 미루어 보았을 때, 숫자 <--> 좌표가
    필수적으로 이루어져야 한다고 판단했다. 즉 좌표를 알 때 숫자를 알 수 있어야 하고, 숫자를 알 때 해당
    숫자가 어느 위치에 있는지 알아야 한다는 것이다. 이를 위해 어떤 자료형으로 관리해야 할지 많이 고민했다.
    - 백트래킹을 쓰는 문제임은 직관적으로 알 수 있었다. 함수 인자나 이런 부분은 구현 단계에서 생각하는 게
    편하다고 생각하여 대략적인 생각만을 가지고 넘어갔다.

[구현]
    - grid와 dict의 업데이트는 비가역적, 술래가 움직이는 것은 가역적인 기능이라 판단해, grid와 dict만
    복사해 업데이트한 후 백트래킹 보내는 방식을 취하게 되었다. 물론 술래가 잡는 기능은 복원까지 빼먹지
    않고 수행했다.
    - 구현하는 부분에 있어서 잔실수가 조금 있었는데, 입력 받는 부분에서 j대신 i를 써서 해당 부분은 금방
    수정을 할 수 있었다. 대체로 금방 깨닫고 찾을 수 있는 부분에 대한 것들이였고, 큰 문제 없이 구현을
    마쳤다고 생각했다.

[수정 및 검증]
    - custom_print 함수를 정의해 매턴 찍어보며, 문제에서 요구하는 바를 올바르게 수행하는지 계속 확인해
    보았다. 그러던 중 첫 번째 업데이트 이후 지속적으로 grid update 기능이 올바르게 수행되지 않음을 발견
    할 수 있었다.
    - 출력 결과와 예제를 기준으로 확인해보니 방향을 돌리면 그 방향을 계속 가지게 된다는 사실을 알 수 있었
    다. 내가 잘못 이해한 부분이었다. 아주 일부만 수정하면 되었어서 곧바로 수정할 수 있었고, 이후 문제를
    재차 읽어보며 내가 잘못한 부분이 없는지 따져보았다.
'''

# 신경쓸 부분이 많은 문제인 것 같다. 한 번에 못 풀면 할복한다는 마음가짐으로 풀자.
# 도둑말은 번호가 작은 순서대로 이동. 이동 규칙이 정해져 있어 이동 위치와 여부는 로직에 의해 정해짐.
# 도둑은 이동 방향 전환이 가능. 술래는 불가능. 백트래킹을 활용해 문제에 접근하면 될 것이다.
# 순서?를 어떻게 할 수 있을까? 숫자 -> 좌표, 좌표 -> 숫자 모두 가능해야 한다.
# dictionary를 따로 하나 더 만들자. 그게 마음 편할듯?

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def in_range(row, col):
    return 0 <= row < 4 and 0 <= col < 4

def update(curr_grid, curr_dict, soolae_row, soolae_col):
    # 복사해서 진행하자.
    temp_grid = [row[:] for row in curr_grid]
    temp_dict = {k: v for k, v in curr_dict.items()}
    # 작은 숫자 순서대로 이동 진행.
    for num in sorted(list(temp_dict.keys())):
        curr_row, curr_col = temp_dict[num]
        curr_dir = temp_grid[curr_row][curr_col][1]
        
        # 현 방향 기준 돌면서 체크
        for d in range(8):
            next_dir = (curr_dir + d) % 8
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]
            
            # 만약 범위에서 벗어나거나 술래가 있는 칸은 못감
            if not in_range(next_row, next_col):
                continue
            if next_row == soolae_row and next_col == soolae_col:
                continue
            
            # 빈칸 여부에 따라 적절하게 기능 수행. 빈칸 or 도둑 말이 있는 칸으로 이동 가능하므로.
            if temp_grid[next_row][next_col] is None:
                temp_dict[num] = (next_row, next_col)
                temp_grid[next_row][next_col] = (num, next_dir)     # next_dir로 업데이트 하는게 중요!
                temp_grid[curr_row][curr_col] = None
            else:
                chage_num, chage_dir = temp_grid[next_row][next_col]
                temp_dict[chage_num] = (curr_row, curr_col)
                temp_dict[num] = (next_row, next_col)
                temp_grid[curr_row][curr_col] = temp_grid[next_row][next_col]
                temp_grid[next_row][next_col] = (num, next_dir)     # next_dir로 업데이트 하는게 중요!
            
            # 이동했으면 더 볼 필요가 없으므로 break
            break
    
    # 업데이트 결과 반환.
    return temp_grid, temp_dict

def backtrack(curr_row, curr_col, curr_dir, acc, curr_grid, curr_dict):
    global answer
    # 정답은 매번 업데이트 해주자.
    if answer < acc:
        answer = acc

    # 술래가 움직인 직후이니 grid와 dict를 업데이트 해주자
    next_grid, next_dict = update(curr_grid, curr_dict, curr_row, curr_col)

    # 최대 3칸까지 갈 수 있음.
    for k in range(1, 4):
        next_row, next_col = curr_row + dr[curr_dir] * k, curr_col + dc[curr_dir] * k

        # 범위에서 벗어나면 k값이 올라가도 벗어나므로 break
        if not in_range(next_row, next_col):
            break
        # 빈 칸이라면 술래가 갈 수 없으므로 continue
        if next_grid[next_row][next_col] is None:
            continue

        # 복원하기 위해 술래의 이동 대상이 되는 지점에 대한 정보 저장해두기.
        kill_num, kill_dir = next_grid[next_row][next_col]
        # 술래 이동 처리
        next_grid[next_row][next_col] = None
        next_dict.pop(kill_num)
        # 백트래킹 보내기
        backtrack(next_row, next_col, kill_dir, acc+kill_num, next_grid, next_dict)
        # 복원
        next_grid[next_row][next_col] = (kill_num, kill_dir)
        next_dict[kill_num] = (next_row, next_col)

def custom_print(grid, d):
    print(f'----------grid----------')
    for row in grid:
        print(*row)
    print(f'----------dict----------')
    for k, v in d.items():
        print(f'key:{k}, value:{v}')

# 문제 풀이의 핵심이 되는 두 변수 선언.
grid = []               # 좌표를 알 때, (숫자, 방향) 정보를 알기 위함.
data_dict = dict()      # 숫자를 알 때, 좌표 정보를 알기 위함.

# 입력받으며 초기 정보 잘 저장하기.
for i in range(4):
    data = list(map(int, input().split()))
    temp = []
    for j in range(4):
        num, dir = data[j<<1], data[j<<1|1]-1
        data_dict[num] = (i, j)
        temp.append((num, dir))
    grid.append(temp)

# 백트래킹을 위한 초기 세팅
temp, curr_dir = grid[0][0]
answer = grid[0][0][0]
grid[0][0] = None
data_dict.pop(temp)
backtrack(0, 0, curr_dir, temp, grid, data_dict)

print(answer)