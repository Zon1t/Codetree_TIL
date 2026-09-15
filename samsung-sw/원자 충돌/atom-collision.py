# 7:20 시작
# 1. 모든 원자는 1초 지날 때마다 본인 방향의 속력만큼 이동.
# 2. 이동이 끝난 이후, 2개 이상의 원자가 있으면 합성이 일어남. -> 조건 참조.
# move -> boom 정도로 구성하면 되겠다. 좌표 모두 %N 처리 잘하기. 그리드는 매번 업데이트 해주기.
# 나머진 크게 고려할 사항이 없을듯..?


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def move():
    return_dict = dict()
    for curr_row, curr_col in list(data.keys()):
        for curr_mass, curr_speed, curr_dir in data[(curr_row, curr_col)]:
            next_row, next_col = (curr_row + dr[curr_dir] * curr_speed) % N, (curr_col + dc[curr_dir] * curr_speed) % N

            if (next_row, next_col) in return_dict:
                return_dict[(next_row, next_col)][0] += curr_mass
                return_dict[(next_row, next_col)][1] += curr_speed
                return_dict[(next_row, next_col)][2] += 1
                return_dict[(next_row, next_col)][3].append(curr_dir)
            else:
                return_dict[(next_row, next_col)] = [curr_mass, curr_speed, 1, [curr_dir]]
    return return_dict


def boom():
    return_data = dict()
    for curr_row, curr_col in list(new_data.keys()):
        total_mass, total_speed, total_cnt, dir_lst = new_data[(curr_row, curr_col)]
        if total_cnt == 1:
            return_data[(curr_row, curr_col)] = [(total_mass, total_speed, dir_lst[0])]
        else:
            next_mass, next_speed = total_mass // 5, total_speed // total_cnt

            if not next_mass:
                continue

            standard = dir_lst[0]%2
            for i in range(1, total_cnt):
                if standard != dir_lst[i]%2:
                    standard = 2
                    break

            return_data[(curr_row, curr_col)] = []
            for next_dir in ([1, 3, 5, 7] if standard == 2 else [0, 2, 4, 6]):
                return_data[(curr_row, curr_col)].append((next_mass, next_speed, next_dir))
    return return_data


def get_answer():
    temp = 0
    for row, col in data.keys():
        for mass, _, _ in data[(row, col)]:
            temp += mass
    return temp


def custom_print():
    for row, col in data.keys():
        print(f'----row:{row}, col:{col}----')
        for mass, speed, d in data[(row, col)]:
            print(mass, speed, d)


N, M, K = map(int, input().split())
data = dict()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    data[(r-1, c-1)] = [(m, s, d)]

# 실행부
for _ in range(K):
    # 1. 움직이자.
    new_data = move()

    # 2. 처리하자.
    data = boom()

# 정답 출력
answer = get_answer()
print(answer)