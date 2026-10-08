# 1. 공장 설립
#       - 그냥 적절하게 물건 배치하면 된다.
#       - n, m, ids, ws 입력 형식에 주의

# 2. 물건 하차
#       - pointer를 활용하는 문제인 것 같다.
#       - 맨 뒤로 보내는 것도 (pointer + 1) % belt_cnt
#       - 하차 처리? 그냥 pop해도 되는건가 싶긴하다. removed_set에 기록

# 3. 물건 제거
#       - 직접 pop해줘야 하나? 그냥 lazy하게 처리해도 될 것 같고.. -> lazy하게 처리
#       - removed에 기록은 해줘야 한다.

# 4. 물건 확인
#       - removed에 있다면 바로 -1 반환
#       - 어디 벨트에 저장되어 있는지도 체크. 즉 데이터 저장할 때 벨트 넘버도 기록하자.

# 5. 벨트 고장
#       - 이미 망가진 벨트면 -1 반환
#       - 아니면 오른쪽 방향으로 벨트 확인. 발견하면 상자들 쭉 옮겨주기.
#       - 개수 업데이트 잘하기. 고장난 벨트 체크.


# 각 함수별 호출 횟수에 대한 제한은 없고 그냥 총 쿼리 수만 나와있음.
# 고루고루 잘 작동할 수 있게끔 하면 될 것 같다.
# 시간 초과 발생시 제거 로직을 손보면 되겠다. 구현 ㄱㄱ

import sys; input = sys.stdin.readline


class Node:
    __slots__ = ('idx', 'belt_num', 'weight', 'prev_node', 'next_node')
    
    def __init__(self, idx, belt_n, weight, prev_node=None, next_node=None):
        self.idx = idx
        self.belt_num = belt_n
        self.weight = weight
        self.prev_node = prev_node
        self.next_node = next_node


def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def command_100(data):
    cur = 3
    for belt_num in range(M):
        idx, weight = data[cur], data[cur+N]

        start_node = prv = Node(idx, belt_num, weight)
        front[belt_num] = start_node

        present_info[idx] = start_node
        cur += 1

        for _ in range(init_cnt-1):
            idx, weight = data[cur], data[cur+N]
            node = Node(idx, belt_num, weight)

            prv.next_node, node.prev_node = node, prv
            prv = node

            present_info[idx] = node
            cur += 1

        prv.next_node, start_node.prev_node = start_node, prv


def command_200(w_max):
    acc = 0
    for belt_n in range(M):
        if broken[belt_n] or front[belt_n] is None:
            continue

        curr_node = front[belt_n]

        if curr_node.weight <= w_max:
            acc += curr_node.weight
            removed.add(curr_node.idx)

            prv = curr_node.prev_node
            if prv == curr_node:
                front[belt_n] = None
                continue

            nxt = curr_node.next_node
            prv.next_node = nxt
            nxt.prev_node = prv

        front[belt_n] = curr_node.next_node

    return acc


def command_300(r_id):
    if r_id in removed or r_id not in present_info:
        return -1

    node = present_info[r_id]
    prv, nxt = node.prev_node, node.next_node
    belt_n = find(node.belt_num)

    if prv == node:
        front[belt_n] = None
    else:
        prv.next_node = nxt
        nxt.prev_node = prv
        if front[belt_n] == node:
            front[belt_n] = nxt

    removed.add(r_id)
    return r_id


def command_400(f_id):
    if f_id in removed or f_id not in present_info:
        return -1

    belt_num = find(present_info[f_id].belt_num)
    front[belt_num] = present_info[f_id]
    return belt_num + 1


def command_500(belt_n):
    if broken[belt_n]:
        return -1

    broken[belt_n] = True
    next_belt = (belt_n + 1) % M
    while True:
        if broken[next_belt]:
            next_belt = (next_belt + 1) % M
            continue

        parent[belt_n] = next_belt

        if front[belt_n] is None:
            pass
        elif front[next_belt] is None:
            front[next_belt] = front[belt_n]
        else:
            cur_prv, nxt_prv = front[belt_n].prev_node, front[next_belt].prev_node
            front[belt_n].prev_node, nxt_prv.next_node = nxt_prv, front[belt_n]
            front[next_belt].prev_node, cur_prv.next_node = cur_prv, front[next_belt]

        return belt_n + 1


# =====================================================================
# 세팅

Q = int(input())
init_data = list(map(int, input().split()))
commands = [map(int, input().split()) for _ in range(Q-1)]

N, M = init_data[1], init_data[2]
init_cnt = N//M

present_info = dict()               # id: (weight, belt_n)
removed = set()                     # 삭제된 애들
front = [None] * M

command_100(init_data)

parent = [i for i in range(M)]
broken = [False] * M

answer = []

# =====================================================================
# 실행부

for command, *data in commands:
    if command == 200: answer.append(str(command_200(data[0])))
    if command == 300: answer.append(str(command_300(data[0])))
    if command == 400: answer.append(str(command_400(data[0])))
    if command == 500: answer.append(str(command_500(data[0]-1)))

print('\n'.join(answer))