# 배열의 크기가 변하게 된다. 행이 열의 개수보다 크거나 같을 때 / 작을 때 다른 방식으로 연산 수행
# + 100 넘어가면 격자 버리기 잘 처리하기.
# 격자가 지칭하는 바 1행 1열부터 시작함에 유의하자.
# 만들어야 하는 함수. simulate(규칙 수행), update(격자 자르기), check(종료 조건 체크)
# 시간 복잡도 괜찮나? 최대 100*100 처리를 100번한다?

temp = dict()
def simulate():
    global grid, N, M

    new_grid = []
    # 중복되는 것 같은데 다른 방법론 없을라나
    if N >= M:
        rows = []
        for row in range(N):
            temp.clear()

            for col in range(M):
                if grid[row][col] == 0:
                    continue

                if grid[row][col] in temp:
                    temp[grid[row][col]] += 1
                else:
                    temp[grid[row][col]] = 1

            lst = []
            for key, value in temp.items():
                lst.append((value, key))
            lst.sort()

            new_row = []
            for val, k in lst:
                new_row.extend([k, val])

            rows.append(len(new_row))
            new_grid.append(new_row)

        max_row = max(rows)
        for idx in range(N):
            if rows[idx] < max_row:
                new_grid[idx] += [0] * (max_row - rows[idx])
        grid = new_grid

        M = max_row
    else:
        cols = []
        for col in range(M):
            temp.clear()

            for row in range(N):
                if grid[row][col] == 0:
                    continue

                if grid[row][col] in temp:
                    temp[grid[row][col]] += 1
                else:
                    temp[grid[row][col]] = 1

            lst = []
            for key, value in temp.items():
                lst.append((value, key))
            lst.sort()

            new_col = []
            for val, k in lst:
                new_col.extend([k, val])

            cols.append(len(new_col))
            new_grid.append(new_col)

        max_col = max(cols)
        for idx in range(M):
            if cols[idx] < max_col:
                new_grid[idx] += [0] * (max_col - cols[idx])

        new_grid = [row for row in zip(*new_grid)]
        grid = new_grid

        N = max_col

def update():
    global grid
    new_N, new_M = N%100, M%100
    grid = [row[(100 if M > 100 else 0):] for row in grid[(100 if N > 100 else 0):]]
    return new_N, new_M

def check():
    return target_r < N and target_c < M and grid[target_r][target_c] == k


# 입력 처리
target_r, target_c, k = map(int, input().split())
target_r, target_c = target_r-1, target_c-1
grid = [list(map(int, input().split())) for _ in range(3)]

N, M = 3, 3
# 에지? 시작하자마자 끝나는 경우
if check():
    print(0)
else:
    # 주어진 시간만큼 시뮬레이션 수행
    for time in range(1, 101):
        # 규칙 적용
        simulate()

        # grid 업데이트
        update()

        # 종료 체크
        if check():
            print(time)
            break

    # 시간 안에 못 끝냈다면..
    else:
        print(-1)