# 해야 할 것. 1. 한 칸 먼저 회전시키기. 2. 이동 시키기. 3. 한 명 더 올리기. 4. 종료 체크하기.
# 위 과정을 반복하면 된다. 아마 큐의 rotate 등의 개념을 사용하면 풀이에 용이할 것으로 판단된다.
# 관리를 어떻게 하면 좋을까? 1번 위치(칸 아님)에 있는 건 pointer개념 활용. 사람은 set으로 둬서
# 업데이트를 하면 편할 것으로 생각된다.

# 중복되는 코드가 많은데 나중에 리팩토링하면서 고쳐보자.
# 주의할 점. 사람은 그냥 상대적인 위치가 아니라는거?

from collections import deque

def move():
    global zero_cnt

    # 번거롭지만 끝에 있는 사람은 따로 연산해주었다.
    if human:
        next_pos = (human[-1] + 1) % length
        if lst[next_pos] != 0:
            human[-1] = next_pos
            lst[human[-1]] -= 1

            if lst[human[-1]] == 0:
                zero_cnt += 1

    for i in range(human_cnt-2, -1, -1):
        # 내 위치 다음 한 칸을 찾는다.
        next_pos = (human[i]+1) % length

        # 다음 칸의 안정성이 0보다 크고 다음 위치에 내 앞사람이 없다면 한 칸 이동
        if lst[next_pos] and human[i+1] != next_pos:
            human[i] = next_pos
            lst[human[i]] -= 1

            if lst[human[i]] == 0:
                zero_cnt += 1

def check():
    global human_cnt
    if human and human[-1] == (pointer + N-1) % length:
        human.pop()
        human_cnt -= 1

def custom_print():
    print(human)
    print(*(lst[pointer:]+lst[:pointer]))


N, k = map(int, input().split())
lst = list(map(int, input().split()))

human = deque()
length = 2 * N
pointer = 0

human_cnt = 0
zero_cnt = 0
turn = 0

while True:
    turn += 1

    # 1. 한 칸 회전시키기.
    pointer = (pointer - 1) % length
    check()     # 사람 뺄 수 있으면 빼기

    # 2. 이동 시키기.
    move()
    check()     # 사람 뺄 수 있으면 빼기

    # 3. pointer 위치에 사람 올리기. 1번 칸에 사람이 있는 경우가 존재할 수 없다. 회전이 되기 때문
    if lst[pointer]:
        human.appendleft(pointer)   # pointer에 가까운 순으로 왼쪽에 배치된다.
        human_cnt += 1

        lst[pointer] -= 1
        if lst[pointer] == 0:
            zero_cnt += 1

    # 4. 안정성 검사 cnt가 k이상이면 종료하기.
    if zero_cnt >= k:
        break

print(turn)