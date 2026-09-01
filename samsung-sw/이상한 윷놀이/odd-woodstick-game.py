''' 이상한 윷놀이 / 20260901 / 체감 난이도 : 실버 1
소요 시간 : 50분 / 시도 : 1회 / 실행 시간 : 81ms / 메모리 : 18MB

타임 라인 : 구상 및 틀 만들기(16분) - 구현(14분) - 수정 및 검증(20분)


[구상]
    - 내가 누굴 업고 있는지, 다음 이동한 칸에 대해선 누가 있는지 등을 처리하려면 어떤 방식을 사용하는게
    좋을지 고민을 많이 해보았던 것 같다. 파이썬은 슬라이싱이나 뒤집기 이런 기능이 워낙 쓰기 좋다고 생각
    했어서 빈 리스트를 원소로 갖는 N*N grid를 따로 만들어 관리하고자 했다.
    - 더불어 1~k번 순서대로 말이 움직이기 때문에 이를 위해 따로 딕셔너리로 관리해주었다. 그냥 리스트
    써도 될듯? 이후 코드 정리를 해보아야겠다.

[구현]
    - 분기처리만 잘하면 사실 크게 문제될 게 없다고 생각했다.
    - 파란 칸과 격자 밖을 나가게 되는 경우를 동일시하라고 해서 얘를 먼저 처리해야 겠다고 생각했다. 범위
    체크를 하지 않으면 next_row, next_col로 접근이 안되기 때문이다.
    - 조금 낭비가 될 수 있겠지만 구현함에 있어 내가 보기 편하게 필요한 변수들은 저장해서 사용했다. 실수
    하지 않기 위함이였다.

[검증]
    - 내가 선언한 grid와 dictionary를 계속 찍어보면서 맞는지 여부를 판단했다.
    - 부끄럽지만 pan과 grid를 혼동해서 사용한 부분이 있었다. 찾는데 시간이 좀 걸렸어서, 해당 부분을
    수정하는 것에 시간을 적잖게 할애했다.
    - 업데이트하는 과정에서 정답에 영향은 안 주지만 중복 처리한 코드가 있어, 해당 부분을 수정하였다.
'''

# 굉장히 귀찮은 문제이다. 이동 대상 칸 색상별 구분 잘해서 분기문 짜기.
# 파랑색 or 격자 경계의 경우 처리가 중요할 듯 싶다. 파랑을 만나 방향을 바꿨다. 이후 격자 밖으로 가려고
# 한다면 음..방향만 또 바꾸나? 그냥 그대로 두나?
# 말이 4개 이상 겹쳐지는지 매턴 확인할 필요가 있다.
# 음.. 12by12면 그냥 격자 그리기 + dict[idx] = data ~ 이런 느낌으로 관리해보면 어떨까?

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def in_range(row, col):
    return 0 <= row < N and 0 <= col < N

def move(idx):
    # 위치 정보와 다음 위치 진입 여부를 판단하기 위한 변수들 세팅.
    row, col, curr_dir = data_dict[idx]
    next_row, next_col = row + dr[curr_dir], col + dc[curr_dir]
    
    # 다음 칸이 파란색이거나 격자 밖인경우. 제자리 있는 경우만 따로 처리하자.
    if not in_range(next_row, next_col) or pan[next_row][next_col] == 2:
        next_dir = curr_dir ^ 1         # 방향 뒤집기
        next_row, next_col = row + dr[next_dir], col + dc[next_dir]
        data_dict[idx][2] = next_dir
        if not in_range(next_row, next_col) or pan[next_row][next_col] == 2:
            return False

    # 데이터 업데이트를 위한 세팅들
    start = grid[row][col].index(idx)
    move_object = grid[row][col][start:]
    grid[row][col] = grid[row][col][:start]

    # 만약 다음 칸이 흰 칸이면 그냥 추가
    if pan[next_row][next_col] == 0:
        grid[next_row][next_col].extend(move_object)
    # 빨간 칸이면 뒤집어서 추가
    else:
        grid[next_row][next_col].extend(move_object[::-1])

    # 내가 업은 애들도 좌표는 업뎃해주기
    for i in move_object:
        data_dict[i][0], data_dict[i][1] = next_row, next_col

    # 만약 내가 도착한 칸에 4개 이상의 말이 존재한다면 True, 아니면 False 반환
    return len(grid[next_row][next_col]) >= 4

def custom_print():
    print(f'---------grid----------')
    for row in grid:
        print(*row)
    print(f'---------dict----------')
    for k in data_dict:
        print(f'k:{k}, value:{data_dict[k]}')

# 데이터 입력받기.
N, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# 적절한 변수들을 활용하여 입력받은 데이터 정리하기.
grid = [[[] for _ in range(N)] for _ in range(N)]
data_dict = dict()
for idx in range(1, K+1):
    x, y, d = map(lambda x: int(x)-1, input().split())
    data_dict[idx] = [x, y, d]
    grid[x][y].append(idx)

answer = -1
# 이상한 윷놀이 진행.
for turn in range(1, 1001):
    # 입력받은 순서대로 말 위치 업데이트
    for idx in range(1, K+1):
        stop = move(idx)
        # 만약 말 4개 이상인 위치가 존재한다면 멈추자
        if stop:
            break
    # for문 다 순회했으면 이상 없다는 뜻! 다음 턴으로 넘어가자.
    else:
        continue

    # 여기까지 왔다는건 stop했다는 뜻. 정답 저장하고 반복문 종료.
    answer = turn
    break

# 정답 출력
print(answer)