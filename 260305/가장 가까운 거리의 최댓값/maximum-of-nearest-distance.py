import heapq
import sys; MAX_VALUE = sys.maxsize

N, M = map(int, input().split())
A, B, C = map(int, input().split())
data_node = dict()
answer = 0
for _ in range(M):
    s, e, w = map(int, input().split())
    if data_node.get(s):
        data_node[s].append((e, w))
    else:
        data_node[s] = [(e, w)]
    if data_node.get(e):
        data_node[e].append((s, w))
    else:
        data_node[e] = [(s, w)]

def dijkstra(start):
    distances = [MAX_VALUE] * (N+1)
    distances[start] = 0
    Q = [(0, start)]
    while Q:
        curr_dist, curr_node = heapq.heappop(Q)
        if distances[curr_node] < curr_dist:
            continue
        for next_node, delta_dist in data_node.get(curr_node, (-1, -1)):
            if next_node == -1:
                continue
            next_dist = distances[curr_node] + delta_dist
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heapq.heappush(Q, (next_dist, next_node))
    return min(distances[A], distances[B], distances[C])

for node in data_node:
    total = dijkstra(node)
    if total == MAX_VALUE:
        continue
    answer = max(answer, total)
print(answer)