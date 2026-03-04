n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

import sys; MAX_VALUE = sys.maxsize
import heapq

def dijkstra(start):
    distance[start] = 0
    Q = [(0, start)]
    while Q:
        curr_dist, curr_node = heapq.heappop(Q)
        if curr_dist > distance[curr_node]:
            continue
        
        for next_node, weight in graph[curr_node]:
            next_dist = curr_dist + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(Q, (next_dist, next_node))

distance = [MAX_VALUE] * (n+1)
graph = [[] for _ in range(n+1)]
for s, e, w in edges:
    graph[s].append((e, w))
    graph[e].append((s, w))

dijkstra(k)
for i in range(1, n+1):
    print(distance[i])