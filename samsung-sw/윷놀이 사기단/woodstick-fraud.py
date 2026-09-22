# 16:09 시작
# 클래스 써서 해볼까 싶기도 하다? Node.next 이런 느낌으로..
# 그냥 인접리스트 써서 해보자.
# idx      0    1    2    3    4        5    6    7    8    9         10    11    12    13    14        15    16    17    18    19    20    21    22    23    24    25    26    27    28    29    30    31
scores = [ 2,   4,   6,   8,   10,      12,  14,  16,  18,  20,       22,   24,   26,   28,   30,       32,   34,   36,   38,   40,   13,   16,   19,   22,   24,   28,   27,   26,   25,   30,   35,   0]
nlst =   [[1], [2], [3], [4], [5, 20], [6], [7], [8], [9], [10, 23], [11], [12], [13], [14], [15, 25], [16], [17], [18], [19], [31], [21], [22], [28], [24], [28], [26], [27], [28], [29], [30], [19], [31]]


cnt_lst = list(map(int, input().split()))

def backtrack(idx, acc):
    global answer
    if idx == 10:
        if answer < acc:
            answer = acc
        return

    for mal_idx in range(4):
        if curr_pos[mal_idx] == 31:
            continue

        curr_idx = curr_pos[mal_idx]
        next_idx = 0 if curr_idx == -1 else nlst[curr_idx][-1]

        for _ in range(cnt_lst[idx]-1):
            next_idx = nlst[next_idx][0]
        
        if next_idx != 31 and next_idx in curr_pos:
            continue
        
        curr_pos[mal_idx] = next_idx
        backtrack(idx+1, acc+scores[next_idx])
        curr_pos[mal_idx] = curr_idx


curr_pos = [cnt_lst[0]-1, -1, -1, -1]

answer = 0
backtrack(1, scores[curr_pos[0]])
print(answer)