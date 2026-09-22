# 12:02 시작
# 시작 좌표를 기준으로, 아래 / 옆으로 블럭 떨구면 된다.
# 옆으로 떨구는거 따로 만들기 귀찮으니 전치 시켜서 생각하면 될 것.
# 이때 블럭 타입도 적절하게 바꾸어 주어야 한다.
# 점수 업뎃 하는 것도 주의해서 잘해주기.


def drop(t, c, grid):
    curr_row = 1
    if t == 2:
        while True:
            curr_row += 1
            if curr_row == 6 or grid[curr_row][c] or grid[curr_row][c+1]:
                grid[curr_row-1][c] = grid[curr_row-1][c+1] = 1
                break
    else:
        while True:
            curr_row += 1
            if curr_row == 6 or grid[curr_row][c]:
                grid[curr_row-1][c] = 1
                if t == 3:
                    grid[curr_row-2][c] = 1
                break


def update(grid):
    temp = 0
    for row in range(5, -1, -1):
        while sum(grid[row]) == 4:
            temp += 1
            grid.pop(row)
            grid.insert(0, [0, 0, 0, 0])

    pop_cnt = 0
    for row in range(2):
        for col in range(4):
            if grid[row][col]:
                pop_cnt += 1
                break

    for _ in range(pop_cnt):
        grid.pop()
        grid.insert(0, [0, 0, 0, 0])

    return temp


def print_grid(what, grid):
    print(f'----{what}_grid----')
    for row in grid:
        print(*row)


# ====================================
# 세팅

N = int(input())
yellow = [[0] * 4 for _ in range(6)]
redred = [[0] * 4 for _ in range(6)]

# ====================================
# 실행부

answer = 0
for _ in range(N):
    t, x, y = map(int, input().split())

    # 1. 블럭 떨구기
    drop(t, y, yellow)
    drop(t if t == 1 else 5-t, x, redred)

    # 2. 정보 업데이트
    answer += update(yellow)
    answer += update(redred)

# 정답 출력
print(answer)
print(sum([sum(row) for row in yellow]) + sum([sum(row) for row in redred]))