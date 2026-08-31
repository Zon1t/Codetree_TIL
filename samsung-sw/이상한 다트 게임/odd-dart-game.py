# 문제 침착하게 읽고 풀기. 빨리 안풀어도 됨.
# 원판의 수 n, m개의 정수. 12시부터 시계방향으로 정수가 배치됨.
# 돌리는 연산은 포인터로 적절하게 처리하면 될 것 같다.
# 인접하다의 정의를 복잡하게 내려주었지만, 보편적으로 생각하는 그 개념을 설명한다.
# 인접한 숫자에 대한 처리는 동시에 일어나야 한다? 아마 그럴듯?
# 만들 함수 check -> standard_scale
# 같은 수를 지우는 과정은 회전시킨 이후 진행하라고 문제에서 나와있다.


# 틀린 부분 : 배수 돌리기인데 적용 안했다; 왜이러지

# 돌리기
def rotate(x, d, k):
    for pan_idx in range(x, N, x+1):
        pointers[pan_idx] = (pointers[pan_idx] + (1 if d else -1) * k) % M

# 해당 로직이 중요하다.
def check():
    global pan

    need_scaling = True
    erase_set = set()
    # 판과 판 사이 위 아래로 인접한지 체크하기
    for pan_idx in range(N-1):
        for num_idx in range(M):
            first_num_idx, second_num_idx = (pointers[pan_idx]+num_idx)%M, (pointers[pan_idx+1]+num_idx)%M
            if pan[pan_idx][first_num_idx] == pan[pan_idx+1][second_num_idx] and not erase_grid[pan_idx][first_num_idx] and not erase_grid[pan_idx+1][second_num_idx]:
                erase_set.add((pan_idx, first_num_idx))
                erase_set.add((pan_idx+1, second_num_idx))
                need_scaling = False

    # 양 옆으로 인접한지 체크하기.
    for pan_idx in range(N):
        for num_idx in range(M):
            if pan[pan_idx][num_idx] == pan[pan_idx][num_idx-1] and not erase_grid[pan_idx][num_idx] and not erase_grid[pan_idx][num_idx-1]:
                erase_set.add((pan_idx, num_idx))
                erase_set.add((pan_idx, num_idx-1))
                need_scaling = False

    for pan_idx, num_idx in erase_set:
        erase_grid[pan_idx][num_idx] = True

    return need_scaling


def standard_scale():
    total = 0
    cnt = 0
    for pan_idx in range(N):
        for num_idx in range(M):
            if erase_grid[pan_idx][num_idx]:
                continue
            total += pan[pan_idx][num_idx]
            cnt += 1

    # 숫자가 남아있는 경우만 진행
    if cnt:
        avg = total // cnt
        for pan_idx in range(N):
            for num_idx in range(M):
                if erase_grid[pan_idx][num_idx]:
                    continue

                if pan[pan_idx][num_idx] > avg:
                    pan[pan_idx][num_idx] -= 1
                elif pan[pan_idx][num_idx] < avg:
                    pan[pan_idx][num_idx] += 1


def calc_answer():
    temp = 0
    for pan_idx in range(N):
        for num_idx in range(M):
            if erase_grid[pan_idx][num_idx]:
                continue
            temp += pan[pan_idx][num_idx]
    return temp

def custom_print():
    print(f'-------rotate_result---------')
    for pan_idx in range(N):
        print(pan[pan_idx][pointers[pan_idx]:]+pan[pan_idx][:pointers[pan_idx]])
    print(f'-------erase_result----------')
    for pan_idx in range(N):
        print(erase_grid[pan_idx][pointers[pan_idx]:] + erase_grid[pan_idx][:pointers[pan_idx]])


N, M, Q = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# 필요 배열 선언.
pointers = [0] * N
erase_grid = [[False] * M for _ in range(N)]

for _ in range(Q):
    # 0. 명령 정보 입력받기.
    x, d, k = map(int, input().split())

    # 1. 돌리기
    rotate(x-1, d, k)

    # 2. 지울 수 있는 숫자 지우기
    need_scaling = check()

    # 3. 만약 정규화가 필요하면 진행.
    if need_scaling:
        standard_scale()

# 4. 정답 연산 후 출력
answer = calc_answer()
print(answer)