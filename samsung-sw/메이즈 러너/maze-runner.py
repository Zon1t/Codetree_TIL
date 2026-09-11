''' 메이즈 러너 / 20260911 / 체감 난이도 : 골드 2
소요 시간 : 105분 / 시도 : 3회(1회차 : 런타임 에러, 2회차 : 틀림) / 실행 시간 : 59ms / 메모리 : 16MB

타임 라인 : 구상/틀만들기(13분) - 구현(38분) - 디버깅/검증(15분) - 1차 수정(5분) - 2차 수정(34분)


[구상]
    - 솔직히 쉽다고 생각했다. 회전 좌표만 잘 판가름하고 사각형 찾는 로직도 익숙하다고 생각했기에
    구상하고 틀을 만드는 것에 많은 시간을 쏟지는 않았다.
    - 대신 이동 로직에 대해서는 명확하게 하고자 했다. 최단거리로만 움직인다? 근데 우리가 익숙한
    그 최단거리가 아니다. 맨해튼 거리가 줄어드는 방향으로 움직인다는 것. 이러면 줄어드는 방향은
    1 or 2개 밖에 없고 그에 따른 적절한 처리가 필요했다. 델타 세팅도 그냥 상하 먼저 그 이후
    좌우를 탐색하게 하여 알아서 우선 순위에 맞는 길을 택하도록 했다.

[구현]
    - 좌표를 적절하게 이동시키는 것. 단순히 grid로 이동시키는 것이 아닌 특정한 점에 대해서 한
    번에 이동시키고자 했기에, 좌표를 그려가며 이동 대상이 되는 좌표를 받아오고자 했다. 이게 생
    각보다 헷갈렸어서 조금 오래 걸렸다.
    - 중간에 좌표를 알면 사람의 좌표를 알아야하지 않나? 라는 생각을 가지게 되었다. 격자를 회전
    하면 그 회전 격자 내부에 있는 사람들 모두 회전하게 되는데, 이게 조금 골칫거리였다. human이
    그려진 격자를 새로 추가하고자 해서 수정하다가 교차 검증 과정에서 사람이 생각보다 많지 않다는
    사실을 알게 되었다. 이를 바탕으로 굳이 따로 만들지 말고 순회하는 것이 더 경제적일 것이라 판
    단했다. 따라서 다시 고쳐 해당 방식을 기용했다.
    - 끝점에 대한 우선순위가 좌상단 점에 대한 우선순위와 동일할 것이라 판단하여 끝 지점을 기준으
    로 find, rotate 로직을 구성하였다.

[디버깅 & 검증]
    - 예제를 기준으로 디버깅과 검증을 진행하였다. 사람 좌표가 업데이트가 안 된다거나 이동 좌표
    중 이상한 좌표들이 있었다. 해당 부분은 금방 발견해 수정할 수 있었다.
    - 문제를 많이 읽어 봤었는데 문제에서 잘못 이해했을 부분은 없을 것이라 생각했고, 곧 바로 제
    출하게 되었다.

[1차 수정]
    - 냉정하게 생각해 너무 이성적이지 못한 판단이였다. 테케도 단순하고 충분히 K 올려서 돌려볼 수
    있는 판국에 그냥 냅다 질러 런타임 에러를 맞았다. 빨리 풀고 싶다는 욕심이 있었던 것 같다. 조
    기 종료 조건 위치가 잘못되었음을 곧바로 알 수 있었고, 수정한 뒤 곧바로 제출했다.

[2차 수정]
    - 또 안됐다! 이젠 진짜 뭐가 문젠지 모르겠어서 하나하나 찍어보며 확인도 해보고, 변화 양상도
    열심히 관찰해보는 등 열심히 문제점을 찾아보았다.
    - 기능 단위로 문제를 제기해보았다. "얘가 무조건 틀렸다면 어디가 잘못 되었을까?"가 베이직 질
    문이었다. 처음에는 좀 큰 단위 기능부터 생각을 해보고 그 이후 작은 반복문/조건문에 대하여 지
    속적으로 의문을 제기해보았다. 꽤나 오랜 시간을 여기에 투자했다. 해당 과정에서 말도 안되는 생
    각을 했었는데 혹시 탈출구가 여러개인가 생각도 했었다
    - 구현 단계에서 좀 넘겨 짚은 부분이 있었다. 끝 지점에서 우선 순위를 체크한 것과 시작 지점에
    서 우선 순위를 체크한 것이 동치라는 생각이였다! 시작 지점도 잘 찾아낼 수 있으면서 냅다 끝 지
    점 갖다 쓸 생각은 왜 한건지 아직도 모르겠다. 더 검증할게 없다고 생각하여 테케 끌고 와서 답만
    확인한 이후 제출해보았다.

* 피드백
    - 동치 << 이거 진짜 조심해라. 엄밀한 검증 이전까진 동치임을 확신하지 마라.
'''

