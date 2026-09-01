# 1. 열별 탐색 진행. 이때 채취 여부를 체크하면 좋을 것 같다.
# 2. 이동 진행. 이때 위치는 어떻게 연산하는가? 개미 문제를 떠올리면 너무 쉽게 구할 수 있다.
# 2-1. 만약 같은 공간에 곰팡이가 있으면 실시간으로 잡아먹게끔 세팅해주면 될 것이다.
# 3. 모든 열에 대해서 위 과정을 수행하고, 끝났을 때의 곰팡이 크기 총합 출력하기.
# 좌표랑 방향 모두 1부터 시작함에 유의하자.
# 딕셔너리 쓰면 금방 풀 수 있지 않을까?


# 순서대로 위, 아래, 오른, 왼
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def catch(row, col):
    global answer
    _, _, size = gompang2.pop((row, col))
    answer += size

def move():
    global gompang2
    new_pang2 = dict()
    catch_pang2.clear()

    for curr_row, curr_col in gompang2:
        speed, curr_dir, size = gompang2[(curr_row, curr_col)]
        if curr_dir <= 1:
            next_row = (curr_row + speed * dr[curr_dir])%row_standard
            next_col = curr_col
            if next_row <= N-1:
                next_dir = curr_dir
            else:
                next_row = row_standard-next_row
                next_dir = curr_dir ^ 1
        else:
            next_row = curr_row
            next_col = (curr_col + speed * dc[curr_dir])%col_standard
            if next_col <= M-1:
                next_dir = curr_dir
            else:
                next_col = col_standard-next_col
                next_dir = curr_dir ^ 1

        if next_col == col+1:
            catch_pang2.append(next_row)

        if (next_row, next_col) in new_pang2:
            if size > new_pang2[(next_row, next_col)][2]:
                new_pang2[(next_row, next_col)] = (speed, next_dir, size)
        else:
            new_pang2[(next_row, next_col)] = (speed, next_dir, size)

    # 업데이트
    gompang2 = new_pang2

N, M, K = map(int, input().split())

row_standard, col_standard = 2*N-2, 2*M-2
gompang2, catch_pang2 = dict(), []
for _ in range(K):
    r, c, s, d, b = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    if c == 0:
        catch_pang2.append(r)
    gompang2[(r, c)] = (s, d, b)

answer = 0
# 실험 진행
for col in range(M):
    # 1. 곰팡이 채취
    if catch_pang2:
        catch_pang2.sort()
        catch(catch_pang2[0], col)

    # 2. 움직이기.
    move()

print(answer)