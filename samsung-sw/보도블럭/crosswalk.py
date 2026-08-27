# 적절한 cnt 세팅으로 경사로 길이를 체크하면 될 듯 싶다. 끝난 경우에도 cnt 확인하기.
# 행, 열에 대해서 모두 수햄. 내가 구현하는 로직이 경사로 설치 제한 조건을 잘 반영하는지 확인하기.
# 크게 문제될 부분은 없을 것 같다?

def check(idx, dr, dc):
    # 필요 변수들 설정.
    curr_row, curr_col = (0, idx) if dr else (idx, 0)
    curr_height = grid[curr_row][curr_col]
    can_put = True
    cnt = 1

    # simulation 진행
    for _ in range(1, N):
        curr_row, curr_col = curr_row + dr, curr_col + dc

        # 놓을 수 있는 요건 초기화
        if not can_put and cnt == L:
            can_put = True
            cnt = 0

        # 각 분기별 수행 로직.
        if curr_height == grid[curr_row][curr_col]:
            cnt += 1
        elif curr_height+1 == grid[curr_row][curr_col]:
            if cnt >= L and can_put:
                curr_height = grid[curr_row][curr_col]
                cnt = 1
            else:
                return False
        elif curr_height-1 == grid[curr_row][curr_col]:
            # 진행중인 보도블럭이 있으면 안됨.
            if not can_put:
                return False

            curr_height = grid[curr_row][curr_col]
            can_put = False
            cnt = 1
        else:
            return False

    if not can_put and cnt < L:
        return False

    return True

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    # 열 방향으로 이동하며 체크
    if check(i, 1, 0):
        answer += 1

    # 행 방향으로 이동하며 체크
    if check(i, 0, 1):
        answer += 1

print(answer)