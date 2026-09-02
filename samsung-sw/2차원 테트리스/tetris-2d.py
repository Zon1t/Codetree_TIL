''' 2차원 테트리스 / 20260902 / 체감 난이도 : 골드 5
소요 시간 : 50분 / 시도 : 1회 / 실행 시간 : 258ms / 메모리 : 23MB

타임 라인 : 구상 및 틀 만들기(17분) - 구현(12분) - 디버깅 및 검증(21분)


[구상]
    - 블럭의 가짓수가 굉장히 적어서 다행이라고 생각했다. 모양도 단순해서 직접 떨궈보며 grid에
    그려가면 될 것이라 판단했다.
    - 노란 격자와 빨간 격자를 구분해서 구현하려니 너무 복잡하다고 생각했다. 방향만 다르시 사실
    작용하는 기능이나 원리는 똑같기 때문에 빨간 격자를 90도 돌려서 생각하기로 했다.

[구현]
    - 구현하면서 크게 어려운 부분은 없었던 것 같다. 기능별로 어떻게 구현해야 할 지 미리 생각하
    고 들어갔기 때문에 금방금방 코드를 짤 수 있었다.
    - 기능별로 어느 정도 구현이 되었다고 생각한 순간 custom_print 함수를 정의하고 디버깅에
    들어갔다. 이런 부류의 문제는 직접 찍어보며 내 의도한 바 올바르게 수행하는지 체크하는 편이
    마음에 편한 것 같다.

[검증]
    - 잘못 구현했던 부분과 수정 사항은 다음과 같다.
        1. 빨간 격자에 블럭을 떨굴 때 3번 블럭 -> 2번 블럭으로 바꿔서 진행해주었다. 해당 과
       정에서 바라봐야 하는 column 인자가 1만큼씩 차인 난다는 것을 생각하지 못했다.
        2. 전역 변수 관리. grid를 업데이트할 때, "grid = [[0, 0, 0, 0]] + grid"라는
       코드로 진행했는데, global 변수를 선언하던가 그냥 배열 insert를 하던가 해야했다. 이를
       망각해서 업데이트가 똑바로 진행되지 않았었다. 이 과정에서 연한 부분 깎는 로직도 수정하
       게 되었다.
    - custom_print 출력 결과와 예제를 비교하면서 틀린 부분을 역추적하니 금방금방 발견하고 수
    정할 수 있었던 것 같다.
'''

# 테트리스 문제. 내가 놓는 블럭이 노란, 빨간색 격자로 떨어지게 된다.
# 타일의 종류는 3가지. delta 연산을 통해 블럭을 저장하면 될 듯 싶다.
# 떨어지는 로직을 2개 구현하기는 힘들어보인다. 따라서 빨간색은 그냥 90도 회전한 상태라고 가정한 후
# 관리하면 될 듯 싶다. 지워지면 각 줄당 1점. 격자 밖으로 삐져나가는 경우(연한 칸) 적절하게 체크 후
# 넘어가야 한다. 그냥 격자 직접 그려가면서 관리하면 편할 듯?
# 최대 10000번 수행하는 데 음.. 괜찮을 듯 싶다?

# 빨간 격자에 떨굴 때 필요한 대응관계
to_red = {1: 1, 2: 3, 3: 2}

# 블럭을 떨구는 로직
def apply_gravity(block_type, curr_col, grid):
    global answer1
    curr_row = 1
    if block_type == 2:
        while True:
            if curr_row == 6 or grid[curr_row][curr_col] or grid[curr_row][curr_col+1]:
                grid[curr_row-1][curr_col] = grid[curr_row-1][curr_col+1] = 1
                if sum(grid[curr_row-1]) == 4:
                    grid.pop(curr_row-1)
                    grid.insert(0, [0, 0, 0, 0])
                    answer1 += 1
                return
            curr_row += 1
    else:
        while True:
            if curr_row == 6 or grid[curr_row][curr_col]:
                grid[curr_row-1][curr_col] = 1
                if block_type == 1:
                    if sum(grid[curr_row-1]) == 4:
                        grid.pop(curr_row - 1)
                        grid.insert(0, [0, 0, 0, 0])
                        answer1 += 1
                else:
                    grid[curr_row-2][curr_col] = 1
                    if sum(grid[curr_row-1]) == 4:
                        grid.pop(curr_row - 1)
                        grid.insert(0, [0, 0, 0, 0])
                        answer1 += 1
                        if sum(grid[curr_row-1]) == 4:
                            grid.pop(curr_row - 1)
                            grid.insert(0, [0, 0, 0, 0])
                            answer1 += 1
                    else:
                        if sum(grid[curr_row-2]) == 4:
                            grid.pop(curr_row-2)
                            grid.insert(0, [0, 0, 0, 0])
                            answer1 += 1
                return
            curr_row += 1

def check(grid):
    pop_count = 0
    for row in range(2):
        for col in range(4):
            if grid[row][col]:
                pop_count += 1
                break
    for _ in range(pop_count):
        grid.pop()
        grid.insert(0, [0, 0, 0, 0])


# 정답 두 번째 줄에 출력할 값을 연산.
def calc_answer2():
    temp = 0
    for row in range(2, 6):
        for col in range(4):
            temp += yellow[row][col] + red[row][col]
    return temp

# def custom_print():
#     print(f'----------yellow---------')
#     for row in yellow:
#         print(*row)
#     print(f'------------red-----------')
#     for row in red:
#         print(*row)

Q = int(input())
yellow = [[0] * 4 for _ in range(6)]
red = [[0] * 4 for _ in range(6)]

answer1 = 0
for _ in range(Q):
    t, r, c = map(int, input().split())

    # 1. 각 격자에 떨구기
    apply_gravity(t, c, yellow)
    red_t = to_red[t]
    # apply_gravity(red_t, 3 - r + (-1 if red_t == 2 else 0), red)
    apply_gravity(red_t, r, red)    # 생각해보니 조잡한 짓 안해도 됐었다.

    # 2. row 기준 지울 수 있는가 체크. 지울 수 있으면 땡기기.
    check(yellow)
    check(red)

answer2 = calc_answer2()
print(answer1)
print(answer2)