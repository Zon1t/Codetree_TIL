# [] /
# 내가 가는 경로가 목적지에 도착한다는 것에 대한 보장을 어떻게 할 수 있을까
# 단순히 출발지, 목적지에서 bfs를 시작하면 그게 경로 위에 존재하는 노드들을 방문했다고 볼 수 있는건가
# dfs 메모이제이션으로 시간 안에 될라나

from collections import deque

N, M = map(int, input().split())
data = [[] for _ in range(N+1)]
revd = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    data[start].append(end)
    revd[end].append(start)

start, end = map(int, input().split())

pick = 1
visited = [0] * (N+1)
visited[end] = pick

Q = deque([end])
while Q:
    curr_node = Q.popleft()

    for next_node in revd[curr_node]:
        if visited[next_node] & pick:
            continue
        visited[next_node] |= pick
        Q.append(next_node)

pick = 2
visited[start] |= pick

Q.append(start)
while Q:
    curr_node = Q.popleft()

    if curr_node == end:
        continue

    for next_node in data[curr_node]:
        if visited[next_node] & pick:
            continue
        visited[next_node] |= pick
        Q.append(next_node)

first_set = set([node for node in range(1, N+1) if visited[node] == 3])


pick = 1
visited = [0] * (N+1)
visited[start] = pick

Q = deque([start])
while Q:
    curr_node = Q.popleft()

    for next_node in revd[curr_node]:
        if visited[next_node] & pick:
            continue
        visited[next_node] |= pick
        Q.append(next_node)

pick = 2
visited[end] |= pick

Q.append(end)
while Q:
    curr_node = Q.popleft()

    if curr_node == start:
        continue

    for next_node in data[curr_node]:
        if visited[next_node] & pick:
            continue
        visited[next_node] |= pick
        Q.append(next_node)

second_set = set([node for node in range(1, N+1) if visited[node] == 3])

print(len(first_set.intersection(second_set))-2)