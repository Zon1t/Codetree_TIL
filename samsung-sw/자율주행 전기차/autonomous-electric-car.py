# 몬스터 처치? 아기 상어의 모험? 이였나. 이름은 기억 안나지만 그거랑 이동 로직이 비슷하다.
# 태우기 + 목적기 -> 사실상 번호 순서가 거의 정해져 있어서 편하긴 할 것 같다.
# 도착과 동시에 배터리 소진 -> 다시 운행 가능! : 이 로직을 정확하게 구현해야겠다.
# find -> move 반복하면 될 듯.

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# arrive 확인 잘하기?
def find():
    time_table = [[-1] * N for _ in range(N)]
    time_table[start_row][start_col] = 0
    time, find_lst = 0, []

    if (start_row, start_col) in start_data and not arrive[start_data[(start_row, start_col)]]:
        return 0, start_row, start_col, start_data[(start_row, start_col)]

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if time != time_table[curr_row][curr_col]:
            if find_lst:
                find_lst.sort()
                return_row, return_col, return_idx = find_lst[0]
                return time_table[return_row][return_col], return_row, return_col, return_idx
            time = time_table[curr_row][curr_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or time_table[next_row][next_col] != -1:
                continue
            if grid[next_row][next_col]:
                continue

            time_table[next_row][next_col] = time_table[curr_row][curr_col] + 1
            Q.append((next_row, next_col))
            if (next_row, next_col) in start_data and not arrive[start_data[(next_row, next_col)]]:
                find_lst.append((next_row, next_col, start_data[(next_row, next_col)]))

    # 벽에 막히는 등 모종의 사유로 발견이 불가능할 때
    return float('inf'), -1, -1, -1

def go(end_row, end_col):
    time_table = [[-1] * N for _ in range(N)]
    time_table[start_row][start_col] = 0

    Q = deque([(start_row, start_col)])
    while Q:
        curr_row, curr_col = Q.popleft()

        if curr_row == end_row and curr_col == end_col:
            return time_table[end_row][end_col]

        for d in range(4):
            next_row, next_col = curr_row + dr[d], curr_col + dc[d]

            if not in_range(next_row, next_col) or time_table[next_row][next_col] != -1:
                continue
            if grid[next_row][next_col]:
                continue

            time_table[next_row][next_col] = time_table[curr_row][curr_col] + 1
            Q.append((next_row, next_col))

    return float('inf')


def custom_print():
    print(f'---------curr_pos/oil----------')
    print(f'row : {start_row}, col : {start_col}, remain : {C}')
    print(f'-------curr_status---------')
    print(*arrive)


scaling = lambda x: int(x)-1
# 입력 받기
N, M, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
start_row, start_col = map(scaling, input().split())

start_data, end_data = dict(), []
for idx in range(M):
    sr, sc, er, ec = map(scaling, input().split())
    start_data[(sr, sc)] = idx                      # 출발지가 동일한 경우는 없다니까 ㄱㅊ
    end_data.append((er, ec))
arrive = [False] * M

answer = -1
# 실행부
for _ in range(M):

    # 1. 승객 위치 찾기
    first_cost, next_row, next_col, idx = find()
    # 1-1. 만약 못가면 break.
    if first_cost > C:
        C = -1
        break


    # 2. 해당 위치로 이동하기
    start_row, start_col= next_row, next_col
    # 2-1. 정보 업데이트 하기.
    C -= first_cost


    # 3. 목적지로 이동시키기
    second_cost = go(end_data[idx][0], end_data[idx][1])
    # 3-1. 갈 수 있는지 체크.
    if second_cost > C:
        C = -1
        break
    # 3-2. 정보 업데이트.
    start_row, start_col = end_data[idx]
    arrive[idx] = True
    C += second_cost

# 정답 출력
print(C)