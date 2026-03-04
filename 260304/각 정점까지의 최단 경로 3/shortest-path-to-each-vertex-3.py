n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

import heapq

MAX_DIST = 1
graph = [[] for _ in range(101)]
for s, e, w in edges:
    graph[s].append((e, w))
    MAX_DIST += w

distance = [MAX_DIST] * 101
distance[1] = 0

Q = [(0, 1)]
while Q:
    curr_dist, curr_node = heapq.heappop(Q)
    if curr_dist > distance[curr_node]:
        continue

    for next_node, weight in graph[curr_node]:
        dist = curr_dist + weight
        if dist > distance[next_node]:
            continue
        distance[next_node] = dist
        heapq.heappush(Q, (dist, next_node))
for i in range(2, n+1):
    print(distance[i] if distance[i] != MAX_DIST else -1)