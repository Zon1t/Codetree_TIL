# 09:08 시작 /[
# 달팽이 문제. 경로 받아서 하나의 1차원 배열을 선언하고, 이를 바탕으로 문제를 해결하면 될 것.
# 내가 지워야 하는 좌표와 배열 인덱스는 어떻게 받는가. 참조해야 할 인덱스 그리드를 하나 뽑자.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def setting():
    path, curr_idx = [], end-1
    visited = [[False]*N for _ in range(N)]
    idx_grid = [[-1]*N for _ in range(N)]
    
    curr_row, curr_col, curr_dir = 0, 0, 0
    while curr_idx != -1:
        path.append(grid[curr_row][curr_col])
        idx_grid[curr_row][curr_col] = curr_idx
        visited[curr_row][curr_col] = True

        curr_idx -= 1
        if not in_range(curr_row+dr[curr_dir], curr_col+dc[curr_dir]) or \
                visited[curr_row+dr[curr_dir]][curr_col+dc[curr_dir]]:
            curr_dir = (curr_dir+1)%4
        curr_row, curr_col = curr_row+dr[curr_dir], curr_col+dc[curr_dir]

    return idx_grid, path[::-1]


def shot(d, p):
    global answer
    for k in range(1, p+1):
        kill_row, kill_col = center+dr[d]*k, center+dc[d]*k
        target_idx = index_grid[kill_row][kill_col]
        answer += path[target_idx]
        path[target_idx] = 0


def push():
    pointer = 0
    for i in range(end):
        if path[i]:
            if pointer != i:
                path[pointer], path[i] = path[i], path[pointer]
            pointer += 1


def kill_check():
    global answer
    cnt, target, is_killed = 1, path[0], False
    this_end = end
    for i in range(1, end):
        if path[i] == 0:
            this_end = i
            break

        if path[i] == target:
            cnt += 1
        else:
            if cnt >= 4:
                answer += cnt * target
                is_killed = True
                for kill_idx in range(i-cnt, i):
                    path[kill_idx] = 0
            cnt, target = 1, path[i]

    if cnt >= 4:
        answer += cnt * target
        is_killed = True
        for kill_idx in range(this_end-cnt, this_end):
            path[kill_idx] = 0

    return is_killed


def update():
    new_path = [0] * end
    cnt, target, pointer = 1, path[0], 0
    for i in range(1, end):
        if pointer >= end or path[i] == 0:
            break

        if path[i] == target:
            cnt += 1
        else:
            new_path[pointer] = cnt
            new_path[pointer+1] = target
            pointer += 2

            cnt, target = 1, path[i]

    if cnt and target != 0 and pointer < end:
        new_path[pointer] = cnt
        new_path[pointer+1] = target

    return new_path


# ===============================================================
# 세팅

N, K = map(int, input().split())
center, end = N >> 1, N**2-1

grid = [list(map(int, input().split())) for _ in range(N)]
index_grid, path = setting()

# ================================================================
# 실행부

answer = 0
for _ in range(K):
    # 1. 몬스터 죽이기.
    d, p = map(int, input().split())
    shot(d, p)
    
    # 2. 몬스터 땡겨오기.
    push()
    
    # 3. 4칸 이상 연속한 몬스터 죽이기.
    while kill_check():
        push()

    # 4. 경로 업데이트 하기.
    path = update()

# 정답 출력
print(answer)