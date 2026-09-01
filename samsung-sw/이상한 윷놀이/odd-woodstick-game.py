# 굉장히 귀찮은 문제이다. 이동 대상 칸 색상별 구분 잘해서 분기문 짜기.
# 파랑색 or 격자 경계의 경우 처리가 중요할 듯 싶다. 파랑을 만나 방향을 바꿨다. 이후 격자 밖으로 가려고
# 한다면 음..방향만 또 바꾸나? 그냥 그대로 두나?
# 말이 4개 이상 겹쳐지는지 매턴 확인할 필요가 있다.
# 음.. 12by12면 그냥 격자 그리기 + dict[idx] = data ~ 이런 느낌으로 관리해보면 어떨까?

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def move(idx):
    row, col, dir = data_dict[idx]

    start = -1
    for pos, num in enumerate(grid[row][col]):
        if num == idx:
            start = pos
            break

    move_object = grid[row][col][start:]
    grid[row][col] = grid[row][col][:start]

    next_row, next_col = row + dr[dir], col + dc[dir]
    if not in_range(next_row, next_col) or pan[next_row][next_col] == 2:
        next_dir = dir ^ 1
        next_row, next_col = row + dr[next_dir], col + dc[next_dir]
        if not in_range(next_row, next_col) or pan[next_row][next_col] == 2:
            next_row, next_col = row, col
            grid[next_row][next_col].extend(move_object)
        else:
            if pan[next_row][next_col] == 0:
                grid[next_row][next_col].extend(move_object)
            elif pan[next_row][next_col] == 1:
                grid[next_row][next_col].extend(move_object[::-1])
        data_dict[idx][2] = next_dir
    elif pan[next_row][next_col] == 0:
        grid[next_row][next_col].extend(move_object)
    else:
        grid[next_row][next_col].extend(move_object[::-1])

    for i in move_object:
        data_dict[i][0], data_dict[i][1] = next_row, next_col

    return len(grid[next_row][next_col]) >= 4

def custom_print():
    print(f'---------grid----------')
    for row in grid:
        print(*row)
    print(f'---------dict----------')
    for k in data_dict:
        print(f'k:{k}, value:{data_dict[k]}')

# 데이터 입력받기.
N, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# 적절한 변수들을 활용하여 입력받은 데이터 정리하기.
grid = [[[] for _ in range(N)] for _ in range(N)]
data_dict = dict()
for idx in range(1, K+1):
    x, y, d = map(lambda x: int(x)-1, input().split())
    data_dict[idx] = [x, y, d]
    grid[x][y].append(idx)

answer = -1
# 이상한 윷놀이 진행.
for turn in range(1, 1001):
    for idx in range(1, K+1):
        stop = move(idx)
        if stop:
            break
    else:
        continue

    answer = turn
    break

print(answer)