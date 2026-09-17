# 10:54 시작 중간에 5분 탈주
# add -> check 로 가보자.
# 어느 방향으로든 나갔으면 다시 들어오는 선이 존재 해야함. 즉 모든 인접한 사람 사이 라인의 개수는
# 짝수여야 함을 이용해보자. 다 짝수라고 되는건 아님! 최적화해볼까?


def check():
    human = target[:]
    for row in range(H):
        for col in range(N-1):
            if lines[row][col]:
                human[col], human[col+1] = human[col+1], human[col]

    return human == target


def backtrack(cnt, col):
    global answer
    if cnt == target_cnt:
        if check() and cnt < answer:
            answer = cnt
        return

    if col == N-1:
        return

    for row in can_lst[col]:
        if not lines[row][col]:
            if col != 0 and lines[row][col-1]:
                continue

            lines[row][col] = 1
            line_cnt[col] += 1

            if line_cnt[col]%2 == 0:
                backtrack(cnt+1, col+1)
                backtrack(cnt+1, col)
            else:
                backtrack(cnt+1, col)

            lines[row][col] -= 1
            line_cnt[col] -= 1

    backtrack(cnt, col+1)


def print_grid():
    print(f'----grid----')
    for row in lines:
        print(*row)

# =========================================================
# 입력받기

N, M, H = map(int, input().split())
lines = [[0] * (N-1) for _ in range(H)]
line_cnt = [0] * (N-1)

can_cnt = [1, 3] if M % 2 else [0, 2]
for _ in range(M):
    row, col = map(lambda x: int(x)-1, input().split())
    lines[row][col] = 1
    line_cnt[col] += 1

# =========================================================
# 세팅

can_lst = [[] for _ in range(N-1)]
for col in range(N-1):
    for row in range(H):
        left, right = col-1, col+1
        flag1, flag2 = False, False

        if left < 0 or not lines[row][left]:
            flag1 = True
        if right > N-2 or not lines[row][right]:
            flag2 = True

        if flag1 and flag2:
            can_lst[col].append(row)

target = list(range(1, N+1))

# =========================================================
# 실행부

answer = 4
for target_cnt in can_cnt:
    backtrack(0, 0)

    if answer != 4:
        break

print(answer if answer != 4 else -1)