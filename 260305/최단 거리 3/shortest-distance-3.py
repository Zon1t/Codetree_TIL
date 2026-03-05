import sys; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())

graph = [[MAX_VALUE] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s][e] = graph[e][s] = min(graph[s][e], w)

start, end = map(int, input().split())
distance = [MAX_VALUE] * (N+1)
distance[start] = 0

visited = [False] * (N+1)
for i in range(1, 1+N):
    min_idx = -1

    for j in range(1, 1+N):
        if visited[j]:
            continue
        if min_idx == -1 or distance[min_idx] > distance[j]:
            min_idx = j
    visited[min_idx] = True
    for j in range(1, 1+N):
        if graph[min_idx][j] == MAX_VALUE:
            continue
        if distance[j] > distance[min_idx] + graph[min_idx][j]:
            distance[j] = distance[min_idx] + graph[min_idx][j]
print(distance[end])