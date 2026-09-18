# 15:04 시작
# 우리가 익히 알고 있는 2048게임 그거 하면 된다. 대신 연쇄작용 판별 정도만? 잘 하면 될듯
# 그냥 격자 자체를 돌려서 해버리자.


def rotate(d, grid):
    if d == 1: return [list(row[::-1]) for row in zip(*grid)]
    if d == 2: return [row[::-1] for row in grid[::-1]]
    if d == 3: return [list(row) for row in zip(*grid)][::-1]


def apply_gravity(grid):
    for col in range(N):
        stk, can_add = [], True
        for row in range(N-1, -1, -1):
            if grid[row][col]:
                if stk and stk[-1] == grid[row][col] and can_add:
                    stk[-1] *= 2
                    can_add = False
                else:
                    stk.append(grid[row][col])
                    can_add = True

        pointer = N-1
        for num in stk:
            grid[pointer][col] = num
            pointer -= 1

        while pointer >= 0:
            grid[pointer][col] = 0
            pointer -= 1


def backtrack(cnt, arr):
    global answer
    if cnt == 5:
        temp = max([max(row) for row in arr])
        if answer < temp:
            answer = temp
        return

    for d in range(4):
        temp_grid = [row[:] for row in arr]
        if d != 0: temp_grid = rotate(d, temp_grid)
        apply_gravity(temp_grid)
        backtrack(cnt+1, temp_grid)


def print_grid(grid):
    print(f'----grid----')
    for row in grid:
        print(*row)

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
backtrack(0, grid)
print(answer)