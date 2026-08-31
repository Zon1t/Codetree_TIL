''' 종전 / 20260831 / 체감 난이도 : 골드 3
소요 시간 : 75분 / 시도 : 1회 / 실행 시간 : 299ms / 메모리 : 23MB

타임 라인 : 구상 및 틀 만들기(30분) - 구현(25분) - 검증 및 수정(20분)


[구상]
    - 직사각형을 만드는 방법론으로 처음에는 백트래킹이 우선적으로 생각이 났던 것 같다. 근데 그걸 쓰기보단
    사이즈가 주어지니 step을 각각 정의해서 꼭짓점의 좌표를 쓰는 편이 좋다고 생각했다. 인구 수 연산에 필연
    적으로 쓰일 것이라 생각했기 때문이다.
    - 이후 인구수를 각 그룹별로 어떻게 해줄까에 대해서 가장 많은 시간을 할애했던 것 같다. 손으로 조금 그려
    보니, 부등식 개념이 떠올라서 직선의 방정식을 정의해 문제를 해결하고자 했다. 전체적인 틀을 만들어 가면서
    조금 더 구현할 부분들을 명확하게 떠올려보았다.

[구현]
    - 직선의 방정식 만드는 공식을 바탕으로 두 점의 좌표가 주어졌을 때, 해당 두 점을 지나는 직선의 방정식을
    반환하는 함수를 만들었다.
    - 각 영역별 range를 적절하게 주고, 대소 관계만 적절하게 준다면 연산이 원활하게 될 것으로 생각했다. 이때
    grid는 뒤집혀 있다는 점을 확실하게 인지하고 range를 적절하게 주기 위해 신경을 많이 썼다.

[검증]
    - 검증할 때는 처음엔 로직이 실행될 때마다 결과값을 찍어보았는데, 가독성이 너무 떨어져서 정답이 업데이트
    되는 순간만 출력해보았다.
    - 몇몇 테케에서 정답이 안나왔었는데, 다른 로직은 다 맞았었는데 꼭짓점 연산하는 부분이 일부 지워져있는 것을
    발견하고 해당 부분을 채워주었다. 매번 시작 지점, step 변수들, calc결과를 찍어보며 비교하니 내가 틀린
    부분을 추적하는 게 비교적 쉬웠던 것 같다.
    - 혹시 빼먹은 부분이 없을까 문제를 한 번 더 읽어보고, 코드에 잘 반영되었다고 생각한 순간 제출했다.
'''

# 직사각형에 대한 구상 -> 만들 수 있는 직사각형의 사이즈는 정해져있다. 해당 위치에 의거하여 각각
# 대각으로 몇 칸을 갈 수 있는가에 대한 연산이 필요하다. 영역별 합을 구하는 로직에 대해서는 조금 더 생각해볼
# 필요가 있을 것으로 보인다.
# 진행 로직 : 1. 직사각형의 양 끝 꼭짓점의 좌표를 구하기
#           2. 영역별 인구수 연산
#           3. min, max 차이 연산
# 하드코딩이 많이 필요해보이는데 너무 고민하기보단 기세로 밀고가보자.

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def calc_members(standard_point):
    # 이래도 되는건가 싶지만 직선의 방정식 쓰면 되지 않나?
    # 기울기가 1 혹은 -1이라 굳이 안 써도 된다.
    return_lst = [0, 0, 0, 0]

    # 우하단
    for row in range(standard_point[1][0]+1, N):
        for col in range(max(0, standard_point[0][0]-row+1) + standard_point[0][1], N):
            return_lst[3] += grid[row][col]

    # 우상단
    for row in range(standard_point[1][0]+1):
        for col in range(max(row-standard_point[1][0]+standard_point[1][1], standard_point[2][1])+1, N):
            return_lst[1] += grid[row][col]

    # 좌상단
    for row in range(standard_point[3][0]):
        for col in range(min(1, standard_point[2][0]-row)+standard_point[2][1]):
            return_lst[0] += grid[row][col]

    # 좌하단
    for row in range(standard_point[3][0], N):
        for col in range(min(standard_point[0][1], row-standard_point[3][0]+standard_point[3][1])):
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