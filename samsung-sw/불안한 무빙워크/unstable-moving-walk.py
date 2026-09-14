# 시작 04:51
# 1. 무빙워크 한 칸 회전
# 2. 회전 방향으로 사람 1칸 이동. 이동 불가시 X
# 3. 1번 칸 사람 올리기.
# 4. 안정성이 0인 칸 k개 이상이면 종료.

def move():
    global cnt
    for delta_idx in range(N-2, 0, -1):
        curr_idx = (pointer + delta_idx) % mod
        next_idx = (pointer + delta_idx + 1) % mod
        if human[curr_idx] and not human[next_idx] and moving_walk[next_idx]:
            human[curr_idx], human[next_idx] = False, True
            moving_walk[next_idx] -= 1

            if moving_walk[next_idx] == 0:
                cnt += 1

    if human[Nth_pos]:
        human[Nth_pos] = False


def custom_print():
    print(f'----moving_walk----')
    for i in range(mod):
        print(moving_walk[(pointer+i)%mod], end=' ')
        if i == N-1:
            print()
    print(f'----human----')
    for i in range(mod):
        print(human[(pointer+i)%mod], end=' ')
        if i == N-1:
            print()


N, K = map(int, input().split())
moving_walk = list(map(int, input().split()))
pointer, mod, cnt = 0, 2*N, 0

human = [False] * mod
turn = 0
while True:
    turn += 1

    # 1. 한 칸 회전
    pointer = (pointer - 1) % mod
    Nth_pos = (pointer + N - 1) % mod

    if human[Nth_pos]:
        human[Nth_pos] = False

    # 2. 사람 이동
    move()

    if cnt >= K:
        break

    # 3. 사람 올리기
    if moving_walk[pointer]:
        human[pointer] = True
        moving_walk[pointer] -= 1

        if moving_walk[pointer] == 0:
            cnt += 1

    if cnt >= K:
        break

print(turn)