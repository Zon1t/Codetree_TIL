# 11:42
# 1. 양분 섭취
#       - 본인 나이만큼의 양분을 섭취. 섭취 순서는 나이가 어린 순서
#       - 양분 섭취하면 나이 1 증가. 나이만큼 못 먹으면 죽임.
#       - 죽은 애들은 나이//2만큼 양분화.

# 2. 번식
#       - 번식은 나이가 5의 배수인 애들만 진행.
#       - 인접한 8칸에 대하여 나이가 1인 바이러스 생성

# 위 과정을 반복하며 양분 grid 업데이트. 조건 빼먹지 말고 성실하게 수행하자.


dr = [0, 1, 0, -1, 1, 1, -1, -1]
dc = [1, 0, -1, 0, 1, -1, 1, -1]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def eat():
    new_dict = {}
    for (row, col), age_dict in virus_dict.items():
        threshold = yangboon_grid[row][col] + update_grid[row][col] * time
        be_yangboon = 0
        cant_go = False
        for age in sorted(age_dict.keys()):
            cnt = age_dict[age]

            if cant_go:
                be_yangboon += age//2 * cnt
                continue

            if age * cnt <= threshold:
                threshold -= age * cnt
                if (row, col) in new_dict:
                    new_dict[(row, col)][age+1] = new_dict[(row, col)].get(age+1, 0) + cnt
                else:
                    new_dict[(row, col)] = {age+1: cnt}

                if age%5 == 4:
                    age_5[(row, col)] = age_5.get((row, col), 0) + cnt
            elif age > threshold:
                be_yangboon += age//2 * cnt
                cant_go = True
            else:
                max_cnt = threshold // age
                threshold -= age * max_cnt
                if (row, col) in new_dict:
                    new_dict[(row, col)][age+1] = new_dict[(row, col)].get(age+1, 0) + max_cnt
                else:
                    new_dict[(row, col)] = {age+1: max_cnt}

                if age%5 == 4:
                    age_5[(row, col)] = age_5.get((row, col), 0) + max_cnt

                be_yangboon += age//2 * (cnt-max_cnt)
                cant_go = True

        yangboon_grid[row][col] = threshold - update_grid[row][col] * time + be_yangboon

    return new_dict


def burnsick():
    for (row, col), cnt in age_5.items():
        for d in range(8):
            next_row, next_col = row + dr[d], col + dc[d]
            if not in_range(next_row, next_col):
                continue
            if (next_row, next_col) in virus_dict:
                virus_dict[(next_row, next_col)][1] = virus_dict[(next_row, next_col)].get(1, 0) + cnt
            else:
                virus_dict[(next_row, next_col)] = {1: cnt}
    age_5.clear()


# ============================================================================
# 세팅

N, K, T = map(int, input().split())
yangboon_grid = [[5] * N for _ in range(N)]
update_grid = [list(map(int, input().split())) for _ in range(N)]

virus_dict = {}
for _ in range(K):
    r, c, a = map(int, input().split())
    virus_dict[(r-1, c-1)] = {a: 1}
age_5 = {}

# ============================================================================
# 실행부

for time in range(T):
    # 1. 양분 섭취
    virus_dict = eat()

    # 2. 번식 진행
    burnsick()

# 정답 출력
print(sum([sum(age_dict.values()) for age_dict in virus_dict.values()]))