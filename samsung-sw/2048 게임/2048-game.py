''' 2048게임 / 20260831 / 체감 난이도 : 골드 4~5
소요 시간 : 47분 / 제출 시도 : 1회 / 실행 시간 : 202ms / 메모리 : 23MB

타임 라인 : 구상 및 틀 만들기(14분) - 구현(22분) - 검증(11분)


[구상]
    - 입력 데이터 조건과 문제에서 말하는 조건이 서로 달랐다. 문제는 다음과 같았다.
        '2, 4, 8, 16 등 2의 거듭제곱꼴로 나타나는 2 이상 2048 이하의 숫자들로 구성된 4 * 4 격자 판이
        주어졌을 때, 5번 움직인 이후에 격자판에서 가장 큰 값의 최댓값을 구하는 프로그램을 작성해보세요.'
      하지만 입력 데이터 조건은 n <= 20으로 달랐어서 회전 등의 로직을 구성할 때 아낄 수 있는 방식으로
      짜야 하는가에 대해서 고민을 좀 했던 것 같다.
    - 필요한 기능들을 분리해 함수와 변수를 정의했다. 전체적인 틀을 짜기 전까진 구현을 시작하지 않았다.
    - 합쳐지고 중력 적용된 격자를 되돌리기란 불가능하므로 배열은 복사 후 넘겨주기로 했다.

[구현]
    - temp.py 파일을 만들어 기능별로 테스트를 진행해보았다.
    - 처음 계획했던 것은 apply_gravity 함수에 진짜 중력만을 적용하는 다음과 같은 코드가 있었다.
    ----------------------------------------
        def apply_gravity(curr_grid):
            for col in range(N):
                pointer = N-1
                for row in range(N-1, -1, -1):
                    if curr_grid[row][col] != 0:
                        if pointer != row:
                            curr_grid[pointer][col], curr_grid[row][col] = curr_grid[row][col], curr_grid[pointer][col]
                        pointer -= 1
    ----------------------------------------
    잘 생각해보니 합쳐지는 로직으로 인해 쓸모가 없다는 것을 뒤늦게 깨달았다. 충분히 미리 생각해볼 수 있는
    부분이라 생각했는데 이러한 부분을 좀 신결쓸 필요가 있겠다.

[검증]
    - 테케 정답이 잘 나오는 것을 확인한 후 매 단계, 매 기능을 수행해보며 결과를 출력해보았다.
    - 중간에 합쳐지는 부분에서 바닥 선분 쪽이 아닌 반대에서 먼저 합쳐지는 현상을 발견했는데, 스택의 특성을
    고려하지 않고 while문으로 pop하면서 grid에 써적었었다. 올바른 순서로 적기 위해, for문으로 바꾸고 다시
    검증한 뒤레 제출하였다.
'''

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
        curr_grid = curr_grid[::-1]
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

        # 회전 - 중력 - 역회전? 잘 생각해보면 역회전이 필요한가?
        next_grid = rotate(cnt, next_grid)
        apply_gravity(next_grid)
        # next_grid = rotate((4-cnt)%4, next_grid)

        # 백트래킹 보내기.
        backtrack(step+1, next_grid)


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
backtrack(0, grid)
print(answer)