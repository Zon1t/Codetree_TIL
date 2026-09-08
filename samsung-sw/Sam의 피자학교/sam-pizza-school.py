# 문제가 뭐 이래
# 1. 가장 작은 위치 찾아서 밀가루 1 넣어주기.(여러개일 수 있음)
# 2. 도우 말기..? 얘는 어떻게 구현하면 될까. 동적으로 배열 만들기?
# 3. 도우 누르기. 적절하게 업데이트 필요
# 4. 재배치
# 5. 두 번 접기
# 6. 도우 누르기
# 7. 재배치
# -> 말기 / 접기 로직만 잘 구현하면 문제 없이 풀릴 것 같다.. 하다하다 이런 식으로 달팽이를 만드네.
# -> 1, 2, 2, 3, ... 이렇게 진행되는 것 같다. 이를 잘 활용하면 될듯? 일반화된 로직을 만들기 위해
# 두 번 누를 때랑 비슷하게 작동한다고 생각했는데 흠.. 따로 잘 구현해보자.

dr = [0, 1]
dc = [1, 0]

def in_range(row, col, h, w):
    return 0 <= row < h and 0 <= col < w

def add_one():
    min_num = min(milgaru)
    for idx in range(N):
        if milgaru[idx] == min_num:
            milgaru[idx] += 1


def rotate(arr):
    return [list(row[::-1]) for row in zip(*arr)]


def snail():
    # 전개 과정. 배열 만들기 -> 더 만들 수 있으면 rotate 반복, 4의 배수인데 미리 만들까?
    need_idx, remain = 2, N-4
    curr_idx = 4
    curr_arr = [[milgaru[1], milgaru[0]],
                [milgaru[2], milgaru[3]]]
    while snail_cnts[need_idx] <= remain:
        curr_arr = rotate(curr_arr)
        need_cnt = snail_cnts[need_idx]
        curr_arr.append(milgaru[curr_idx:curr_idx+need_cnt])

        remain -= need_cnt
        curr_idx += need_cnt
        need_idx += 1

    w, h = len(curr_arr[0]), len(curr_arr)
    new_arr1 = [[0] * w for _ in range(h)]
    new_arr2 = [0] * (N-curr_idx+1)
    for row in range(h):
        for col in range(w):
            curr_num = curr_arr[row][col]
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col, h, w):
                    continue
                temp = abs(curr_arr[next_row][next_col] - curr_num) // 5
                if temp:
                    new_arr1[next_row][next_col] -= temp * (1 if curr_arr[next_row][next_col] > curr_num else -1)
                    new_arr1[row][col] += temp * (1 if curr_arr[next_row][next_col] > curr_num else -1)

    for idx in range(curr_idx-1, N-1):
        temp = abs(milgaru[idx]-milgaru[idx+1]) // 5
        if temp:
            new_arr2[idx-curr_idx+1] += temp * (1 if milgaru[idx] < milgaru[idx+1] else -1)
            new_arr2[idx-curr_idx+2] -= temp * (1 if milgaru[idx] < milgaru[idx+1] else -1)

    # 업데이트 해주기.
    for r in range(h):
        for c in range(w):
            curr_arr[r][c] += new_arr1[r][c]
    curr_arr[-1][-1] += new_arr2[0]

    for idx in range(1, len(new_arr2)):
        milgaru[curr_idx+idx-1] += new_arr2[idx]

    write_idx = 0
    for col in range(w):
        for row in range(h-1, -1, -1):
            milgaru[write_idx] = curr_arr[row][col]
            write_idx += 1


def twice():
    temp = [milgaru[:half][::-1],
            milgaru[half:]]

    new_arr = []
    rotated = rotate(rotate([list(row[:quat]) for row in temp]))

    new_arr.append(rotated[0])
    new_arr.append(rotated[1])
    new_arr.append(temp[0][quat:])
    new_arr.append(temp[1][quat:])

    update = [[0] * quat for _ in range(4)]
    for row in range(4):
        for col in range(quat):
            for d in range(2):
                next_row, next_col = row + dr[d], col + dc[d]
                if not in_range(next_row, next_col, 4, quat):
                    continue
                temp = abs(new_arr[row][col] - new_arr[next_row][next_col]) // 5
                if temp:
                    update[row][col] += temp * (1 if new_arr[row][col] < new_arr[next_row][next_col] else -1)
                    update[next_row][next_col] -= temp * (1 if new_arr[row][col] < new_arr[next_row][next_col] else -1)

    for row in range(4):
        for col in range(quat):
            new_arr[row][col] += update[row][col]

    write_idx = 0
    for col in range(quat):
        for row in range(3, -1, -1):
            milgaru[write_idx] = new_arr[row][col]
            write_idx += 1


N, K = map(int, input().split())
milgaru = list(map(int, input().split()))
half, quat = N>>1, N>>2

snail_cnts = [i//2+1 for i in range(1, N)]  # 대충 넉넉하게 잡자. 1, 2, 2, 3 ...
cnt = 0
while max(milgaru) - min(milgaru) > K:
    # 1. 작은 놈 밀 추가.
    add_one()

    # 2. 말기 & 누르기 & 배치
    snail()

    # 3. 두 번 접기 & 누르기 & 배치
    twice()

    # 횟수 카운트.
    cnt += 1

# 정답 출력
print(cnt)