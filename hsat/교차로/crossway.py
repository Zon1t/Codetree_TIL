# 16:02
# 분기문이 많아지나? 그렇게 어려운 문제는 아닌 것 같다?

from collections import deque

N = int(input())

cars = [deque() for _ in range(4)]
answer = ['-1'] * N

lst = []
for order in range(N):
    time, idx = input().split()
    time = int(time)
    lst.append((time, ord(idx)-ord('A'), order))

pointer = 0
curr_time = lst[0][0]
while pointer < N:

    while pointer < N and lst[pointer][0] == curr_time:
        _, idx, order = lst[pointer]
        cars[idx].append(order)
        pointer += 1

    while True:
        get_out, continue_flag = False, False
        for d in range(4):
            if continue_flag:
                continue_flag = False
                continue
            if cars[d] and not cars[d-1]:
                order = cars[d].popleft()
                answer[order] = str(curr_time)
                get_out, continue_flag = True, True

        if not get_out:
            break

        curr_time += 1
        while pointer < N and lst[pointer][0] == curr_time:
            _, idx, order = lst[pointer]
            cars[idx].append(order)
            pointer += 1

    curr_time = lst[pointer][0] if pointer < N else None

print('\n'.join(answer))