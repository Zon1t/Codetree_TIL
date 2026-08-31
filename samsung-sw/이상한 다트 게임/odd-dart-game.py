''' 이상한 다트 게임 / 20260831 / 체감 난이도 : 실버 1
소요 시간 : 51분 / 시도 2회 (1회차 : 틀림) / 실행 시간 : 115ms / 메모리 : 19MB

타임 라인 : 구상 및 틀 만들기(15분) - 구현(22분) - 검증(10분) - 수정(4분)


[구상]
    - pointers 리스트를 만들고 이를 활용하면 회전 로직 분리 및 시/공간 복잡도를 낮출 수 있을 것이라
    기대하고 이를 기반으로 풀이 로직을 구성하였다.
    - 기능을 분리하고, 이를 바탕으로 함수와 실행부의 틀을 구성하였다.

[구현]
    - 삭제를 함에 있어 한 번에 일어나야 하는 과정이다 보니 이를 구현할 때 헷갈리는 부분이 좀 있었다. 몇 번
    쓰고 지우기를 반복하다 그냥 set에 집어넣고 나중에 업데이트하는 방향으로 로직 구성을 진행하였다.
    - 기타 로직들은 손쉽게 구현하고 custom_print 함수를 정의해 검증을 준비했다.

[검증]
    - 생각보다 수정할 부분이 많았다. 우선 정규화가 전체 원판에 대해서 평균값을 연산해 진행해야 하는 부분인데
    이를 원판별로 수행해야 한다고 잘못 이해했었다. 주어진 테케에선 정규화 과정까지 가는 경우가 없어 확인을
    하지 못했었는데, 직접 테케를 만들어 검증하니 이런 부분이 좋았다.
    - 다른 부분에 대해선 크게 걸리는 부분이 없다고 생각해서 곧바로 제출해보았다.

[수정]
    - 문제를 다시 읽자마자 문제점을 발견할 수 있었다. 회전 로직을 구성할 때 배수 칸을 다 돌려야 하는데, 해당
    칸만 회전을 시키고 있었다. 요즘 이런 실수가 잦은데 조심해야 할 필요가 있다.
    - 해당 로직을 추가하고 내 코드와 문제를 다시 비교해보고 제출했다.


썼던 테케
4 4 1
5 2 3 4
1 5 2 3
5 7 1 4
6 2 6 3
2 0 0

59 // 16 = 3
-> custom_print로 찍어보고 비교함.
'''

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
    need_scaling = True
    erase_set = set()
    # 판과 판 사이 위 아래로 인접한지 체크하기
    for pan_idx in range(N-1):
        for num_idx in range(M):
            first_num_idx, second_num_idx = (pointers[pan_idx]+num_idx)%M, (pointers[pan_idx+1]+num_idx)%M
            if pan[pan_idx][first_num_idx] == pan[pan_idx+1][second_num_idx] and pan[pan_idx][first_num_idx]:
                erase_set.add((pan_idx, first_num_idx))
                erase_set.add((pan_idx+1, second_num_idx))
                need_scaling = False

    # 양 옆으로 인접한지 체크하기.
    for pan_idx in range(N):
        for num_idx in range(M):
            if pan[pan_idx][num_idx] == pan[pan_idx][num_idx-1] and pan[pan_idx][num_idx]:
                erase_set.add((pan_idx, num_idx))
                erase_set.add((pan_idx, num_idx-1))
                need_scaling = False

    for pan_idx, num_idx in erase_set:
        pan[pan_idx][num_idx] = 0

    return need_scaling


def standard_scale():
    total = 0
    cnt = 0
    for pan_idx in range(N):
        for num_idx in range(M):
            if not pan[pan_idx][num_idx]:
                continue
            total += pan[pan_idx][num_idx]
            cnt += 1

    # 숫자가 남아있는 경우만 진행
    if cnt:
        avg = total // cnt
        for pan_idx in range(N):
            for num_idx in range(M):
                if not pan[pan_idx][num_idx]:
                    continue

                if pan[pan_idx][num_idx] > avg:
                    pan[pan_idx][num_idx] -= 1
                elif pan[pan_idx][num_idx] < avg:
                    pan[pan_idx][num_idx] += 1


def calc_answer():
    temp = 0
    for pan_idx in range(N):
        for num_idx in range(M):
            temp += pan[pan_idx][num_idx]
    return temp

def custom_print():
    print(f'-------result---------')
    for pan_idx in range(N):
        print(pan[pan_idx][pointers[pan_idx]:]+pan[pan_idx][:pointers[pan_idx]])

N, M, Q = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

# 필요 배열 선언.
pointers = [0] * N

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
