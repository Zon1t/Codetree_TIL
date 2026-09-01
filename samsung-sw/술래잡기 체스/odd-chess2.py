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
    temp_grid = [row[:] for row in curr_grid]
    temp_dict = {k: v for k, v in curr_dict.items()}
    for num in sorted(list(temp_dict.keys())):
        curr_row, curr_col = temp_dict[num]
        curr_dir = temp_grid[curr_row][curr_col][1]

        for d in range(8):
            next_dir = (curr_dir + d) % 8
            next_row, next_col = curr_row + dr[next_dir], curr_col + dc[next_dir]

            if not in_range(next_row, next_col):
                continue
            if next_row == soolae_row and next_col == soolae_col:
                continue

            if temp_grid[next_row][next_col] is None:
                temp_dict[num] = (next_row, next_col)
                temp_grid[next_row][next_col] = (num, next_dir)
                temp_grid[curr_row][curr_col] = None
            else:
                chage_num, chage_dir = temp_grid[next_row][next_col]
                temp_dict[chage_num] = (curr_row, curr_col)
                temp_dict[num] = (next_row, next_col)
                temp_grid[curr_row][curr_col] = temp_grid[next_row][next_col]
                temp_grid[next_row][next_col] = (num, next_dir)
            break

    return temp_grid, temp_dict

def backtrack(curr_row, curr_col, curr_dir, acc, curr_grid, curr_dict):
    global answer
    if answer < acc:
        answer = acc

    next_grid, next_dict = update(curr_grid, curr_dict, curr_row, curr_col)
    # custom_print(next_grid, next_dict)
    # print(curr_row, curr_col, curr_dir, acc)
    for k in range(1, 4):
        next_row, next_col = curr_row + dr[curr_dir] * k, curr_col + dc[curr_dir] * k

        if not in_range(next_row, next_col):
            break
        if next_grid[next_row][next_col] is None:
            continue

        kill_num, kill_dir = next_grid[next_row][next_col]
        next_grid[next_row][next_col] = None
        next_dict.pop(kill_num)
        backtrack(next_row, next_col, kill_dir, acc+kill_num, next_grid, next_dict)
        next_grid[next_row][next_col] = (kill_num, kill_dir)
        next_dict[kill_num] = (next_row, next_col)

def custom_print(grid, d):
    print(f'----------grid----------')
    for row in grid:
        print(*row)
    print(f'----------dict----------')
    for k, v in d.items():
        print(f'key:{k}, value:{v}')

grid = []
data_dict = dict()
for i in range(4):
    data = list(map(int, input().split()))
    temp = []
    for j in range(4):
        num, dir = data[j<<1], data[j<<1|1]-1
        data_dict[num] = (i, j)
        temp.append((num, dir))
    grid.append(temp)

temp, curr_dir = grid[0][0]
answer = grid[0][0][0]
grid[0][0] = None
data_dict.pop(temp)
backtrack(0, 0, curr_dir, temp, grid, data_dict)

print(answer)