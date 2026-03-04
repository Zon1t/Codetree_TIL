import sys; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    e, s, w = map(int, input().split())
    graph[s].append((e, w))

distance = [MAX_VALUE] * (N+1)
distance[N] = 0

Q = [(0, N)]
while Q:
    curr_dist, curr_node = heapq.heappop(Q)
    if curr_dist > distance[curr_node]:
        continue
    for next_node, weight in graph[curr_node]:
        next_dist = curr_dist + weight
        if next_dist < distance[next_node]:
            distance[next_node] = next_dist
            heapq.heappush(Q, (next_dist, next_node))
print(max(distance[1:]))