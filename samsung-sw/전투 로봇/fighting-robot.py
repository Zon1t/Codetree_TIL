# 뇌절해보자 : 비트마스킹 + heapq

from heapq import heappop, heappush

def kill_check(cur, cur_Lv):
    q = []
    # (거리, x좌표, y좌표)
    heappush(q, (0, cur//N, cur%N))

    visited = 0
    visited |= 1<<cur

    while q:
        dist, cx, cy = heappop(q)
        now = cx*N + cy

        monster_Lv = matrix[now]

        if 0 < monster_Lv < cur_Lv:
            return (dist, cx, cy, monster_Lv, now)

        for d in dxdy:
            nxt = now + d
            if (d==1 and nxt%N==0) or (d==-1 and nxt%N==N-1):
                continue
            if 0 <= nxt < N**2:
                if not (visited&(1 << nxt)) and matrix[nxt] <= cur_Lv:
                    visited |= (1 << nxt)
                    heappush(q, (dist + 1, nxt//N, nxt%N))

    return (-1, -1, -1, -1, -1)

N = int(input())
dxdy = (1, -1, N, -N)

matrix = []
for i in range(N):
    matrix.extend(list(map(int, input().split())))

cur = -1
for j, val in enumerate(matrix):
    if val == 9:
        cur = j
        matrix[j] = 0 # 이거 안해주면 나중에 못감

cur_Lv = 2
cur_exp = 0
time = 0

while True:
    dist, nx, ny, monster_Lv, nxt = kill_check(cur, cur_Lv)

    if dist == -1:
        break

    time += dist            # 죽임
    matrix[nxt] = 0
    cur_exp += 1
    if cur_exp == cur_Lv:   # 레벨업
        cur_Lv += 1
        cur_exp = 0
    cur = nxt               # 이동

print(time)