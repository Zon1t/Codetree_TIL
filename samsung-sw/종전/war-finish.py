# 직사각형에 대한 구상 -> 만들 수 있는 직사각형의 사이즈는 정해져있다. 해당 위치에 의거하여 각각
# 대각으로 몇 칸을 갈 수 있는가에 대한 연산이 필요하다. 영역별 합을 구하는 로직에 대해서는 조금 더 생각해볼
# 필요가 있을 것으로 보인다.
# 진행 로직 : 1. 직사각형의 양 끝 꼭짓점의 좌표를 구하기
#           2. 영역별 인구수 연산
#           3. min, max 차이 연산
# 하드코딩이 많이 필요해보이는데 너무 고민하기보단 기세로 밀고가보자.

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def make_linear_equation(pos1, pos2):
    return lambda x: ((pos1[1]-pos2[1])/(pos1[0]-pos2[0]))*(x-pos1[0]) + pos1[1]

def calc_members(standard_point):
    # 이래도 되는건가 싶지만 직선의 방정식 쓰면 되지 않나?
    return_lst = [0, 0, 0, 0]

    # 우하단
    linear_equation = make_linear_equation(standard_point[0], standard_point[1])
    for row in range(standard_point[1][0]+1, N):
        for col in range(standard_point[0][1], N):
            if linear_equation(row) < col:
                return_lst[3] += grid[row][col]

    # 우상단
    linear_equation = make_linear_equation(standard_point[1], standard_point[2])
    for row in range(standard_point[1][0]+1):
        for col in range(standard_point[2][1]+1, N):
            if linear_equation(row) < col:
                return_lst[1] += grid[row][col]

    # 좌상단
    linear_equation = make_linear_equation(standard_point[2], standard_point[3])
    for row in range(standard_point[3][0]):
        for col in range(standard_point[2][1]+1):
            if linear_equation(row) > col:
                return_lst[0] += grid[row][col]

    # 좌하단
    linear_equation = make_linear_equation(standard_point[3], standard_point[0])
    for row in range(standard_point[3][0], N):
        for col in range(standard_point[0][1]):
            if linear_equation(row) > col:
                return_lst[2] += grid[row][col]

    return return_lst


dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

total_population = sum([sum(row) for row in grid])
answer = 40000
for sr in range(2, N):
    for sc in range(1, N-1):
        for first_step in range(1, N):
            for second_step in range(1, N-first_step+1):
                standard_point = [(sr, sc)]
                curr_row, curr_col = sr, sc

                # 끝단 꼭짓점 연산하기.
                for d in range(3):
                    curr_row, curr_col = curr_row + dr[d] * (first_step if d%2 == 0 else second_step), curr_col + dc[d] * (first_step if d%2 == 0 else second_step)
                    if not in_range(curr_row, curr_col):
                        break
                    standard_point.append((curr_row, curr_col))

                # 더 이상 살펴볼 수 없는 경우
                if len(standard_point) != 4:
                    break

                # 나머지 부족 사람 수 연산하러 ㄱㄱㅆ
                pop_lst = calc_members(standard_point)
                first_group = total_population - sum(pop_lst)

                # 정답 업데이트하기.
                max_pop = max(max(pop_lst), first_group)
                min_pop = min(min(pop_lst), first_group)
                if answer > max_pop-min_pop:
                    answer = max_pop-min_pop

# 정답 출력
print(answer)
