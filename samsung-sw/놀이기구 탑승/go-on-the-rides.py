# 좀 어렵다. 힙으로 관리해야하나? 그러면 발생할 수 있는 문제가 없겠는가?
# 그냥 순회 업뎃이 맞는듯? 힙 만드는 것도 짜피 순회해야 하니 그냥 바로바로 업뎃하는 방식이 맞아보인다.
# 구현해야 하는 함수 : find_pos, calc_score
# 학생 정보는 어디에 담겠는가? 그냥 dict?

# 델타 세팅
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 점수 세팅.
scores = [0, 1, 10, 100, 1000]

def find_pos(node):
    # 자리 초기화
    best_pos = (100, 100, 100, 100)

    for row in range(N):
        for col in range(N):
            # 이미 사람이 있으면 스킵.
            if grid[row][col]:
                continue

            # 우선순위 연산을 위한 친구 수, 빈 칸 수 세기 변수 선언.
            friend_cnt = 0
            empty_cnt = 0
            
            # 인접 칸 탐색
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]

                # 격자에서 벗어나는 칸은 비어있는 칸으로 취급하지 않는다.
                if not in_range(next_row, next_col):
                    continue

                # 빈 칸이면 빈자리 += 1.
                if grid[next_row][next_col] == 0:
                    empty_cnt += 1
                # 사람이 있으면 친구인지 체크.
                else:
                    if grid[next_row][next_col] in data[node]:
                        friend_cnt += 1
            
            # 우선순위에 의거한 자리찾기.
            if best_pos > (-friend_cnt, -empty_cnt, row, col):
                best_pos = (-friend_cnt, -empty_cnt, row, col)

    # 자리에 앉기
    grid[best_pos[2]][best_pos[3]] = node


def calc_score():
    temp = 0
    for row in range(N):
        for col in range(N):
            now_node = grid[row][col]
            cnt = 0
            for d in range(4):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col):
                    continue
                if grid[next_row][next_col] in data[now_node]:
                    cnt += 1
            temp += scores[cnt]
    return temp

# 범위 안에 있는지 체크하는 함수.
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


N = int(input())
grid = [[0] * N for _ in range(N)]

data = dict()
order = []
for _ in range(N*N):
    n0, *friends = map(int, input().split())
    data[n0] = friends
    order.append(n0)

# 1. 순서대로 시뮬레이션 수행
for node in order:
    find_pos(node)

# 2. 점수 계산
answer = calc_score()

# 3. 점수 출력
print(answer)