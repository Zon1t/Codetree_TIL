# 시작 4:37
# 우선순위에 맞는 자리 배치 문제.
# 1. 좋아하는 친구가 가장 많은 위치.
# 2. 비어있는 칸이 가장 많은 위치.
# 3. 행이 작은 위치.
# 4. 열이 작은 위치.
# 모두 배치한 이후 점수 연산.


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def find(node):
    curr_max = (-1, -1, -1, -1)
    for row in range(N):
        for col in range(N):
            if grid[row][col]:
                continue
            friend_cnt, empty_cnt = 0, 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]

                if not in_range(next_row, next_col):
                    continue

                search = grid[next_row][next_col]
                if search == 0:
                    empty_cnt += 1
                else:
                    if search in friends[node]:
                        friend_cnt += 1

            curr_value = (friend_cnt, empty_cnt, -row, -col)
            if curr_max < curr_value:
                curr_max = curr_value

    grid[-curr_max[2]][-curr_max[3]] = node


def calc_score():
    temp = 0
    for row in range(N):
        for col in range(N):
            cnt, curr_node = 0, grid[row][col]
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue
                if grid[next_row][next_col] in friends[curr_node]:
                    cnt += 1
            temp += scores[cnt]
    return temp


N = int(input())
grid = [[0] * N for _ in range(N)]

friends = [None] * (N**2+1)
for _ in range(N**2):
    n0, *friend = map(int, input().split())
    friends[n0] = friend
    find(n0)


# 정답 연산하기.
scores = [0, 1, 10, 100, 1000]
answer = calc_score()
print(answer)