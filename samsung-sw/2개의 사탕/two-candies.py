# 2048문제 풀던 방식과 비슷? 중력 적용 정도로 하면 될 것 같다. 10번 이내이니
# 4^10 -> 나름 여유로울 것으로 예상?
# 잘 생각해야 할 부분 : 파랑이 먼저 나오는 것 X, 동시에 나오는 것 X, 벽에 닿는 것 처리 잘하기 정도?
# 사탕 좌표 정도는 저장해두는 편이 좋을 것 같다. 기울일 때 주의 사항? 바닥면에 가까운 애들 먼저 떨구기
# 전부 장애물로 막혀있다는 조건이 있다. inrange 확인은 안해도 될듯.

def move(object, direction, curr_grid):
    curr_row, curr_col = object
    next_row, next_col = curr_row + dr[direction], curr_col + dc[direction]
    curr_object = curr_grid[curr_row][curr_col]
    curr_grid[curr_row][curr_col] = '.'
    while True:
        # 적절한 분기처리
        if curr_grid[next_row][next_col] in ['#', 'R', 'B']:
            curr_grid[next_row-dr[direction]][next_col-dc[direction]] = curr_object
            return (next_row-dr[direction], next_col-dc[direction])
        elif curr_grid[next_row][next_col] == 'O':
            return (-1, -1)
        # 빈칸이면 탐험 계속하기
        next_row += dr[direction]
        next_col += dc[direction]

# 기세로 가자.
def simulate(direction, curr_red, curr_blue, curr_grid):
    if direction==0:
        if curr_red[1] < curr_blue[1]:
            next_blue = move(curr_blue, direction, curr_grid)
            next_red = move(curr_red, direction, curr_grid)
        else:
            next_red = move(curr_red, direction, curr_grid)
            next_blue = move(curr_blue, direction, curr_grid)
    elif direction==1:
        if curr_red[0] < curr_blue[0]:
            next_blue = move(curr_blue, direction, curr_grid)
            next_red = move(curr_red, direction, curr_grid)
        else:
            next_red = move(curr_red, direction, curr_grid)
            next_blue = move(curr_blue, direction, curr_grid)
    elif direction==2:
        if curr_red[1] > curr_blue[1]:
            next_blue = move(curr_blue, direction, curr_grid)
            next_red = move(curr_red, direction, curr_grid)
        else:
            next_red = move(curr_red, direction, curr_grid)
            next_blue = move(curr_blue, direction, curr_grid)
    else:
        if curr_red[0] > curr_blue[0]:
            next_blue = move(curr_blue, direction, curr_grid)
            next_red = move(curr_red, direction, curr_grid)
        else:
            next_red = move(curr_red, direction, curr_grid)
            next_blue = move(curr_blue, direction, curr_grid)
    return next_red, next_blue

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
for row in range(N):
    for col in range(M):
        if grid[row][col] == 'R':
            red_row, red_col = row, col
        if grid[row][col] == 'B':
            blue_row, blue_col = row, col

def backtrack(cnt, curr_red, curr_blue, curr_grid):
    global answer
    # 동시에 들어가는 것조차 안되니까
    if curr_blue[0] == -1:
        return
    # 가지치기? 하는 편이 좋겠지?
    if answer != -1 and answer <= cnt:
        return

    # 파랑도 들어갔으면 위에서 return. 빨강만 들어간 경우임.
    if curr_red[0] == -1:
        # 만약 제때 들어갔다면 최소 업데이트
        if answer == -1 or cnt < answer:
            answer = cnt
        # 더 확인하는 게 의미가 없다.
        return

    # 더 진행 불가능하니 반환
    if cnt == 10:
        return

    # 각 방향에 대해서 중력 적용.
    for d in range(4):
        next_grid = [row[:] for row in curr_grid]
        next_red, next_blue = simulate(d, curr_red, curr_blue, next_grid)
        backtrack(cnt+1, next_red, next_blue, next_grid)

answer = -1
backtrack(0, (red_row, red_col), (blue_row, blue_col), grid)
print(answer)