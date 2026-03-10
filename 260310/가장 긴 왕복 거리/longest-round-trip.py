import sys; input = sys.stdin.readline; MAX_VALUE = sys.maxsize
import heapq

N, M, X = map(int, input().split())
data = [[] for _ in range(N+1)]
data_inv = [[] for _ in range(N+1)]
ans = 0

for _ in range(M):
    s, e, d = map(int, input().split())
    data[s].append((d, e))
    data_inv[e].append((d, s))

def dijkstra(start, distances, data_dict):
    distances[start] = 0
    Q = [(0, start)]
    while Q:
        curr_dist, curr_node = heapq.heappop(Q)
        if curr_dist > distances[curr_node]:
            continue
        for delta, next_node in data_dict[curr_node]:
            next_dist = curr_dist + delta
            if next_dist < distances[next_node]:
                distances[next_node] = next_dist
                heapq.heappush(Q, (next_dist, next_node))

dist_X = [MAX_VALUE] * (N+1)
dist_inv_X = [MAX_VALUE] * (N+1)

dijkstra(X, dist_X, data)
dijkstra(X, dist_inv_X, data_inv)

for i in range(1, N+1):
    if i == X:
        continue
    ans = max(ans, dist_X[i] + dist_inv_X[i])
print(ans)