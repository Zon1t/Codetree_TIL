# 10:17 시작     [/
# 대각선의 묘리를 깨우쳐보자. 순회하면서 사각형 만들기 -> 부족원 수 계산
# 잘 진행해보면 될듯. 함수화해서 대각 꼭짓점 좌표만 받아와 보자. << 걍 순회하자.

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def calc_num():
    pops = [0, 0, 0, 0]
    for row in range(lst[1][0]+1, N):
        for col in range(lst[0][1], N):
            if row+col > sum(lst[0]):
                pops[0] += grid[row][col]

    for row in range(lst[1][0]+1):
        for col in range(lst[2][1]+1, N):
            if row-col < lst[1][0]-lst[1][1]:
                pops[1] += grid[row][col]

    for row in range(lst[3][0]):
        for col in range(lst[2][1]+1):
            if row+col < sum(lst[2]):
                pops[2] += grid[row][col]

    for row in range(lst[3][0], N):
        for col in range(lst[0][1]):
            if row-col > lst[3][0]-lst[3][1]:
                pops[3] += grid[row][col]

    return pops


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(row) for row in grid])
answer = float('inf')
for row in range(2, N):
    for col in range(1, N-1):
        for length1 in range(1, N):
            for length2 in range(1, N-length1+1):

                lst = [(row, col)]
                for d in range(3):
                    next_row, next_col = lst[-1][0] + dr[d] * (length2 if d % 2 else length1), lst[-1][1] + dc[d] * (length2 if d % 2 else length1)
                    if not in_range(next_row, next_col):
                        break
                    lst.append((next_row, next_col))

                if len(lst) < 4:
                    continue

                populations = calc_num()
                center = total - sum(populations)
                max_num = max(max(populations), center)
                min_num = min(min(populations), center)

                if answer > max_num - min_num:
                    answer = max_num - min_num

print(answer)