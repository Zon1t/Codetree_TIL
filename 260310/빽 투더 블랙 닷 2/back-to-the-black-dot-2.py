import sys; input = sys.stdin.readline; MAX_VALUE = sys.maxsize
import heapq

N, M = map(int, input().split())
R1, R2 = map(int, input().split())
data = [[] for _ in range(N+1)]
answer = MAX_VALUE

for _ in range(M):
    s, e, d = map(int, input().split())
    data[s].append((d, e))
    data[e].append((d, s))

dist_r1 = [MAX_VALUE] * (N+1)
dist_r2 = [MAX_VALUE] * (N+1)

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

dijkstra(R1, dist_r1, data)
dijkstra(R2, dist_r2, data)

for i in range(1, N+1):
    if i == R1 or i == R2:
        continue
    answer = min(answer, dist_r1[i] + dist_r1[R2] + dist_r2[i])

print(answer if answer != MAX_VALUE else -1)