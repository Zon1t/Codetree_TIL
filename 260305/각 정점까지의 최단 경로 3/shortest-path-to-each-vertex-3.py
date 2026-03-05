import sys; MAX_VALUE = sys.maxsize; input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
distances = [MAX_VALUE] * (N+1)
visited = [False] * (N+1)
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s][e] = w

distances[1] = 0
for i in range(1, N+1):
    min_idx = -1

    for j in range(1, N+1):
        if visited[j]:
            continue
        if min_idx == -1 or distances[min_idx] > distances[j]:
            min_idx = j

    visited[min_idx] = True
    for j in range(1, 1+N):
        if graph[min_idx][j] == 0:
            continue
        if distances[j] > distances[min_idx] + graph[min_idx][j]:
            distances[j] = distances[min_idx] + graph[min_idx][j]

for i in range(2, N+1):
    print(distances[i] if distances[i] != MAX_VALUE else -1)