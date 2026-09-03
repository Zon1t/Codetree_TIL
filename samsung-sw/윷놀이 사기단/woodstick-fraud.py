# 윷놀이 판을 어떻게 구성해야 할까? lst 4개를 만들어 grid를 업데이트 하는 방식으로
# 진행하면 좋을 것 같다.
# 던질 수 있는 횟수 10회 / 최댓값 구하는 문제. 4^10 정도? 백트래킹 하면 되겠다.
# 이동 불가능함 관리 -> 말의 위치를 저장하는 data_lst로 관리. 있으면 못가고 등등~
# 가지치기 조건 없나? 머리 아프니까 한 번 초기화 하고 가자.
# 원하는 이동 횟수 -> 이거 뭔말임??

grid = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40]]
cnts = list(map(int, input().split()))

grid_length = [len(row) for row in grid]
chage_set = {10, 20, 30}
check_set = {25, 35, 40}

# 집합 찍어보기
# for i in range(4):
#     for j in range(i):
#         print(f'--------intersection{i, j}---------')
#         print(set(grid[i]).intersection(set(grid[j])))

# 말의 정보를 받는 lst
info = [[0, 0] for _ in range(4)]

def check(grid_idx, pos, mal_idx):
    for another_idx in range(4):
        if mal_idx == another_idx:
            continue

        mal_grid, mal_pos = info[another_idx][0], info[another_idx][1]
        if mal_pos == -1:
            continue
        if mal_grid == grid_idx and mal_pos == pos:
            return False
        if grid[mal_grid][mal_pos] == grid[grid_idx][pos]:
            if grid[grid_idx][pos] in check_set:
                return False
            if grid[grid_idx][pos] == 30 and (pos != 0 and mal_pos != 0):
                return False
    return True

def backtrack(turn, acc):
    global answer
    if turn == 10:
        if answer < acc:
            answer = acc
        return

    for mal_idx in range(4):
        grid_idx, curr_pos = info[mal_idx][0], info[mal_idx][1]
        if curr_pos == -1:
            continue

        next_pos = curr_pos + cnts[turn]
        if next_pos >= grid_length[grid_idx]:   # 그냥 continue해도 될 것 같은데 혹시 모르니..
            info[mal_idx][1] = -1
            backtrack(turn+1, acc)
            info[mal_idx][1] = curr_pos
            continue

        if grid_idx == 0 and (grid[0][next_pos] in chage_set):
            if check(grid[0][next_pos]//10, 0, mal_idx):
                info[mal_idx] = [grid[0][next_pos]//10, 0]
                backtrack(turn+1, acc+grid[0][next_pos])
                info[mal_idx] = [0, curr_pos]
        else:
            if check(grid_idx, next_pos, mal_idx):
                info[mal_idx][1] = next_pos
                backtrack(turn+1, acc+grid[grid_idx][next_pos])
                info[mal_idx][1] = curr_pos

answer = 0
backtrack(0, 0)
print(answer)
