# 천천히 침착하게 풀자.

# 중력 적용. 합쳐질 때는 방향 선분에 가까운 순서대로 적용된다. 연쇄 X
# 5번 움직였을 때의 최대? 백트래킹 적용하면 될 듯? 비가역적 반응이라 배열은 복사 후 보내기!
# 중력 적용 및 합성 로직을 잘 구성하면 그 밖에는 다 괜찮을 듯 싶다.
# 각 방향에 대해서 굳이굳이 다 구현해야 하는가? 그냥 회전 - 중력적용 - 역회전?
# 메모리나 이런 낭비가 있을 것 같긴하다. n이 안커서 할만한 것 같기도 하고
# 문제 설명이랑 입력 조건이 좀 다르긴 하다. 설명은 2048까지, 4*4격자로 되어있는데
# 실제 입력은 격자 사이즈<=20, 1024까지 주어진다. 흠.. rotate 방식으로 해보자.

def custom_print(step, d, grid):
    print(step, d)
    for row in grid:
        print(*row)

def find_max(curr_grid):
    return max([max(row) for row in curr_grid])


def rotate(cnt, curr_grid):
    if cnt == 1:
        curr_grid = [list(row[::-1]) for row in zip(*curr_grid)]

    elif cnt == 2:
        curr_grid = [list(row[::-1]) for row in zip(*curr_grid)]
        curr_grid = [list(row[::-1]) for row in zip(*curr_grid)]

    elif cnt == 3:
        curr_grid = [list(row) for row in zip(*curr_grid)]
        curr_grid = curr_grid[::-1]

    return curr_grid


def apply_gravity(curr_grid):
    # 각 행에 대해서 진행.
    for col in range(N):
        stk = []            # 합성 기능 처리를 위함.
        can_sum = True      # 연쇄 작용 방지를 위함.
        for row in range(N-1, -1, -1):
            if curr_grid[row][col]:
                if stk and stk[-1] == curr_grid[row][col] and can_sum:
                    stk.append(stk.pop()*2)
                    can_sum = False
                else:
                    stk.append(curr_grid[row][col])
                    can_sum = True

        # stack에 있는거 순서대로 넣어주기
        pointer = N-1
        for num in stk:
            curr_grid[pointer][col] = num
            pointer -= 1
        while pointer >= 0:
            curr_grid[pointer][col] = 0
            pointer -= 1


def backtrack(step, curr_grid):
    global answer
    if step == 5:
        answer = max(answer, find_max(curr_grid))
        return

    for cnt in range(4):
        # 비가역적인 기능을 수행해야 하므로, 배열은 복사해놓고 백트래킹 보내자.
        next_grid = [row[:] for row in curr_grid]

        # 회전 - 중력 - 역회전
        next_grid = rotate(cnt, next_grid)
        apply_gravity(next_grid)
        next_grid = rotate((4-cnt)%4, next_grid)

        # 백트래킹 보내기.
        backtrack(step+1, next_grid)


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
backtrack(0, grid)
print(answer)