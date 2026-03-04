import sys; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))


end, start = map(int, input().split())
distance = [MAX_VALUE]*(N+1)
distance[start] = 0
path = [0] * (N+1)
Q = [(0, start)]
while Q:
    curr_dist, curr_node = heapq.heappop(Q)
    if curr_dist > distance[curr_node]:
        continue
    for next_node, weight in graph[curr_node]:
        next_dist = curr_dist + weight
        if next_dist < distance[next_node]:
            distance[next_node] = next_dist
            path[next_node] = curr_node
            heapq.heappush(Q, (next_dist, next_node))
print(distance[end])
pointer = end
while pointer != start:
    print(pointer, end=' ')
    pointer = path[pointer]
print(start)