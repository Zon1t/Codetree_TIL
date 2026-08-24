from collections import deque

N = int(input())
end = N**2
deltas = (1, -1, N, -N)

pos = []
curr_pos = -1
for i in range(N):
    temp = list(map(int, input().split()))
    if curr_pos == -1:
        for j in range(N):
            if temp[j] == 9:
                curr_pos = i*N+j
                temp[j] = 0
    pos.extend(temp)

def bfs():
    visited = 1<<curr_pos
    time_ = 0
    monsters = []
    Q = deque()
    Q.append((0, curr_pos))
    while Q:
        now_time, now_pos = Q.popleft()
        if time_ != now_time:
            if monsters:
                monsters.sort()
                return monsters[0], now_time
            time_ = now_time
        for d in deltas:
            next_pos = now_pos + d
            if not (0 <= next_pos < end) or (visited & 1<<next_pos):
                continue
            if (d==1 and next_pos%N==0) or (d==-1 and next_pos%N==N-1):
                continue
            if pos[next_pos] > level:
                continue
            elif 0 < pos[next_pos] < level:
                monsters.append(next_pos)
            visited |= 1 << next_pos
            Q.append((now_time+1, next_pos))
    return -1, -1

time, cnt, level = 0, 0, 2
while True:
    next_pos, delta = bfs()
    if next_pos == -1:
        break

    curr_pos = next_pos
    pos[curr_pos] = 0
    time += delta
    cnt += 1
    if cnt == level:
        level += 1
        cnt = 0
print(time)