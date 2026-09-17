# 11:46 시작
# 경사로 조건 잘 따지면 되는 문제.
# 놓을 수 없는 조건 : 높이 차가 1보다 큼, 주어진 경사로 길이만큼 연속X, 경사로 again
# 이를 따지기 위해 잘 순회하면서 경사로를 만들어보자

dr = [0, 1]
dc = [1, 0]


def check(start_row, start_col, d):
    curr_num, cnt = grid[start_row][start_col], 1
    can_put = True

    curr_row, curr_col = start_row+dr[d], start_col+dc[d]
    while curr_row < N and curr_col < N:
        # 체크
        if not can_put and cnt == L:
            can_put = True
            cnt = 0

        if grid[curr_row][curr_col] == curr_num:
            cnt += 1
        elif grid[curr_row][curr_col] == curr_num-1:
            if not can_put:
                return False
            can_put = False
            curr_num, cnt = grid[curr_row][curr_col], 1
        elif grid[curr_row][curr_col] == curr_num+1:
            if cnt < L or not can_put:
                return False
            curr_num, cnt = grid[curr_row][curr_col], 1
        else:
            return False

        curr_row, curr_col = curr_row + dr[d], curr_col + dc[d]

    if not can_put and cnt < L:
        return False
    return True

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for idx in range(N):
    answer += check(idx, 0, 0)
    answer += check(0, idx, 1)

print(answer)