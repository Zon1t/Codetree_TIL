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
    curr_row = 1
    if block_type == 2:
        while True:
            if curr_row == 6 or grid[curr_row][curr_col] or grid[curr_row][curr_col+1]:
                grid[curr_row-1][curr_col] = grid[curr_row-1][curr_col+1] = 1
                return
            curr_row += 1
    else:
        while True:
            if curr_row == 6 or grid[curr_row][curr_col]:
                grid[curr_row-1][curr_col] = 1
                if block_type == 3:
                    grid[curr_row-2][curr_col] = 1
                return
            curr_row += 1


# 체크 하면서 지우기를 한 번에 처리하자.
def check(grid):
    global answer1

    pointer = 5
    while 0 <= pointer:
        while sum(grid[pointer]) == 4:
            grid.pop(pointer)
            grid.insert(0, [0, 0, 0, 0])
            answer1 += 1
        pointer -= 1

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

def custom_print():
    print(f'----------yellow---------')
    for row in yellow:
        print(*row)
    print(f'------------red-----------')
    for row in red:
        print(*row)

Q = int(input())
yellow = [[0] * 4 for _ in range(6)]
red = [[0] * 4 for _ in range(6)]

answer1 = 0
for _ in range(Q):
    t, r, c = map(int, input().split())

    # 1. 각 격자에 떨구기
    apply_gravity(t, c, yellow)
    red_t = to_red[t]
    apply_gravity(red_t, 3-r+(-1 if red_t == 2 else 0), red)

    # 2. row 기준 지울 수 있는가 체크. 지울 수 있으면 땡기기.
    check(yellow)
    check(red)

answer2 = calc_answer2()
print(answer1)
print(answer2)