# 좀 불친절한? 예제를 자세히 풀어서 주지 않았다. 잘 생각해서 문제를 풀어보자.
# 최단거리는 맨해튼 거리로 정의. 출구 방향으로 어쨋든 움직이긴 해야 한다.
# move -> rotate 이동은 할 때마다 answer에 넣어주는 방식으로 진햄.
# find와 같은 세부 기능 수행을 위함 함수 정의도 필요할 듯?
# N이 그렇게 크진 않음. K도 그렇고.. 시간초과? 그건 괜찮을듯?


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 범위 체크
def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

# 맨해튼 거리 반환
def get_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

# 움직이는 함수
def move():
    global answer
    for idx, pos in enumerate(human):

        # 도착한 애는 스킵
        if arrive[idx]:
            continue

        # 현재 위치를 기준으로 최단거리 비교
        curr_dist = get_dist(pos, EXIT)
        for d in range(4):
            next_row, next_col = pos[0] + dr[d], pos[1] + dc[d]

            # 범위에서 벗어나거나 벽이 있으면 스킵
            if not in_range(next_row, next_col):
                continue
            if grid[next_row][next_col]:
                continue

            # 다음 위치를 기준으로 한 맨해튼 거리 기반 최단거리 비교
            next_dist = get_dist((next_row, next_col), EXIT)
            if next_dist < curr_dist:

                # 나갔으면 탈출처리
                if (next_row, next_col) == EXIT:
                    arrive[idx] = True

                # 이동 처리
                human[idx] = (next_row, next_col)
                answer += 1
                break

# 정사각형 찾기
def find():
    standard = (10, 10, 10)
    for idx, pos in enumerate(human):
        # 이미 방문한 친구는 스킵
        if arrive[idx]:
            continue

        # 필요한 변수들 세팅
        curr_size = max(abs(pos[0]-EXIT[0]), abs(pos[1]-EXIT[1]))
        end_row, end_col = max(pos[0], EXIT[0]), max(pos[1], EXIT[1])
        start_row, start_col = max(end_row-curr_size, 0), max(end_col-curr_size, 0)

        # 우선순위에 맞게 판단
        if (curr_size, start_row, start_col) < standard:
            standard = (curr_size, start_row, start_col)

    # 해당 위치 및 사이즈 반환
    return standard

# 깎고 돌리기
def rotate(start_row, start_col, size):
    global EXIT
    
    # 끝 지점을 찾아보자. 이동을 위한 임시 변수도 세팅
    end_row, end_col = start_row+size, start_col+size
    temp = [[0] * (size+1) for _ in range(size+1)]

    # 순회하며 깎고 돌리는 위치에 놓기
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if grid[row][col]:
                grid[row][col] -= 1
            temp[col-start_col][-1-row+start_row] = grid[row][col]

    # 사람도 돌려
    for idx, (row, col) in enumerate(human):
        if arrive[idx]:
            continue

        if start_row <= row <= end_row and start_col <= col <= end_col:
            human[idx] = (start_row+col-start_col, end_col-row+start_row)

    # 이제 이동시키자.
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            grid[row][col] = temp[row-start_row][col-start_col]

    # 탈출구도 물론 이동
    EXIT = (start_row+EXIT[1]-start_col, end_col-EXIT[0]+start_row)


def custom_print():
    print(f'----turn:{turn+1}----')
    print(f'----human----')
    print(*human)
    print(f'----arrive----')
    print(*arrive)
    print(f'----EXIT----')
    print(*EXIT)
    print(f'----grid----')
    for row in grid:
        print(*row)


scaling = lambda x: int(x)-1

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
human = [tuple(map(scaling, input().split())) for _ in range(M)]
EXIT = tuple(map(scaling, input().split()))
arrive = [False] * M

answer = 0
for turn in range(K):
    # 1. 동시에 움직이자.
    move()

    # 조기 종료 조건
    if sum(arrive) == M:
        break

    # 2. 작은 사각형 찾고 돌리기.
    size, start_row, start_col = find()
    rotate(start_row, start_col, size)

# 정답 출력
print(answer)
print(EXIT[0]+1, EXIT[1]+1)