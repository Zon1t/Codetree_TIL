# 격자를 벗어난다는 개념은 존재하지 않는다. 다 mod N 처리.
# 음.. n이 작긴 한데 격자를 그릴 필요가 있나 싶다. 그냥 dictionary 써서 하는 게 마음 편할 것 같다.
# 만들 함수. 그냥 move, update, calc_scores

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    temp = dict()
    for row, col, mass, speed, direction in data:
        next_row, next_col = (row + speed*dr[direction])%N, (col + speed*dc[direction])%N

        if (next_row, next_col) in temp:
            temp[(next_row, next_col)][0] += mass
            temp[(next_row, next_col)][1] += speed
            temp[(next_row, next_col)][2] += 1
            temp[(next_row, next_col)][3].append(direction)

        else:
            temp[(next_row, next_col)] = [mass, speed, 1, [direction]]

    return temp


def update():
    global data

    new_data = []
    for (row, col), (mass, speed, cnt, direction) in atom_dict.items():
        if cnt == 1:
            new_data.append((row, col, mass, speed, direction[0]))
        else:
            next_mass, next_speed = mass // 5, speed // cnt

            if next_mass == 0:
                continue

            # 다음 어떻게 퍼져나갈지 연산하기.
            now_state = direction[0] % 2
            for d in direction[1:]:
                if now_state != d % 2:
                    now_state = 2
                    break

            # 상태에 맞게 퍼뜨리기.
            for d in ((0, 2, 4, 6) if now_state != 2 else (1, 3, 5, 7)):
                new_data.append((row, col, next_mass, next_speed, d))

    # data 업데이트 해주기.
    data = new_data

def calc_scores():
    temp = 0
    for _, _, m, _, _ in data:
        temp += m
    return temp


# 헷갈릴 것 같아서 자주 쓰는 변수로 바꿔 받았다.
N, K, T = map(int, input().split())

# 기본적으로 이동에 대한 정보를 기록하는 변수. 지속적으로 업데이트 될 것.
data = []
for _ in range(K):
    r, c, m, s, d = map(int, input().split())
    data.append((r-1, c-1, m, s, d))

for _ in range(T):
    # 기록용으로 남기는 딕셔너리. atom_dict[(row, col)] = [mass, speed, cnt, directions]
    atom_dict = move()
    update()

answer = calc_scores()
print(answer)