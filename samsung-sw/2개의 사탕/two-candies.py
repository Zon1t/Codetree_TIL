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

def move(blue, red, direction, blue_first):
    if blue_first:
        next_blue = blue + deltas[direction]
        while True:
            # 적절한 분기처리
            if grid[next_blue] == '#':
                next_blue = next_blue-deltas[direction]
                break
            elif grid[next_blue] == 'O':
                next_blue = -1
                break
            next_blue += deltas[direction]

        next_red = red + deltas[direction]
        while True:
            # 적절한 분기처리
            if grid[next_red] == '#' or next_red == next_blue:
                next_red = next_red-deltas[direction]
                break
            elif grid[next_red] == 'O':
                next_red = -1
                break
            next_red += deltas[direction]
    else:
        next_red = red + deltas[direction]
        while True:
            # 적절한 분기처리
            if grid[next_red] == '#':
                next_red = next_red - deltas[direction]
                break
            elif grid[next_red] == 'O':
                next_red = -1
                break
            next_red += deltas[direction]

        next_blue = blue + deltas[direction]
        while True:
            # 적절한 분기처리
            if grid[next_blue] == '#' or next_blue == next_red:
                next_blue = next_blue - deltas[direction]
                break
            elif grid[next_blue] == 'O':
                next_blue = -1
                break
            next_blue += deltas[direction]

    return next_red, next_blue

# 기세로 가자.
def simulate(direction, curr_red, curr_blue):
    if direction==0:
        return move(curr_blue, curr_red, direction, curr_red%M < curr_blue%M)
    elif direction==1:
        return move(curr_blue, curr_red, direction, curr_red//M < curr_blue//M)
    elif direction==2:
        return move(curr_blue, curr_red, direction, curr_red%M > curr_blue%M)
    else:
        return move(curr_blue, curr_red, direction, curr_red//M > curr_blue//M)


N, M = map(int, input().split())
grid = ''
for i in range(N):
    grid += input()

deltas = (1, M, -1, -M)
size = N*M

red, blue = -1, -1
for i in range(size):
    if grid[i] == 'R':
        red = i
    elif grid[i] == 'B':
        blue = i

def backtrack(cnt, curr_red, curr_blue):
    global answer
    # 동시에 들어가는 것조차 안되니까
    if curr_blue == -1:
        return
    # 가지치기? 하는 편이 좋겠지?
    if answer != -1 and answer <= cnt:
        return

    # 파랑도 들어갔으면 위에서 return. 빨강만 들어간 경우임.
    if curr_red == -1:
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

        for i in range(cnt+1):
            if (next_red, next_blue) in data[cnt]:
                break
        else:
            data[cnt].add((next_red, next_blue))
            backtrack(cnt+1, next_red, next_blue)

answer = -1
data = [set() for _ in range(10)]
data[0].add((red, blue))
backtrack(0, red, blue)
print(answer)