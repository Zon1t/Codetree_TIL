# grow -> burnsick -> find - fire(update)
# 격자에 대한 연산을 미리미리 해두면 좋을 것 같다.

# 십자
dr1 = [0, 1, 0, -1]
dc1 = [1, 0, -1, 0]

# 대각
dr2 = [-1, 1, 1, -1]
dc2 = [1, 1, -1, -1]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def grow():
    for row in range(N):
        for col in range(N):
            if grid[row][col] > 0:
                burnsick_table.clear()

                cnt, empty = 0, 0
                for d in range(4):
                    nr, nc = row + dr1[d], col + dc1[d]
                    if not in_range(nr, nc) or grid[nr][nc] == -1 or check_table[nr][nc] >= t:
                        continue

                    if grid[nr][nc] == 0:
                        empty += 1
                        burnsick_table.append((nr, nc))
                    else:
                        cnt += 1

                if cnt:
                    grid[row][col] += cnt
                if empty:
                    burnsick_cnt = grid[row][col] // empty
                    for br, bc in burnsick_table:
                        burnsick_dict[(br, bc)] = burnsick_dict.get((br, bc), 0) + burnsick_cnt

def burnsick():
    for (row, col), cnt in burnsick_dict.items():
        grid[row][col] += cnt
    burnsick_dict.clear()

def find():
    max_cnt = 0
    target_row, target_col = -1, -1
    for row in range(N):
        for col in range(N):

            if grid[row][col] < 1:
                continue

            temp = grid[row][col]
            for d in range(4):
                for k in range(1, L+1):
                    next_row, next_col = row + dr2[d] * k, col + dc2[d] * k
                    if not in_range(next_row, next_col) or grid[next_row][next_col] < 1:
                        break
                    temp += grid[next_row][next_col]

            if temp > max_cnt:
                target_row, target_col = row, col
                max_cnt = temp

    return target_row, target_col

def kill_update(row, col):
    global answer

    rip_day = t+Y
    answer += grid[row][col]
    grid[row][col] = 0
    check_table[row][col] = rip_day
    for d in range(4):
        for k in range(1, L+1):
            next_row, next_col = row + dr2[d] * k, col + dc2[d] * k

            if not in_range(next_row, next_col) or grid[next_row][next_col] == -1:
                break
            if grid[next_row][next_col] == 0:
                check_table[next_row][next_col] = rip_day
                break

            answer += grid[next_row][next_col]
            grid[next_row][next_col] = 0
            check_table[next_row][next_col] = rip_day


def custom_print():
    print(t)
    print('-------------------')
    for row in check_table:
        print(*row)
    print('-------------------')
    for row in grid:
        print(*row)
    print('-------------------')


# 격자 size, simulation 진행 턴 수, 확산 범위, 제초제가 남아있는 년수
N, T, L, Y = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 필요 변수 선언.
check_table = [[-1] * N for _ in range(N)]       # 교차 검증시 사용. 새로 뿌려지면 초기화라서

answer = 0
burnsick_dict, burnsick_table = dict(), []
for t in range(T):

    # 1. 나무 성장시키기.
    grow()

    # 2. 나무 번식시키기.
    burnsick()

    # 3. 살포 위치 찾기
    row, col = find()
    if row != -1:
        # 찾으면 업데이트
        kill_update(row, col)
    else:
        break

print(answer)