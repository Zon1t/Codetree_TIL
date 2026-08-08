dr = [None, 0, 0, -1, 1]
dc = [None, 1, -1, 0, 0]

# 윗면 : 0, 옆면 : 1~4, 밑면 : 5

# 각 방향별 인덱스 위치가 어디로 이동하는지 미리 저장해둔다.
move_face = [None, [2, 1, 5, 3, 0, 4], [4, 1, 0, 3, 5, 2],
              [1, 5, 2, 0, 4, 3], [3, 0, 2, 5, 4, 1]]

N, M, curr_row, curr_col, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]   # 인덱스(0~5) : 윗면, 앞면, 왼쪽면, 뒷면, 오른쪽면, 아랫면

for d in directions:
    next_row, next_col = curr_row + dr[d], curr_col + dc[d]

    # 만약 범위 밖으로 나가게 되는 경우 이동 명령을 수행하지 않는다.
    if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
        continue

    curr_row, curr_col = next_row, next_col

    next_face = move_face[d]
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[next_face[0]], dice[next_face[1]], dice[next_face[2]], dice[next_face[3]], dice[next_face[4]], dice[next_face[5]]

    if arr[curr_row][curr_col] == 0:
        arr[curr_row][curr_col] = dice[-1]
    else:
        dice[-1] = arr[curr_row][curr_col]
        arr[curr_row][curr_col] = 0

    print(dice[0])