# 10:42 시작 [] /
# 클래스로 해봐도 될 것 같고.. 근데 굳이 싶긴하다.
# 튜플 비교로 공격자 피격자 잘 찾고, 공격로직 올바르게 만들면 되겠다.

from collections import deque

dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]
INF = float('inf')

def find():
    attack, target = (INF, 0, 0, 0), (-INF, 0, 0, 0)
    for row in range(N):
        for col in range(M):
            if not grid[row][col]:
                continue
            curr_tower = (grid[row][col], -last_attack[row][col], -row-col, -col)
            attack = min(curr_tower, attack)
            target = max(curr_tower, target)

    return attack[3]-attack[2], -attack[3], target[3]-target[2], -target[3]


def plan_a():
    dist_grid = [[-1] * M for _ in range(N)]
    dist_grid[target_row][target_col] = 0

    Q = deque([(target_row, target_col)])
    while Q:
        curr_row, curr_col = Q.popleft()
        for d in range(4):
            next_row, next_col = (curr_row+dr[d])%N, (curr_col+dc[d])%M
            if dist_grid[next_row][next_col] != -1 or not grid[next_row][next_col]:
                continue
            dist_grid[next_row][next_col] = dist_grid[curr_row][curr_col]+1
            Q.append((next_row, next_col))

    if dist_grid[attack_row][attack_col] == -1:
        return False

    # 공격 시작
    curr_row, curr_col = attack_row, attack_col
    damage, half_damage = grid[curr_row][curr_col], grid[curr_row][curr_col]>>1
    while True:
        parts.add((curr_row, curr_col))
        if curr_row == target_row and curr_col == target_col:
            grid[curr_row][curr_col] = max(0, grid[curr_row][curr_col]+half_damage-damage)
            break
        for d in range(4):
            next_row, next_col = (curr_row + dr[d])%N, (curr_col + dc[d])%M
            if dist_grid[next_row][next_col] == dist_grid[curr_row][curr_col]-1:
                grid[next_row][next_col] = max(0, grid[next_row][next_col]-half_damage)
                curr_row, curr_col = next_row, next_col
                break
    return True


def plan_b():
    parts.add((attack_row, attack_col))
    damage, half_damage = grid[attack_row][attack_col], grid[attack_row][attack_col]>>1
    for d in range(8):
        next_row, next_col = (target_row+dr[d])%N, (target_col+dc[d])%M
        if not grid[next_row][next_col] or (next_row == attack_row and next_col == attack_col):
            continue
        grid[next_row][next_col] = max(0, grid[next_row][next_col]-half_damage)
        parts.add((next_row, next_col))
    parts.add((target_row, target_col))
    grid[target_row][target_col] = max(0, grid[target_row][target_col]-damage)


def repair():
    for row in range(N):
        for col in range(M):
            if not grid[row][col] or (row, col) in parts:
                continue
            grid[row][col] += 1
    parts.clear()


def print_grid():
    print('----grid----')
    for row in grid:
        print(*row)


# ===================================================================
# 세팅

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
last_attack = [[-1]*M for _ in range(N)]
add_value = N+M
parts = set()

# ===================================================================
# 실행부

for turn in range(K):
    # 1. 공격자 및 피격자 찾기
    attack_row, attack_col, target_row, target_col = find()
    if attack_row == target_row and attack_col == target_col:
        print(grid[attack_row][attack_col])
        break

    # 2. 공격 개시
    grid[attack_row][attack_col] += add_value
    last_attack[attack_row][attack_col] = turn
    if not plan_a():
        plan_b()

    # 3. 무관한 애들 고치기.
    repair()

else:
    print(max([max(row) for row in grid]))