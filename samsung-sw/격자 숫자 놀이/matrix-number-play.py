'''
애초에 100보다 커지는 경우는 존재하지 않는다. ??
'''

# 배열의 크기가 변하게 된다. 행이 열의 개수보다 크거나 같을 때 / 작을 때 다른 방식으로 연산 수행
# + 100 넘어가면 격자 버리기 잘 처리하기.
# 격자가 지칭하는 바 1행 1열부터 시작함에 유의하자.
# 만들어야 하는 함수. simulate(규칙 수행), update(격자 자르기), check(종료 조건 체크)
# 시간 복잡도 괜찮나? 최대 100*100 처리를 100번한다?

temp = dict()
def simulate():
    global grid, N, M

    need = False
    # 중복되는 것 같은데 다른 방법론 없을라나
    if N < M:
        grid = [row[:] for row in zip(*grid)]
        N, M = M, N
        need = True

    max_row = 0
    for row in range(N):
        temp.clear()

        for col in range(M):
            if grid[row][col] == 0:
                continue

            if grid[row][col] in temp:
                temp[grid[row][col]] += 1
            else:
                temp[grid[row][col]] = 1

        lst, cnt = [], 0
        for key, value in temp.items():
            lst.append((value, key))
            cnt += 1
        lst.sort()

        max_row = max(cnt*2, max_row)
        grid[row] = [0] * 100
        for idx, (v, k) in enumerate(lst):
            grid[row][idx*2], grid[row][idx*2+1] = k, v

    if need:
        N, M = max_row, N
        grid = [row[:] for row in zip(*grid)]
    else:
        M = max_row


def check():
    return target_r < N and target_c < M and grid[target_r][target_c] == k


# 입력 처리
target_r, target_c, k = map(int, input().split())
target_r, target_c = target_r-1, target_c-1

grid = [[0] * 100 for _ in range(100)]
for i in range(3):
    temp_row = list(map(int, input().split()))
    for j in range(3):
        grid[i][j] = temp_row[j]

N, M = 3, 3
# 에지 케이스? 시작하자마자 끝나는 경우
if check():
    print(0)
else:
    # 주어진 시간만큼 시뮬레이션 수행
    for time in range(1, 101):
        # 1. 규칙 적용
        simulate()

        # 2. 종료 체크
        if check():
            print(time)
            break

    # 시간 안에 못 끝냈다면..
    else:
        print(-1)