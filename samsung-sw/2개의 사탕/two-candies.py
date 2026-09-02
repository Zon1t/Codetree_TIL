''' 2개의 사탕 / 20260902 / 체감 난이도 : 골드 4
소요 시간 : 40분 / 시도 : 1회 / 실행 시간 : 2248ms(이 정도면 사실상 틀린거 아닌가?) / 메모리 : 31MB

타임 라인 : 구상 및 틀 만들기(9분) - 구현(23분) - 검증(8분)


[구상]
    - 백트래킹으로 해결해야 하는 문제임을 곧바로 떠올릴 수 있었다. 다만 사탕을 밖으로 빼기의 성공 조건이
    까다롭다고 생각했기에, 이를 적절하게 처리해주는 방식에 대해서 고민을 해보았다.
    - 시간 복잡도에 대해서 그리고 가지치기 조건에 대해서 간략하게 떠올려봤을 때 아주 큰 문제가 될 것 같지
    않았어서 곧바로 문제 풀이를 진행해보았다.

[구현]
    - 가지치기나 종료 조건에 대해서 고민을 많이 해보았다. 어쨋든 매번 배열 복사하고 넘기고 중력 적용하고
    등등 수행하려니 시간 내로 통과 못하진 않을지라도 실행시간과 메모리를 적게 써서 풀고싶은 마음이 있었다.
    - simulate 함수에서 분기문을 줄일 수 있을 것이라 생각하긴 했는데, 괜히 헷갈릴까봐 기세로 모든 경우
    를 다 작성해보았다. 그 밖에는 크게 신경 쓴 부분은 없었던 것 같다.

[검증]
    - 종료 조건, 가지치기 조건이 적절한지 + 매 시행마다 적절하게 grid를 찍어내는지 체크해보았다. 중간에
    and/or을 완전히 잘못 적은 부분이 있어서 해당 부분만 수정하니 문제 없이 잘 돌아갔었다.
    - 문제 재차 읽고, 조건 반영 잘했는지 따져보고 제출해보았다.


*피드백
    - 남들 실행 시간/메모리를 보니 완전 작더라. 남들 코드 안보고 최대한 시간/메모리 줄여보기.
'''

# 2048문제 풀던 방식과 비슷? 중력 적용 정도로 하면 될 것 같다. 10번 이내이니
# 4^10 -> 나름 여유로울 것으로 예상? 제한도 넉넉하게 줬음.
# 잘 생각해야 할 부분 : 파랑이 먼저 나오는 것 X, 동시에 나오는 것 X, 벽에 닿는 것 처리 잘하기 정도?
# 사탕 좌표 정도는 저장해두는 편이 좋을 것 같다. 기울일 때 주의 사항? 바닥면에 가까운 애들 먼저 떨구기
# 전부 장애물로 막혀있다는 조건이 있다. inrange 확인은 안해도 될듯.

def move(object, direction):
    curr_row, curr_col = object
    curr_object = grid[curr_row][curr_col]
    grid[curr_row][curr_col] = 0
    next_row, next_col = curr_row + dr[direction], curr_col + dc[direction]
    while True:
        # 적절한 분기처리
        if grid[next_row][next_col] in [-1, 1, 2]:
            grid[next_row-dr[direction]][next_col-dc[direction]] = curr_object
            return (next_row-dr[direction], next_col-dc[direction])
        elif grid[next_row][next_col] == 3:
            return (-1, -1)
        # 빈칸이면 탐험 계속하기
        next_row += dr[direction]
        next_col += dc[direction]

# 기세로 가자.
def simulate(direction, curr_red, curr_blue):
    if direction==0:
        if curr_red[1] < curr_blue[1]:
            next_blue = move(curr_blue, direction)
            next_red = move(curr_red, direction)
        else:
            next_red = move(curr_red, direction)
            next_blue = move(curr_blue, direction)
    elif direction==1:
        if curr_red[0] < curr_blue[0]:
            next_blue = move(curr_blue, direction)
            next_red = move(curr_red, direction)
        else:
            next_red = move(curr_red, direction)
            next_blue = move(curr_blue, direction)
    elif direction==2:
        if curr_red[1] > curr_blue[1]:
            next_blue = move(curr_blue, direction)
            next_red = move(curr_red, direction)
        else:
            next_red = move(curr_red, direction)
            next_blue = move(curr_blue, direction)
    else:
        if curr_red[0] > curr_blue[0]:
            next_blue = move(curr_blue, direction)
            next_red = move(curr_red, direction)
        else:
            next_red = move(curr_red, direction)
            next_blue = move(curr_blue, direction)
    return next_red, next_blue

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = []
    temp = list(input())
    for ch in temp:
        if ch == '.':
            row.append(0)
        elif ch == '#':
            row.append(-1)
        elif ch == 'R':
            row.append(1)
        elif ch == 'B':
            row.append(2)
        else:
            row.append(3)
    grid.append(row)

red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
for row in range(N):
    for col in range(M):
        if grid[row][col] == 1:
            red_row, red_col = row, col
        if grid[row][col] == 2:
            blue_row, blue_col = row, col

def backtrack(cnt, curr_red, curr_blue):
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
        # 왜 복사해서 보낼 생각을 했을까 흠..
        next_red, next_blue = simulate(d, curr_red, curr_blue)

        backtrack(cnt+1, next_red, next_blue)

        if next_red[0] != -1:
            grid[next_red[0]][next_red[1]] = 0
        if next_blue[0] != -1:
            grid[next_blue[0]][next_blue[1]] = 0

        grid[curr_red[0]][curr_red[1]] = 1
        grid[curr_blue[0]][curr_blue[1]] = 2

answer = -1
backtrack(0, (red_row, red_col), (blue_row, blue_col))
print(answer)