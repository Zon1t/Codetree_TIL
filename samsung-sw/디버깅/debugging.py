# 그럴듯한? 풀이 방법이 떠오르지 않는다.. grid로 입력 받고
# 뭔가 논리적으로 풀 수 있을 것 같은 문제긴 한데, 완탐으로 해야 할 것도 같다.
# 완전 탐색이 이루어질 수 있는 사이즈인가? 300C3.. 될 것 같기도 하고?
# 그냥 백트래킹 쓰자.

def backtrack(row, cnt, prev, human, apply):
    global answer

    # 진행 X
    if answer <= cnt or cnt == 4:
        return

    # 정답 체크
    if row == N:
        if human == target:
            if cnt < answer:
                answer = cnt
        return

    # 코드 꼬이게 하는 만악의 근원
    if apply == 0:
        for col in default[row]:
            human[col], human[col+1] = human[col+1], human[col]

    # 고르기
    for col in possible[row]:
        if col <= prev+1:
            continue

        human[col], human[col+1] = human[col+1], human[col]
        # 같은 열에서 더 고르기
        backtrack(row, cnt+1, col, human, 1)
        human[col], human[col+1] = human[col+1], human[col]

    # 현재 열에서 안고른 경우
    backtrack(row+1, cnt, -2, human, 0)

    # 이것까지.. 해줘야한다.. 이거때매 몇분을 버렸냐
    if apply == 0:
        for col in default[row]:
            human[col], human[col + 1] = human[col + 1], human[col]


M, K, N = map(int, input().split())
grid = [[0] * (M-1) for _ in range(N)]
default = [[] for _ in range(N)]
for _ in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    grid[r][c] = 1
    default[r].append(c)

possible = [[] for _ in range(N)]
for row in range(N):
    for col in range(M-1):
        left = True if col == 0 or grid[row][col-1] == 0 else False
        right = True if col == M-2 or grid[row][col+1] == 0 else False
        if left and right and col not in default[row]:
            possible[row].append(col)

answer = 300
target = list(range(1, M+1))
backtrack(0, 0, -2, list(range(1, M+1)), 0)

print(answer if answer != 300 else -1)