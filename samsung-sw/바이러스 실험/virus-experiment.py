# 시작 11:53
# 나잇대별로 정리해서 관리를 해주자.. 양분_grid 따로 만들기 이때 연산은 lazy하게
# 1. eat. 나이만큼 양분 먹고 나이 += 1
# 2. 죽은 바이러스들은 //2 해서 양분칸에 추가.
# 3. 나이가 5의 배수면 번식 진행.
# 4. 양분 업데이트.. 중요

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def eat():
    new_dict = dict()
    for row, col in virus.keys():
        threshold = yangboon_grid[row][col]+update_grid[row][col]*turn
        already_done = False
        add_yangboon = 0

        for age, cnt in sorted(virus[(row, col)].items()):

            if already_done:
                add_yangboon += (age//2)*cnt
                continue

            if age*cnt <= threshold:
                if (row, col) in new_dict:
                    new_dict[(row, col)][age+1] = cnt
                else:
                    new_dict[(row, col)] = {age+1: cnt}
                threshold -= age*cnt
                yangboon_grid[row][col] -= age*cnt
                if (age+1)%5 == 0:
                    age_5[row][col] += cnt
            elif age > threshold:
                add_yangboon += (age//2)*cnt
                already_done = True
            else:
                max_cnt = threshold//age

                if (row, col) in new_dict:
                    new_dict[(row, col)][age+1] = max_cnt
                else:
                    new_dict[(row, col)] = {age+1: max_cnt}

                threshold -= age*max_cnt
                yangboon_grid[row][col] -= age*max_cnt
                if (age+1)%5 == 0:
                    age_5[row][col] += max_cnt

                add_yangboon += (age//2)*(cnt-max_cnt)
                already_done = True

        yangboon_grid[row][col] += add_yangboon

    return new_dict


def burnsick():
    for row in range(N):
        for col in range(N):
            temp = 0
            for d in range(8):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue
                temp += age_5[next_row][next_col]

            if temp:
                if (row, col) in virus:
                    virus[(row, col)][1] = temp
                else:
                    virus[(row, col)] = {1: temp}

    for row in range(N):
        for col in range(N):
            age_5[row][col] = 0


def get_answer():
    temp = 0
    for age_dict in virus.values():
        temp += sum(age_dict.values())
    return temp


def print_grid():
    print(f'----virus_grid----')
    for row in range(N):
        for col in range(N):
            if (row, col) in virus:
                print(virus[(row, col)], end=' ')
            else:
                print(0, end=' ')
        print()
    print(f'----yangboon_grid----')
    for row in range(N):
        for col in range(N):
            print(yangboon_grid[row][col]+update_grid[row][col]*turn, end=' ')
        print()


# =================================================================
# 입력

N, M, K = map(int, input().split())
yangboon_grid = [[5] * N for _ in range(N)]
update_grid = [list(map(int, input().split())) for _ in range(N)]
age_5 = [[0] * N for _ in range(N)]

virus = dict()
for _ in range(M):
    r, c, age = map(int, input().split())
    virus[(r-1, c-1)] = {age: 1}

# =================================================================
# 실행부

for turn in range(K):
    # 1. 양분 먹기 & 양분화
    virus = eat()

    # 2. 번식 진행
    burnsick()

# 접답 연산
answer = get_answer()
print(answer)