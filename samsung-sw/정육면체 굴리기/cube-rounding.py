# 델타 세팅
dr = [None, 0, 0, -1, 1]
dc = [None, 1, -1, 0, 0]

# 인덱스(0~5) : 윗면, 앞면, 왼쪽면, 뒷면, 오른쪽면, 아랫면
# 으로 정의해서 문제를 풀이하자.

# 각 방향별 인덱스 위치가 어디로 이동하는지 미리 저장해둔다.
move_face = [None, [2, 1, 5, 3, 0, 4], [4, 1, 0, 3, 5, 2],
              [1, 5, 2, 0, 4, 3], [3, 0, 2, 5, 4, 1]]

# 입력값 받기
N, M, curr_row, curr_col, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

# 정육면체 초기 상태
dice = [0, 0, 0, 0, 0, 0]

# 이동명령을 순차적으로 수행한다.
for d in directions:
    # 다음 이동 예정의 좌표.
    next_row, next_col = curr_row + dr[d], curr_col + dc[d]

    # 만약 범위 밖으로 나가게 되는 경우 이동 명령을 수행하지 않는다.
    if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
        continue
    
    # 이동 가능하면 이동 처리를 한다.
    curr_row, curr_col = next_row, next_col
    
    # 다음 변화하게 될 인덱스를 받아와 면을 업데이트한다.
    next_face = move_face[d]
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[next_face[0]], dice[next_face[1]], dice[next_face[2]], dice[next_face[3]], dice[next_face[4]], dice[next_face[5]]
    
    # 문제에서 시키는대로 변화를 수행한다.
    # 만약 칸의 숫자가 0이면 주사위 아랫면 숫자를 복사한다.
    if arr[curr_row][curr_col] == 0:
        arr[curr_row][curr_col] = dice[-1]
    # 만약 칸의 숫자가 0이 아니면 칸의 숫자를 주사위에 복사하고 칸의 숫자를 0으로 바꾼다.
    else:
        dice[-1] = arr[curr_row][curr_col]
        arr[curr_row][curr_col] = 0
    
    # 명령을 수행하고 난 뒤 윗면을 출력한다.
    print(dice[0])